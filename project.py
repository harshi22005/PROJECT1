from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked


if __name__ == "__main__":
    print("\nAI-Powered Resume Ranker (Single File Version)\n")

    job_description = input("Enter Job Description:\n")

    resumes = [
        "Python developer with experience in machine learning, SQL and data analysis",
        "Web developer skilled in HTML CSS JavaScript and Flask",
        "Data analyst with Python pandas machine learning and visualization skills"
    ]

    results = rank_resumes(job_description, resumes)

    print("\n--- Resume Ranking ---")
    for rank, (index, score) in enumerate(results, start=1):
        print(f"Rank {rank}: Resume {index+1}  -->  {round(score*100, 2)}%")
