from langchain_community.vectorstores import FAISS

def build_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever()