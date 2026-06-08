import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


MEMORY_TEXT_FILE = "faiss_memories.json"
FAISS_INDEX_FILE = "memory_index.faiss"

model = SentenceTransformer("all-MiniLM-L6-v2")
EMBEDDING_DIM = 384


def load_memories():
    if os.path.exists(MEMORY_TEXT_FILE):
        with open(MEMORY_TEXT_FILE, "r") as file:
            return json.load(file)
    return []


def save_memories(memories):
    with open(MEMORY_TEXT_FILE, "w") as file:
        json.dump(memories, file, indent=4)


def load_index():
    if os.path.exists(FAISS_INDEX_FILE):
        return faiss.read_index(FAISS_INDEX_FILE)

    return faiss.IndexFlatL2(EMBEDDING_DIM)


def save_index(index):
    faiss.write_index(index, FAISS_INDEX_FILE)


def add_memory(memory_text):
    memories = load_memories()
    index = load_index()

    embedding = model.encode([memory_text])
    embedding = np.array(embedding).astype("float32")

    index.add(embedding)

    memories.append(memory_text)

    save_memories(memories)
    save_index(index)

    return "Memory saved successfully."


def search_memory(query, top_k=3):
    memories = load_memories()
    index = load_index()

    if len(memories) == 0:
        return []

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue

        results.append({
            "memory": memories[idx],
            "distance": float(distance)
        })

    return results


def memory_agent(user_input):
    user_input_lower = user_input.lower()

    if user_input_lower.startswith("remember"):
        memory_text = user_input.replace("remember", "").strip()
        return add_memory(memory_text)

    elif user_input_lower.startswith("recall"):
        query = user_input.replace("recall", "").strip()
        results = search_memory(query)

        if not results:
            return "No memories found."

        response = "Relevant memories:\n"

        for item in results:
            response += f"- {item['memory']} | distance: {item['distance']:.4f}\n"

        return response

    else:
        results = search_memory(user_input)

        if not results:
            return "I do not have relevant memory yet."

        context = "\n".join([item["memory"] for item in results])

        return f"""
Relevant memories found:

{context}

Personalized response:
Based on your memories, I can answer in a more relevant way.
"""


def main():
    print("FAISS Memory Agent")
    print("Commands:")
    print("remember <something>")
    print("recall <query>")
    print("exit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = memory_agent(user_input)

        print("\nAgent:")
        print(response)


if __name__ == "__main__":
    main()