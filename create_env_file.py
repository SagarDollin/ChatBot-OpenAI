# create_env_file.py
import sys

def create_env_file(api_key):
    env_content = f"OPENAI_API_KEY={api_key}\nserver_on_message=\"Welcome to the ChatBot server developed by Sagar Dollin. Refer to readme.md file on how to access the chat app using POSTMAN\""

    with open(".env", "w") as env_file:
        env_file.write(env_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_env_file.py <OPENAI_API_KEY>")
        sys.exit(1)

    input_api_key = sys.argv[1]
    create_env_file(input_api_key)
    print(".env file created successfully.")
