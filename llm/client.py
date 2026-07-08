import ollama


class LLMClient:
    def __init__(self, model="llama3.2:latest"):
        self.model = model

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            return f"Error: {e}"