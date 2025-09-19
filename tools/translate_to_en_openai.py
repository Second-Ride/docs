from openai import OpenAI
import os
from pathlib import Path

# Create OpenAI client (will automatically use OPENAI_API_KEY from environment)
client = OpenAI()

docs_path = Path("docs")

def get_md_files():
    """Return all German markdown files to translate"""
    return [f for f in docs_path.rglob("*.md") if not f.name.endswith(".en.md")]

def translate_to_english(text: str) -> str:
    """Translate German text to English using OpenAI ChatCompletion API"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a translator from German to English."},
            {"role": "user", "content": text},
        ],
        temperature=0.3,
        max_tokens=2000
    )
    # Access the content of the first choice
    return response.choices[0].message.content.strip()

def main():
    for de_file in get_md_files():
        en_file = de_file.with_name(de_file.stem + ".en.md")
        if en_file.exists():
            continue  # Skip if English file already exists
        with open(de_file, "r", encoding="utf-8") as f:
            de_text = f.read()
        en_text = translate_to_english(de_text)
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_text)
        print(f"Translated: {de_file} → {en_file}")

if __name__ == "__main__":
    main()
