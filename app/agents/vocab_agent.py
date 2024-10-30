import os
import random
import google.generativeai as genai
import json
from dotenv import load_dotenv
load_dotenv()

# Configure API key and model once
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    system_instruction=
    """you are a language learning app agent. 
        you have to generate appropriate content depending on the prompt.
        you will only return in json format depending on the prompt details.
        these results will then be used in different functions as tools."""
)


# Function to generate vocabulary based on language, level, and interests
def generate_vocabulary(language, level, interests):
    chat_session = model.start_chat(history=[])

    # Format the prompt with the provided parameters
    prompt = f"""Generate a json object of 10 vocabulary words for a language learning app based on the user’s language, level, and interests.
    Language: {language}
    Level: {level}
    Interests: {interests}
    
    Each item should be a dictionary with the following fields:
    - "word": the vocabulary word in {language}
    - "meaning": a brief English translation
    - "icon": an emoji that relates to the word
    - "example": a sample sentence in {language} using the word
    
    Return a json object consisting of items with this structure."""

    # Get response
    response = chat_session.send_message(prompt)

    api_output = response.text

    vocab_dict = json.loads(api_output)

    vocab_list = vocab_dict["vocabulary"]

    return vocab_list


# Example usage
language = "German"
level = "B1"
interests = ["hiking", "painting", "books"]

vocabulary_list = generate_vocabulary(language, level, interests)
print(vocabulary_list[0])







