import openai
import os
from pathlib import Path

# OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to the markdown documentation
docs_path = Path("docs")

def get_md_files():
    """Return all German markdown files that need to be translated to English"""
    return [f for f in docs_path.rglob("*.md") if not f.name.endswith(".en.md")]

def translate_to_english(text):
    """Translate German text to English using OpenAI API"""
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Translate the following German text to English:\n\n{text}",
        temperature=0.3,  # Lower temperature = more accurate translation
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def main():
    # Iterate over all German markdown files
    for de_file in get_md_files():
        # Determine the English file path
        en_file = de_file.with_name(de_file.stem + ".en.md")
        if en_file.exists():
            continue  # Skip if English file already exists

        # Read the German file
        with open(de_file, "r", encoding="utf-8") as f:
            de_text = f.read()

        # Translate the content
        en_text = translate_to_english(de_text)

        # Write the translated text to the new English file
        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_text)

        print(f"Translated: {de_file} → {en_file}")

if __name__ == "__main__":
    main()
