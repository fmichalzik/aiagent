import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    args = sys.argv

    if len(args) == 1 or len(args) > 3:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = sys.argv[1] # sys.argv variable is a list of strings representing all the command line arguments passed to the script


    # load the environment variables from the .env file using the dotenv library 
    # so we can read the API key
    api_key = os.environ.get("GEMINI_API_KEY")

    # use the API key to create a new instance of a Gemini client
    client = genai.Client(api_key=api_key)

    # in order to keep track of the conversation with the LLM (types.Content) we need a list
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # get a response (for 'contents') from the gemini-2.0-flash-001 model
    # generate_content method returns a GenerateContentResponse object
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    
    # the response has a .usage_metadata property that holds token informations
    # you can think of tokens as the currency of LLMs 
    # they are the way that LLMs measure how much text they have to process.
    prompt_tokens = getattr(response.usage_metadata, 'prompt_token_count', 0)
    response_tokens = getattr(response.usage_metadata, 'candidates_token_count', 0)

    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print("")    
    print("Response:")
    # the .text property holds the model's answer.
    print(response.text)
    
if __name__ == "__main__":
    main()