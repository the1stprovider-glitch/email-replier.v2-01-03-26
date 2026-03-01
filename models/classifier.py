from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from config import MODEL_NAME

class EmailClassifier:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME, num_labels=3)

    def classify(self, text):
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, padding=True)

        outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        score = torch.max(probs).item()
        category = torch.argmax(probs).item()

        labels = ["Very Important", "Medium Important", "Not Important"]
        return labels[category], score
