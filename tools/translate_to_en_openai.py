import openai
import os
from pathlib import Path

# Create OpenAI client using the API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = openai.OpenAI(api_key=api_key)

docs_path = Path("docs")

def get_md_files():
    """Return all German markdown files to translate (excluding existing English files)"""
    return [f for f in docs_path.rglob("*.md") if not f.name.endswith(".en.md")]

def translate_to_english(text):
    """Translate German text to English using OpenAI ChatCompletion API"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a translator from German to English."},
                {"role": "user", "content": text},
            ],
            temperature=0.3,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Translation failed: {e}")
        return None

def main():
    files = get_md_files()
    if not files:
        print("No German Markdown files found to translate.")
        return

    for de_file in files:
        en_file = de_file.with_name(de_file.stem + ".en.md")
        if en_file.exists():
            print(f"Skipping {en_file} (already exists)")
            continue

        with open(de_file, "r", encoding="utf-8") as f:
            de_text = f.read().strip()

        en_text = translate_to_english(de_text)
        if not en_text:
            print(f"Skipping {de_file} due to translation error")
            continue

        with open(en_file, "w", encoding="utf-8") as f:
            f.write(en_text)

        print(f"Translated: {de_file} → {en_file}")

if __name__ == "__main__":
    main()
