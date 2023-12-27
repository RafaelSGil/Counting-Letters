def read_file(file_path, start_line, end_line, file_encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=file_encoding) as file:
            lines = file.readlines()
            start_index = start_line - 1
            end_index = min(end_line, len(lines))

            if start_index >= len(lines) or start_index >= end_index:
                return "Invalid line numbers"

            lines_to_return = lines[start_index:end_index]

        return ''.join(lines_to_return)

    except FileNotFoundError:
        return "File not found"
    except UnicodeDecodeError:
        return f"Unable to decode using {file_encoding} encoding"
    
def format_text(input_string, allowed_characters):
    formatted_string = ''.join(char for char in input_string if char in allowed_characters)
    return formatted_string
