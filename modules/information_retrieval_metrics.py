import math

class InformationRetrievalMetrics:
    """
    A class to calculate information retrieval metrics for evaluating the effectiveness
    of search and retrieval systems.

    Attributes:
        retrieved (list): A list of document identifiers (like passage IDs) retrieved by the search system.
        relevant (set): A set of document identifiers that are relevant to the query.

    Methods:
        precision(): Calculate the precision of the retrieved documents.
        recall(): Calculate the recall of the retrieved documents.
        f1_score(): Calculate the F1 score, the harmonic mean of precision and recall.
        mean_reciprocal_rank(): Calculate the mean reciprocal rank of the retrieved documents.
        ndcg(): Calculate the normalized discounted cumulative gain for the retrieved documents.
        average_precision(): Calculate the average precision across the retrieved documents.
        precision_at_k(k): Calculate the precision at the first k documents.
        recall_at_k(k): Calculate the recall at the first k documents.
    """

    def __init__(self, retrieved, relevant):
        """
        Constructs all the necessary attributes for the InformationRetrievalMetrics object.

        Parameters:
            retrieved (list): The list of documents retrieved by the search system.
            relevant (set): The set of documents that are considered relevant to the query.
        """
        self.retrieved = retrieved
        self.relevant = set(relevant)

    def precision(self):
        """Calculate the precision of the retrieved documents as the proportion of retrieved documents that are relevant."""
        retrieved_relevant = [doc for doc in self.retrieved if doc in self.relevant]
        if not self.retrieved:
            return 0
        return len(retrieved_relevant) / len(self.retrieved)

    def recall(self):
        """Calculate the recall of the retrieved documents as the proportion of relevant documents that are retrieved."""
        retrieved_relevant = [doc for doc in self.retrieved if doc in self.relevant]
        if not self.relevant:
            return 0
        return len(retrieved_relevant) / len(self.relevant)

    def f1_score(self):
        """Calculate the F1 score, which is the harmonic mean of precision and recall."""
        prec = self.precision()
        rec = self.recall()
        if prec + rec == 0:
            return 0
        return 2 * (prec * rec) / (prec + rec)

    def mean_reciprocal_rank(self):
        """Calculate the mean reciprocal rank (MRR) for the first correct answer in the retrieved list."""
        for index, doc in enumerate(self.retrieved):
            if doc in self.relevant:
                return 1 / (index + 1)
        return 0

    def ndcg(self):
        """Calculate the normalized discounted cumulative gain (nDCG) based on the 
        positions of relevant documents."""
        dcg = 0
        for i, doc in enumerate(self.retrieved):
            if doc in self.relevant:
                dcg += 1 / math.log2(i + 2)  # log base 2 of index+2
        idcg = sum(1 / math.log2(i + 2) for i in range(len(self.relevant)))
        if idcg == 0:
            return 0
        return dcg / idcg

    def average_precision(self):
        """Calculate the average precision (AP) as the mean of precision values at each point a relevant document is retrieved."""
        cum_prec = 0
        relevant_retrieved = 0
        for i, doc in enumerate(self.retrieved):
            if doc in self.relevant:
                relevant_retrieved += 1
                cum_prec += relevant_retrieved / (i + 1)
        if relevant_retrieved == 0:
            return 0
        return cum_prec / len(self.relevant)

    def precision_at_k(self, k):
        """Calculate the precision at the top k retrieved documents."""
        return self.precision()[:k]

    def recall_at_k(self, k):
        """Calculate the recall at the top k retrieved documents."""
        return self.recall()[:k]

# Example usage:
retrieved = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
relevant = {'doc1', 'doc3', 'doc6', 'doc7'}
metrics = InformationRetrievalMetrics(retrieved, relevant)

print("Precision:", metrics.precision())
print("Recall:", metrics.recall())
print("F1-Score:", metrics.f1_score())
print("MRR:", metrics.mean_reciprocal_rank())
print("nDCG:", metrics.ndcg())
