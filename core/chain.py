from langchain_classic.chains import RetrievalQA, ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME
from langchain_core.prompts import PromptTemplate

def build_qa_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    prompt_template = """
    You are a helpful assistant that answers questions strictly based on the provided document context and conversation history.

    Rules:
    - Only use information from the context below to answer
    - Use the conversation history to understand follow-up questions
    - If the answer is not in the context, respond exactly with: "I could not find relevant information in the document to answer this question."
    - Do not use your own knowledge or make up answers
    - Be concise and precise

    Context:
    {context}

    Conversation History:
    {chat_history}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "chat_history", "question"]
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

# New function added
def summarize_document(text):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME
    )

    summary_prompt = f"""
    You are a document summarization assistant.

    Based on the following document content, provide a structured summary that includes:
    - What this document is about (1-2 sentences)
    - Main topics covered (bullet points)
    - Key takeaways (bullet points)
    - Who this document is useful for (1 sentence)

    Document Content:
    {text}

    Summary:
    """

    response = llm.invoke(summary_prompt)
    return response.content