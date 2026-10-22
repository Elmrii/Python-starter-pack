def count_words(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return len(text.split())

def count_chars(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return len(text)
filename = "essay.txt"
print("Word count:", count_words(filename))
print("Character count", count_chars(filename))
