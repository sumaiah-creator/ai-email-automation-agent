# ai_agent.py

import requests


# -----------------------------------
# OLLAMA API FUNCTION
# -----------------------------------

def ask_llama(prompt):

    """
    Sends prompt to local Llama3 model using Ollama
    """

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload
        )

        result = response.json()

        return result["response"]

    except Exception as e:

        return f"Ollama Error: {str(e)}"


# -----------------------------------
# EMAIL CLASSIFICATION
# -----------------------------------

def classify_email(content):

    prompt = f"""
    You are an AI email classification assistant.

    Classify the following email into ONLY ONE category.

    Categories:
    - Important
    - Spam
    - Meeting
    - Job
    - Personal

    Return ONLY the category name.

    Email:
    {content}
    """

    return ask_llama(prompt)


# -----------------------------------
# EMAIL SUMMARIZER
# -----------------------------------

def summarize_email(email):

    prompt = f"""
    Summarize this email in 2-3 lines.

    Email:
    {email}
    """

    return ask_llama(prompt)


# -----------------------------------
# EMAIL REPLY GENERATOR
# -----------------------------------

def generate_reply(email):

    prompt = f"""
    You are a professional AI email assistant.

    Write a polite and professional reply
    to the following email.

    Email:
    {email}
    """

    return ask_llama(prompt)


# -----------------------------------
# PRIORITY DETECTION
# -----------------------------------

def detect_priority(email):

    prompt = f"""
    Determine the priority level of this email.

    Return ONLY one:
    - High Priority
    - Medium Priority
    - Low Priority

    Email:
    {email}
    """

    return ask_llama(prompt)