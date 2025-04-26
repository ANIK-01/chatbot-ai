from src import helper
def download_hugging_face_embeddings():
    embeddings=helper.HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-V2')
    return embeddings