import re
import json

def extractjson(content):
    content = str(content)
    
    # Define the pattern to match the content between "Start JSON" and "End JSON"
    pattern = r"Start JSON (.*?) End JSON"
    
    # Use re.DOTALL to ensure the dot matches newlines
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        json_string = match.group(1)
        
        # Remove any unwanted newline escape characters
        json_string = json_string.replace("\\n", " ")
        
        # Remove leading and trailing whitespace
        json_string = json_string.strip()
        
        # Convert the JSON string to a Python dictionary
        try:
            json_data = json.loads(json_string)
            return json_data
        except json.JSONDecodeError:
            return "Invalid JSON format."
    else:
        return "No JSON content found."

