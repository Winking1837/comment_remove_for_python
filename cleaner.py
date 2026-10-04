import tokenize
import io
import sys

def remove_comments(source: str) -> str:
    tokens = tokenize.tokenize(
        io.BytesIO(source.encode("utf-8")).readline
    )

    cleaned_tokens = []

    for token in tokens:
        if token.type == tokenize.COMMENT:
            continue
        cleaned_tokens.append(token)
    return tokenize.untokenize(cleaned_tokens).decode("utf-8")

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a file to analyze.")
        sys.exit(1)
    target_file = sys.argv[1]
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            source = f.read()
        cleaned_source = remove_comments(source)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(cleaned_source)
        print(f"Comments removed from '{target_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{target_file}' was not found.")

if __name__ == "__main__":
    main()
