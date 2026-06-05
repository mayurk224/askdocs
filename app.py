import os
import tempfile
import streamlit as st
from core.loader import load_and_chunk_pdf
from core.embeddings import get_embeddings
from core.vectorstore import build_vectorstore
from core.chain import build_qa_chain

st.title("AskDocs - Document Q&A Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None and st.session_state.qa_chain is None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    try:
        chunks = load_and_chunk_pdf(tmp_path)
        embeddings = get_embeddings()
        retriever = build_vectorstore(chunks, embeddings)
        st.session_state.qa_chain = build_qa_chain(retriever)
        st.success("PDF loaded. Ask your question below.")
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

if st.session_state.qa_chain is not None:
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            if chat.get("is_unanswerable"):
                st.warning("⚠️ I could not find relevant information in the document to answer this question.")
            else:
                st.write(chat["answer"])
                with st.expander("📄 View Sources"):
                    for i, source in enumerate(chat["sources"]):
                        st.markdown(f"**Source {i+1} — Page {source['page']}**")
                        st.caption(source["content"])
                        st.divider()

    question = st.chat_input("Ask a question about your document...")

    if question:
        with st.spinner("Thinking..."):
            response = st.session_state.qa_chain.invoke({"query": question})

        answer = response["result"]
        source_documents = response["source_documents"]

        # Check if answer is irrelevant
        no_answer_phrase = "I could not find relevant information in the document"
        is_unanswerable = no_answer_phrase in answer

        sources = [
            {
                "page": doc.metadata.get("page", 0) + 1,
                "content": doc.page_content
            }
            for doc in source_documents
        ]

        st.session_state.chat_history.append({
            "question": question,
            "answer": answer,
            "sources": sources,
            "is_unanswerable": is_unanswerable
        })

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            if is_unanswerable:
                # Show clean warning instead of bad answer
                st.warning("⚠️ I could not find relevant information in the document to answer this question.")
            else:
                st.write(answer)
                with st.expander("📄 View Sources"):
                    for i, source in enumerate(sources):
                        st.markdown(f"**Source {i+1} — Page {source['page']}**")
                        st.caption(source["content"])
                        st.divider()