from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_chunk_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)

# New function added
def get_summary_text(chunks, max_chunks=20):
    # Take first 20 chunks — enough to summarize without hitting token limit
    selected = chunks[:max_chunks]
    combined_text = "\n\n".join([chunk.page_content for chunk in selected])
    return combined_text