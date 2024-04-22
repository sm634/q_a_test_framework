import pandas as pd
from datasets import Dataset
from ragas.metrics import answer_similarity
from ragas import evaluate


dataset = pd.read_csv('data/q_a_synthetic_data.csv')
breakpoint()
dataset = dataset.to_dict()
dataset = Dataset.from_dict(dataset)
score = evaluate(dataset,metrics=[answer_similarity])
score.to_pandas()

breakpoint()
