AI-Powered Resume Ranking System

An AI-based resume ranking system that evaluates and ranks candidate resumes against a given job description using Natural Language Processing (NLP) techniques. The system leverages TF-IDF vectorization and cosine similarity to measure relevance objectively.

📌 Overview

Recruiters often spend significant time manually screening resumes. This project demonstrates how basic NLP techniques can be applied to automate resume screening by ranking resumes based on their similarity to a job description.

This project is implemented as a single Python script and is intended for learning and demonstration purposes.

⚙️ Key Features

Automated resume ranking based on job relevance

Uses TF-IDF for text vectorization

Measures similarity using cosine similarity

Lightweight and easy to run

Suitable for beginner-to-intermediate NLP projects

🧠 Technical Approach

Combine the job description and resumes into a single corpus

Convert text data into numerical vectors using TF-IDF

Compute similarity scores using cosine similarity

Rank resumes based on similarity scores

🛠️ Tech Stack

Programming Language: Python

Libraries:

scikit-learn

NumPy (indirect dependency)

Concepts:

Natural Language Processing (NLP)

TF-IDF Vectorization

Cosine Similarity

📂 Project Structure
resume-ranking-system/
│
├── resume_ranker.py
└── README.md

📦 Installation

Ensure Python 3.x is installed on your system.

Install required dependencies:

pip install scikit-learn

▶️ Usage

Clone the repository:

git clone https://github.com/your-username/resume-ranking-system.git


Navigate to the project directory:

cd resume-ranking-system


Run the application:

python resume_ranker.py


Enter the job description when prompted.
The system will display ranked resumes with similarity scores.

📊 Sample Output
--- Resume Ranking ---
Rank 1: Resume 3 --> 86.45%
Rank 2: Resume 1 --> 79.12%
Rank 3: Resume 2 --> 41.87%

🚀 Potential Enhancements

Support for resume file uploads (PDF/DOCX)

Integration of word embeddings (Word2Vec, BERT)

Development of a web-based interface

Improved preprocessing (lemmatization, keyword weighting)

📄 License

This project is open-source and available for educational purposes.

👤 Author

G Harshitha
Aspiring AI / Machine Learning Engineer
