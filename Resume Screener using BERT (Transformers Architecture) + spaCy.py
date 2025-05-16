# Import libraries
from transformers import pipeline
import spacy

# Load Huggingface BERT NER pipeline
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Example resume text
resume_text = """
I am a data scientist skilled in Python, Machine Learning, Deep Learning, Data Science and Natural Language Processing.
I have experience working with TensorFlow, PyTorch, and Scikit-Learn.
"""
# Step 1: Extract named entities using BERT
ner_results = ner_pipeline(resume_text)

print("---- Named Entities by BERT ----")
for entity in ner_results:
    print(f"{entity['word']} --> {entity['entity']} (Score: {entity['score']:.2f})")


# Step 2: Define a simple list of technical skills (you can expand this list)
skills_list = [
    "Python", "Machine Learning", "Deep Learning", "NLP", "TensorFlow",
    "PyTorch", "Scikit-Learn", "Data Science", "Artificial Intelligence"
]

# Step 3: Extract skills manually using spaCy
doc = nlp(resume_text)


extracted_skills = []

for token in doc:
    if token.text in skills_list:
        extracted_skills.append(token.text)


# Remove duplicates
extracted_skills = list(set(extracted_skills))


print("\n---- Extracted Skills ----")
print(extracted_skills)
