from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

def main():
    print("Hello from agentic-rag!")


if __name__ == "__main__":
    main()
    print(app.invoke(input={"question": "what is agent memory?"}))
