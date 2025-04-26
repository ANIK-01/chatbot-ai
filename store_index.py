from src.helper import os, Pinecone, ServerlessSpec, PineconeVectorStore, load_dotenv
from src.document_loader import text_split, load_pdf_file
from src.embedding import download_hugging_face_embeddings

extracted_data = load_pdf_file(data="data/")
text_chunks=text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "chatbot-ai"
embedding_dimension = 384  # Matches all-MiniLM-L6-v2

# Check if index exists, create if it doesn't
if index_name not in pc.list_indexes().names():
    print("index creating")
    pc.create_index(
        name=index_name,
        dimension=embedding_dimension,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
else:
    print("index exist")

index_store_chunks = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)