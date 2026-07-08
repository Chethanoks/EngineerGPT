from llm.client import LLMClient

client = LLMClient()

def ask_ai(question):
    return client.generate(question)