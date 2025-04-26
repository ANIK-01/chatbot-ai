from flask import Flask, render_template, jsonify, request
from src.helper import create_retrieval_chain, create_stuff_documents_chain, load_dotenv, os,PineconeVectorStore
from store_index import index_name, embeddings
from src.prompt import *
from src.gemini_model import llm_model


app = Flask(__name__)
load_dotenv()
pinecone_api_key = os.getenv('PINECONE_API_KEY')   
google_api_key=os.getenv('GOOGLE_API_KEY')



docsearch= PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding=embeddings
)
retriever =docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
question_answer_chain = create_stuff_documents_chain(llm_model,prompt)

rag_chain= create_retrieval_chain(retriever,question_answer_chain)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET","POST"])

def chatbot():
    msg = request.form["msg"]
    input = msg
    print(input)

    response =rag_chain.invoke({"input": msg})

    print("Response: ",response["answer"])

    return str(response["answer"])

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5401, debug=True)