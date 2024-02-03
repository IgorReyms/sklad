from docx2pdf import convert

def convert(path_input: str, path_output: str) -> bool:
    try:
        convert(path_input, path_output)
        return True
    except:
        return False