from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Knowledge base documents
documents = [
    """
    Agentic AI is a type of artificial intelligence system that can reason,
    plan, use tools, maintain memory, and take actions to complete a goal.
    """,

    """
    Retrieval-Augmented Generation, or RAG, is a method where relevant
    information is retrieved from documents and given to an LLM as context
    before generating an answer.
    """,

    """
    Embeddings are numerical vector representations of text. They capture
    semantic meaning, so similar concepts are placed close together in vector space.
    """,

    """
    Sentence Transformers are models that convert sentences or paragraphs
    into embeddings. These embeddings are useful for semantic search,
    recommendation systems, RAG, and agent memory.
    """,

    """
    Prompt Engineering is the process of writing effective instructions
    for an LLM. Good prompts include role, task, context, constraints,
    and output format.
    """
]


# 2. Simple chunking
def chunk_documents(documents):
    chunks = []

    for doc in documents:
        cleaned_doc = doc.strip()
        chunks.append(cleaned_doc)

    return chunks


# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 4. Create embeddings for document chunks
chunks = chunk_documents(documents)
chunk_embeddings = model.encode(chunks)


# 5. Retrieve most relevant chunk
def retrieve_context(user_query):
    query_embedding = model.encode([user_query])

    similarities = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    best_index = similarities.argmax()
    best_chunk = chunks[best_index]
    best_score = similarities[best_index]

    return best_chunk, best_score


# 6. Generate answer using retrieved context
def generate_answer(user_query, context, score):
    answer = f"""
Question:
{user_query}

Retrieved Context:
{context}

Similarity Score:
{score:.4f}

Answer:
Based on the retrieved context, {context}
"""
    return answer


# 7. Chatbot loop
def rag_chatbot():
    print("Simple RAG Chatbot Started")
    print("Type 'exit' to stop.\n")

    while True:
        user_query = input("You: ")

        if user_query.lower() == "exit":
            print("Chatbot stopped.")
            break

        context, score = retrieve_context(user_query)
        answer = generate_answer(user_query, context, score)

        print("\nBot:")
        print(answer)


if __name__ == "__main__":
    rag_chatbot()