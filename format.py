import json, os


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


def format_file(file, output_directory):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    with open(file, "r") as f:
        for line in f.readlines():
            title, markdown = convert_to_markdown(line)
            path = os.path.join(output_directory, f"{title}.md")
            if not os.path.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as of:
                    of.write(markdown)


if __name__ == "__main__":
    import sys

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for file in os.listdir(input_dir):
        path = os.path.join(input_dir, file)
        format_file(path, output_dir)
