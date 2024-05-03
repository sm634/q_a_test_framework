import re
import pandas as pd
from tqdm import tqdm

from connectors.elasticsearch_connector import WatsonDiscoveryV2Connector
from utils.files_handler import FileHandler


file_handler = FileHandler()

def replace_after_pipe(text):
    # Pattern to match everything after the first occurrence of '|'
    pattern = r'\|.*$'
    # Replacement text
    replacement = ''
    # Substitute the matched pattern with the replacement text
    result = re.sub(pattern, replacement, text)
    return result

def replace_special_patterns(text):
    pattern = r'[\t]'
    replacement = ''
    result = re.sub(pattern, replacement, text)
    return result

def custom_preprocess(text):
    preprocessed_string = replace_after_pipe(text)
    preprocessed_string = re.sub(' ', '', string=preprocessed_string)
    preprocessed_string = preprocessed_string.lower()
    return preprocessed_string

def run_vodafone_test(version='Apr2024'):

    if version == 'Apr2024':
        df = file_handler.get_df_from_file('TestCase_Discovery_Apr2024.csv')

        # first filter to only keep the test input queries you want.
        df = df.loc[df['keep_faq_for_test'] == 'Y']
        df = df.loc[df['User Input'] != float('nan')]

        # extract the columns out into lists.
        user_inputs = df['User Input'].to_list()
        correct_faqs = df['Correct FAQ'].to_list()
        actual_faqs = []
        correct_faq_in_top_3 = []
        urls = df['Associated URL'].to_list()
        top_3_titles_with_confidence = []

        # instantiate the discovery class
        discovery_instance = WatsonDiscoveryV2Connector()

        # get the queries json for a test query.
        file_handler.get_queries_from_json('vodafone_discovery_queries.json')
        collections_list = file_handler.queries_json["collections"]
        # run the test response to get query responses.

        for _ in tqdm(range(0, len(user_inputs)), desc="User Inputs/Queries Completed"):
            query = user_inputs[_]
            correct_faq = correct_faqs[_]

            discovery_instance.query_response(
                query=query,
                collection_ids=collections_list
            )
            # From the results, get the top 3 titles.
            try:
                top_3_titles = discovery_instance.get_title()[:3]
                top_3_titles = [replace_after_pipe(title) for title in top_3_titles]

                top_title = top_3_titles[0]
                actual_faqs.append(top_title)

                # standardize correct_faq and returned titles
                correct_faq_preprocessed = custom_preprocess(correct_faq)
                top_3_titles_preprocessed = [custom_preprocess(title) for title in top_3_titles]
            
                # compare top title with correct faq.
                if correct_faq_preprocessed in top_3_titles_preprocessed:
                    correct_faq_in_top_3.append('Y')
                else:
                    correct_faq_in_top_3.append('N')

                # get top 3 titles with confidence scores.
                top_3_confidence_scores = discovery_instance.get_result_confidence()[:3]
                top_3_titles_confidence_dict = {}
                for i in range(0, len(top_3_titles)):
                    title = top_3_titles[i]
                    confidence = top_3_confidence_scores[i]

                    top_3_titles_confidence_dict[title] = confidence
                
                top_3_titles_with_confidence.append(top_3_titles_confidence_dict)
            
            except Exception as e:
                message = f"ERROR: {e}"
                actual_faqs.append(message)
                correct_faq_in_top_3.append(message)
                top_3_titles_with_confidence.append(message)
                pass
        
        # Check to see that all values are equal length.
        if len(user_inputs) != len(correct_faqs) != len(actual_faqs) != len(correct_faq_in_top_3) != len(top_3_titles_with_confidence) != len(urls):
            breakpoint() 

        # Prepare output
        output_data = {
            'User Input': user_inputs,
            'Correct FAQ': correct_faqs,
            'Actual FAQ returned (Top result)': actual_faqs,
            'Correct FAQ in top 3': correct_faq_in_top_3,
            'Top 3 returned FAQ with Confidence Scores': top_3_titles_with_confidence,
            'Associated URL': urls
        }
        output_df = pd.DataFrame(output_data)
        
        # Save output.
        file_handler.save_df_to_csv(df=output_df, file_name='TestCase_Discovery_Apr2024_output')
