def lasi_tekstu(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Fails '{filename}' nav atrasts.")
    except Exception as e:
        print(f"Ir atrasta kļūda: {e}")

# Example usage:
lasi_tekstu("izlasit.txt")
