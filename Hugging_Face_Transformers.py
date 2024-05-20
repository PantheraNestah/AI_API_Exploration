import requests
from transformers import pipeline

# Set up Hugging Face pipeline for QA
qa_pipeline = pipeline("question-answering")

user_query = "Air pollution prevention techniques"

result = qa_pipeline(question=user_query, context="Air pollution is caused by Oxides of Nitrogen and Sulphur")

# Response
print(result['answer'])