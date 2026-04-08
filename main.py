from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.1:8b")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate(template)
chain = prompt | model

while True:
    print("\n\n-----------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n-----------------------------")
    if question == "q":
        break

    result = chain.invoke({"reviews": [], "question": question})
    print(result)