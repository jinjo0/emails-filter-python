import os
import re

def extract_emails(input_text):
    # Regular expression to extract email addresses
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(input_text)
    return emails

def process_file(input_path, output_file):
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        content = input_file.read()
        emails = extract_emails(content)

    with open(output_file, 'a') as output:
        for email in emails:
            output.write(f"{email}\n")

if __name__ == "__main__":
    input_folder = os.path.abspath(os.path.dirname(__file__))  # Current folder where the script is located
    output_file = "all_emails.txt"

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, output_file)
