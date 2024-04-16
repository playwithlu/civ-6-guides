import json, os


OUTPUT_DIRECTORY = "KingdomRush"


def convert_to_markdown(json_input):
    # Parse the JSON data
    data = json.loads(json_input)

    # Extract the relevant information
    title = data.get("title", data.get("id", "No Title Provided"))
    text = (
        data.get("text", "No Text Provided")
        .replace('&lt;a href="', "[")
        .replace('"&gt;', "](")
        .replace("&lt;/a&gt;", ")")
    )

    # Define the Markdown output structure
    markdown_output = f"# {title}\n\n"
    markdown_output += text.replace("\nOverview.\n", "\n## Overview\n\n")

    return title, markdown_output


def format_file(file):
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    with open(file, "r") as f:
        for line in f.readlines():
            title, markdown = convert_to_markdown(line)
            path = os.path.join(OUTPUT_DIRECTORY, f"{title}.md")
            if not os.path.exists(path):
                with open(path, "w") as of:
                    of.write(markdown)


if __name__ == "__main__":
    files = ["KingdomRush00.jsonl", "KingdomRush01.jsonl"]
    for file in files:
        format_file(file)
