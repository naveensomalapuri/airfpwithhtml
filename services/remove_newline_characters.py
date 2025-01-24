def removenewlinecharacters(pattern):
        # Replace single and double newline characters with an empty string
    cleaned_pattern = ""
    i = 0
    
    while i < len(pattern):
        # Check for single newline
        if pattern[i] == '\n':
            # Skip the character
            i += 1
            # Check for the next character to see if it's also a newline
            if i < len(pattern) and pattern[i] == '\n':
                # Skip the second newline as well
                i += 1
        else:
            # If it's not a newline, add it to the cleaned string
            cleaned_pattern += pattern[i]
            i += 1
    print("removed newline characters")
    print(cleaned_pattern)
    return cleaned_pattern