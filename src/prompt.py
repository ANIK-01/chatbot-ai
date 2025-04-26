from src import helper
system_prompt = (
    "You are a helpful and concise assistant. "
    "Answer questions using only the information provided in the context below. "
    "If the answer is not in the context, respond with 'I don't know based on the provided information.' "
    "Keep your answers under three sentences.\n\n"
    "{context}"
)

prompt = helper.ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)