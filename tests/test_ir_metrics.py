from modules.information_retrieval_metrics import InformationRetrievalMetrics
import pandas as pd


def test_ir_metrics():
    data = pd.read_csv('data/Synthetic_IR_Data.csv')

    queries = data['Query']
    retrieved = data['Document ID']
    is_relevant = data['Is Relevant']

    metrics = InformationRetrievalMetrics(
        retrieved=retrieved,
        relevant=is_relevant
    )


    precision = metrics.precision()
    recall = metrics.recall()
    f1_score = metrics.f1_score()
    mrr = metrics.mean_reciprocal_rank()
    ndcg = metrics.ndcg()

    return None



# for query in data['Query']:
#     """Getting metric scores per query"""

#     temp_data = data[data['Query'] == query]
#     query = temp_data['Query']
#     retrieved_doc = temp_data['Document ID'] 
#     is_relevant = temp_data['Is Relevant']


#     precision = metrics.precision()
#     recall = metrics.recall()
#     f1_score = metrics.f1_score()
#     mrr = metrics.mean_reciprocal_rank()
#     ndcg = metrics.ndcg()
#     avg_precision = metrics.average_precision()
#     precision_at_k = metrics.precision_at_k(k=3)
#     recall_at_k = metrics.recall_at_k(k=3)
