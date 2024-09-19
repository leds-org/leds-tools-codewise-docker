from openai import OpenAI
import requests
import os
import sys
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint

def suggest_improvements(code: str, language: str) -> str:

    prompt = f"Review the following {language} code and suggest improvements until 150 characteris with markdown :\n\n{code}"
    
    openai_engine = os.getenv("OPENAI_ENGINE")
    
    client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY"), )

    response = client.chat.completions.create(messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ], model=openai_engine,
    )
    message:str = ""
    for choice in response.choices:
        message += "{0} \n".format(choice.message.content)
    
    return message

def main ():
    discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    code_file_path = sys.argv[1]
    language = sys.argv[2]

    with open(code_file_path, 'r') as file:
        code_snippet = file.read()
    
    suggestions = suggest_improvements(code_snippet,language)
    
    pprint (suggestions)

    discord_message = {
        'content': f"Code Review Suggestions:\n```{language}\n{suggestions}```"
    }

    discord_response = requests.post(discord_webhook_url, json=discord_message)
    
    if discord_response.status_code == 204:
        print('Message sent to Discord successfully.')
    else:
        print(f'Failed to send message to Discord. Status code: {discord_response.status_code}')

if __name__ == "__main__":
    main()