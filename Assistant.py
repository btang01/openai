from openai import OpenAI
import os 
from assistant_utils import interact_with_movie_agent_assistant # import helper

# set up key
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_movie_agent_assistant():
    try:
        client = OpenAI()

        assistant = client.beta.assistants.create(
            name="Movie Agent Assistant",
            instructions="You are a movie expert. Use the provided functions to answer questions",
            tools=[{
                "type": "function",
                "function": {
                    "name": "get_latest_movies",
                    "description": "Get this year's movies",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the movie"
                            },
                            "month": {
                                "type": "string",
                                "description": "The month the movie was released"
                            }
                        }
                    }
                }
                }],
            model="gpt-4o-mini",
        )

        print("Movie Agent Assistant created successfully!")
        return assistant
    
    except Exception as e:
        print(f"Error creating assistant: {e}")
        return None 

# Main execution
if __name__ == "__main__": 
    assistant = create_movie_agent_assistant()
    if assistant:
        print(f"Assistant ID: {assistant['id']}")
    else:
        print("Failed to create assistant.")