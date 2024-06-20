import os
import json
from datetime import datetime
from gpt4connect import ask_gpt4
from googledrive import iterate_files_in_folder, get_file_content, get_default_folder_id, get_service

def classify_file(file_content):
    """
    Classifies notes based on the file content. It uses a list of classes derived from a sample (or all at first) of the notes.

    Args:
        file_content (str): The content of the file.

    Returns:
        A single class for the note.
    """
    return "class"
    # # Use GPT-4 to generate follow-up questions
    # system_prompt = """You are an expert at analyzing the content and structure of 
    #     files. Can you generate a list of follow-up questions based on the following file content? Each question should be on a separate line and start with a dash (-).
    #     The file content is:
    #     """
    # user_prompt = file_content
    # response = ask_gpt4(user_prompt, system_prompt)

    # # Parse the response and extract the follow-up questions
    # questions = []
    # for line in response.splitlines():
    #     if line.startswith("- "):
    #         questions.append(line[2:])

    # if questions == [] :
    #     return None
    # else: 
    #     return questions


def get_file_timestamp(file_id):
    """Get the timestamp of a file in Google Drive."""
    file_metadata = get_service().files().get(fileId=file_id, fields='modifiedTime').execute()
    modified_time = file_metadata['modifiedTime']
    return datetime.strptime(modified_time, '%Y-%m-%dT%H:%M:%S.%fZ')

def is_newer_than_json(file_id, json_file_path):
    """Check if the note file is newer than the local JSON file."""
    file_timestamp = get_file_timestamp(file_id)
    json_file_timestamp = datetime.fromtimestamp(os.path.getmtime(json_file_path))
    return file_timestamp > json_file_timestamp

def save_to_json(file_content, file_name, file_timestamp, json_file_path, indent=4):
    """Save the note contents to a local JSON file."""
    with open(json_file_path, 'a') as json_file:
        json.dump({'timestamp': file_timestamp.isoformat(), 'filename': file_name, 'content': file_content}, json_file, indent=indent)

import os
import json

def build_class_list():
    """
    Builds a class list by iterating through files in a folder and saving relevant information to a JSON file.

    Args:
        None

    Returns:
        None
    """
    json_file_path = 'ignore/notes.json'
    folder_id = get_default_folder_id()
    count = 0

    # Create the JSON file if it doesn't exist
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump({}, json_file,indent=4)


    # Iterate through files in the folder
    for file in iterate_files_in_folder(folder_id):
        # Check if the file is newer than the JSON file or in test mode
        if is_newer_than_json(file['id'], json_file_path) or test_mode == True:
            count += 1
            file_content = get_file_content(file['id'])
            file_timestamp = get_file_timestamp(file['id'])
            print(f"{count} saving to json {file_timestamp}")
            save_to_json(file_content, file['name'], file_timestamp, json_file_path)


if __name__ == "__main__":
    test_mode = True
    build_class_list()