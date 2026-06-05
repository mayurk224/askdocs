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

    # Memory stores conversation history
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    # Strict prompt
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