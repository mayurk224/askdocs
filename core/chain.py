from langchain_classic.chains import RetrievalQA
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME
from langchain_core.prompts import PromptTemplate

def build_qa_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME
    )

    # Strict prompt - forces model to only use document context
    prompt_template = """
    You are a helpful assistant that answers questions strictly based on the provided document context.

    Rules:
    - Only use information from the context below to answer
    - If the answer is not found in the context, respond exactly with: "I could not find relevant information in the document to answer this question."
    - Do not use your own knowledge or make up answers
    - Be concise and precise

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt} 
    )