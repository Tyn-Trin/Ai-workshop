import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="documents")


def add_document(doc_id: str, text: str):
    collection.add(
        ids=[doc_id],
        documents=[text]
    )


def search_documents(query: str, n_results: int = 3) -> list[str]:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0]
