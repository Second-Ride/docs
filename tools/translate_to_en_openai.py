import openai
import os
from pathlib import Path

# OpenAI API key (ensure the key is in GitHub secrets)
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
        en_file = de_file.with_name(de_file.stem + ".en.md")
        if en_file.exists():
            continue  # Skip EN files that already exist
        with open(de_file, "r", encoding="utf-8") as f:
            de_text = f.read()
        en_text = translate_to_english(de_text)
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_text)
        print(f"Translated: {de_file} → {en_file}")

if __name__ == "__main__":
    main()
