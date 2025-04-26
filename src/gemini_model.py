from src.helper import os, load_dotenv, ChatGoogleGenerativeAI

load_dotenv()
google_api_key=os.getenv('GOOGLE_API_KEY')

llm_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=google_api_key,
    temperature=0.6,
    max_output_tokens=512
)