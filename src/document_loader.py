from src import helper
def load_pdf_file(data):
    loader =helper.DirectoryLoader(data,
                            glob="*.pdf",
                            loader_cls=helper.PyPDFLoader
                            )
    
    documents=loader.load()
    return documents


def text_split(extracted_data):
    text_splitter=helper.RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks