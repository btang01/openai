from openai import OpenAI
import os 

# set up key
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_assistant():
    try:
        client = openai.client()

        assistant = client.beta.assistants.create(
            name="Math Tutor",
            instructions="You are a personal math tutor. Write and run code to answer math questions.",
            tools=[{"type": "code_interpreter"}],
            model="gpt-4o",
        )

        print("Assistant created successfully!")
        return assistant
    
    except Exception as e:
        print(f"Error creating assistant: {e}")
        return None 

# check if script being run directly (as main) rather than imported as module into another script
# makes sure it only runs on import if create_assistant is called
if __name__ == "__main__": #if run directly, name is main
    assistant = create_assistant()
    if assistant:
        print(f"Assistant ID: {assistant['id']}")
    else:
        print("Failed to create assistant.")