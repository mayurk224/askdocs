import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

load_dotenv()

# --- LLM Setup ---
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is required")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

st.title("AskDocs - Document Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    try:
        loader = PyPDFLoader("temp.pdf")
        documents = loader.load()
    finally:
        if os.path.exists("temp.pdf"):
            os.unlink("temp.pdf")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    st.success("PDF loaded. Ask your question below.")

    question = st.text_input("Ask a question about your document:")

    if question:
        with st.spinner("Thinking..."):
            result = qa_chain.invoke(question)
            answer = result["result"]
        st.write("### Answer")
        st.write(answer)