import os
import random
import google.generativeai as genai
import json

from click import prompt
from dotenv import load_dotenv
load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=
    """you are a language learning app agent. 
        you have to generate appropriate content depending on the prompt.
        you will only return in json format depending on the prompt details.
        these results will then be used in different functions as tools."""
)

vocabulary_list = []
def generate_general_vocabulary(language, level):
    chat_session = model.start_chat(history=[])

    # Format the prompt with the provided parameters
    prompt = f"""Generate a json object of 10 essential vocabulary words for a language learning app based on the user’s language and level.
        Language: {language}
        Level: {level}

        Each item should be a dictionary with the following fields:
        - "word": the vocabulary word in {language}
        - "meaning": a brief English translation
        - "icon": an emoji that relates to the word
        - "example": a sample sentence in {language} using the word

        Return a json object named 'vocabulary' consisting of items with this structure."""

    # Get response
    response = chat_session.send_message(prompt)

    api_output = response.text

    vocab_dict = json.loads(api_output)

    vocab_list = vocab_dict["vocabulary"]

    for item in vocab_list:
        vocabulary_list.append(item)

    return vocab_list

words = generate_general_vocabulary("german", "b2")
print(words)
print("-----------")

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
    
    Return a json object named 'vocabulary' consisting of items with this structure."""

    # Get response
    response = chat_session.send_message(prompt)

    api_output = response.text

    vocab_dict = json.loads(api_output)

    vocab_list = vocab_dict["vocabulary"]

    for item in vocab_list:
        vocabulary_list.append(item)

    return vocab_list


# Example usage
language = "German"
level = "B1"
interests = ["hiking", "painting", "books"]

vocabulary_list = generate_vocabulary(language, level, interests)
print(vocabulary_list)


# TOOL2 : TESTING VOCAB --> MULTIPLE CHOICE

def multiple_choice(vocab_list, num_choices=4):
    questions = []

    for item in vocab_list:
        # The correct answer
        correct_answer = item["meaning"]

        # Get other meanings to use as incorrect answers
        other_meanings = [v["meaning"] for v in vocab_list if v["meaning"] != correct_answer]

        # Randomly select incorrect answers
        if len(other_meanings) >= num_choices - 1:
            incorrect_answers = random.sample(other_meanings, num_choices - 1)
        else:
            # If not enough other meanings are available, repeat some to fill choices
            incorrect_answers = random.choices(other_meanings, k=num_choices - 1)

        # Combine correct answer with incorrect answers and shuffle
        answer_choices = incorrect_answers + [correct_answer]
        random.shuffle(answer_choices)

        # Create question structure
        question = {
            "word": item["word"],
            "question": f"What is the meaning of '{item['word']}'?",
            "choices": answer_choices,
            "correct_answer": correct_answer
        }

        questions.append(question)

    return questions


def fill_in_blanks(language, level,vocab_list=vocabulary_list):
    questions = []
    chat_session = model.start_chat(history=[])
    sentence_list = []

    for word in vocab_list:
        prompt = f"""
            Generate a fill-in-the-blank exercise in JSON format for the language learning app.
            The sentences should match the {level} level in {language}. Use the word '{word}' in context, leaving a blank in place of the words
            Ensure the exercise is simple and aligned with {level} proficiency.

            JSON format example:
            {{
                "sentence": "The quick brown ____ jumps over the lazy dog.",
                "correct_answer": "fox",
                "hint": "animal that is known for being clever"
            }}
            """
        # Get response
        response = chat_session.send_message(prompt)

        api_output = response.text

        sentence_dict = json.loads(api_output)
        sentence_list.append(sentence_dict)

    return sentence_list

fib = fill_in_blanks(language, level,vocab_list=vocabulary_list)
print(fib)
print("-------------")

"""vocabulary_list_test = multiple_choice(vocabulary_list)
print("-------------------------")
print(vocabulary_list_test[0])"""







