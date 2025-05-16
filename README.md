# Resume-Screener-using-BERT-Transformers-Architecture-spaCy
This project aims to automate and improve the resume screening process by leveraging powerful Natural Language Processing (NLP) techniques. It combines BERT-based transformer embeddings for semantic understanding and spaCy's Named Entity Recognition (NER) to extract structured information from resumes. The system evaluates how well a candidate’s resume matches a given job description by computing similarity scores and highlighting relevant skills and qualifications.


---

Key Features

Semantic Matching using BERT: Uses pre-trained BERT models to generate contextual embeddings of resumes and job descriptions for deep semantic comparison.
NER with spaCy: Extracts candidate details like Name, Email, Skills, Education, and Experience from unstructured resumes using spaCy's NER pipeline.
Resume Ranking: Computes cosine similarity between job descriptions and resume embeddings to rank candidates based on job-fit.
Multi-format Support: Supports resume input in formats like .pdf, .docx, and .txt.
Structured Output: Outputs matched resumes along with extracted entities in a clean, structured JSON or CSV format.
--

Tech Stack / Libraries Used
Python 3
Transformers (Hugging Face) – For BERT-based embeddings
spaCy – For custom NER entity extraction
Scikit-learn – For cosine similarity and model evaluation
Pandas, NumPy – For data manipulation
pdfplumber / docx2txt – For parsing resume files
---

Workflow

1. Input: Upload a job description and a batch of candidate resumes.
2. NER Extraction: spaCy extracts key information from each resume.
3. Embedding Generation: BERT encodes both resumes and job descriptions into dense vectors.
4. Similarity Calculation: Cosine similarity is used to compute the relevance of each resume to the job post.
5. Ranking: Resumes are sorted and top-N most relevant resumes are returned with structured info.

---

Use Cases

HR Tech platforms to automate resume screening

Applicant Tracking Systems (ATS)

Job portals and recruitment agencies

Internal tools for talent acquisition teams.
