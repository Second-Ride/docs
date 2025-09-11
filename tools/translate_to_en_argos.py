import openai
import os
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

docs_path = Path("docs")

def get_md_files():
    """Returns all markdown files in DE to be translated to EN"""
    return [f for f in docs_path.rglob("*.md") if not f.name.endswith(".en.md")]

def translate_to_english(text):
    """Translates the text from German to English using the OpenAI API"""
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Translate the following German text to English:\n\n{text}",
        temperature=0.3,  # the lower the temperature, the more precise the translation will be
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def main():
    for de_file in get_md_files():
        en_file = de_file.with_name(de_
