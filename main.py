import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=ai_contents_input()
    )
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

def ai_contents_input():
    if len(sys.argv) != 2:
        print("Usage: uv run main.py <input_contents_here_in_quotes"">")
        sys.exit(1)
    else:
        return sys.argv[1]

if __name__ == "__main__":
    main()

