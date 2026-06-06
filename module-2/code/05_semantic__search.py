from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Machine Learning Basics",
    "Deep Learning Tutorial",
    "Neural Networks Guide",
    "Cooking Pasta Recipe"
]

query = "Artificial Intelligence"

query_embedding = model.encode(query)

best_doc = None
best_score = -1

for doc in documents:

    doc_embedding = model.encode(doc)

    score = cosine_similarity(
        [query_embedding],
        [doc_embedding]
    )[0][0]

    print(f"{doc} -> {score:.4f}")

    if score > best_score:
        best_score = score
        best_doc = doc

print("\nMost Relevant Document:")
print(best_doc)

"""
-----------------------------------Output----------------------------
achine Learning Basics -> 0.5439
Deep Learning Tutorial -> 0.3434
Neural Networks Guide -> 0.3587
Cooking Pasta Recipe -> 0.0876

Most Relevant Document:
Machine Learning Basics


"""