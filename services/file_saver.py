class FileSaver:
    @staticmethod
    def save_to_file(word_frequencies, filename="results.txt"):
        try:
            with open(filename, "w") as file:
                for word, freq in word_frequencies:
                    file.write(f"{word}: {freq}\n")
        except Exception as e:
            print(f"An error occurred while saving the file: {str(e)}")
