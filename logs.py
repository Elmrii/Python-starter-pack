def log(path, severity, text):
    file = open(path, "a")
    file.write(f"{severity}: {text}\n")
    file.close()
