from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

class TopicModeler:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(model_name)
        self.model = BERTopic(embedding_model=self.embedding_model)

    def fit_transform(self, documents):
        print("Training BERTopic model...")
        topics, probs = self.model.fit_transform(documents)
        return topics, probs

    def get_topics_info(self):
        return self.model.get_topic_info()
