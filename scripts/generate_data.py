import pandas as pd
import numpy as np


def generate_ranking_synthetic_data():
    # Constants
    NUM_QUERIES = 5
    DOCS_PER_QUERY = 10

    # Seed for reproducibility
    np.random.seed(42)

    # Create the dataset
    data = []
    for query_id in range(1, NUM_QUERIES + 1):
        # Simulate a random order for documents
        docs_order = np.random.permutation(DOCS_PER_QUERY) + 1
        for doc_index, doc_id in enumerate(docs_order):
            document = f"doc{query_id}_{doc_id}"
            is_relevant = np.random.choice([0, 1], p=[0.7, 0.3])  # 30% chance of being relevant
            data.append({
                "Query": f"Query{query_id}", 
                "Document ID": document, 
                "Is Relevant": is_relevant,
                "Retrieval Order": doc_index + 1  # Add 1 to start from 1 instead of 0
            })

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    csv_file_path = "data/Synthetic_IR_Data.csv"
    df.to_csv(csv_file_path, index=False)


def generate_q_a_synthetic_data():

    # Sample data with some incorrect answers
    data_samples = {
        'question': [
            'When was the first super bowl?',
            'Who won the most super bowls?',
            'What is the capital of France?',
            'Who wrote "Macbeth"?',
            'What element has the chemical symbol "O"?',
            'When did the Titanic sink?',
            'Who is known as the father of computers?',
            'What is the tallest mountain in the world?',
            'What year did World War II begin?',
            'Who painted the Mona Lisa?'
        ],
        'answer': [
            'The first superbowl was held on February 15, 1967',  # Incorrect date
            'The Pittsburgh Steelers have the most super bowl wins',  # Incorrect, vague
            'The capital of France is Lyon',  # Incorrect city
            'Macbeth was written by Charles Dickens',  # Incorrect author
            'The chemical symbol "O" stands for Osmium',  # Incorrect element
            'The Titanic sank in 1905',  # Incorrect year
            'The father of computers is Alan Turing',  # Incorrect, commonly confused
            'The tallest mountain in the world is K2',  # Incorrect mountain
            'World War II began in 1941',  # Incorrect year
            'The Mona Lisa was painted by Michelangelo'  # Incorrect painter
        ],
        'ground_truth': [
            'The first superbowl was held on January 15, 1967',
            'The New England Patriots have won the Super Bowl a record six times',
            'Paris is the capital of France',
            'William Shakespeare wrote "Macbeth"',
            'Oxygen is represented by the chemical symbol "O"',
            'The Titanic sank on April 15, 1912',
            'Charles Babbage is considered the father of the computer',
            'Mount Everest is the highest mountain in the world',
            'World War II started in the year 1939',
            'Leonardo da Vinci painted the Mona Lisa'
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data_samples)
    df.to_csv('data/q_a_synthetic_data.csv', index=False)

generate_q_a_synthetic_data()