def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents
    