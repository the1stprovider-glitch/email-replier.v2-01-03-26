from sentence_transformers import SentenceTransformer
import numpy as np

class StyleModel:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = []

    def learn_from_sent(self, emails):
        for email in emails:
            emb = self.model.encode(email)
            self.embeddings.append(emb)

    def get_style_embedding(self):
        if not self.embeddings:
            return None
        return np.mean(self.embeddings, axis=0)
