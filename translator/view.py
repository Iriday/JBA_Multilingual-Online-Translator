__languages = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French", 6: "Hebrew", 7: "Japanese",
               8: "Dutch", 9: "Polish", 10: "Portuguese", 11: "Romanian", 12: "Russian", 13: "Turkish"}


def get_mode():
    show_header()
    from_lan = __languages[int(input("Type the number of your language:\n"))]
    to_lan = __languages[int(input("Type the number of language you want to translate to:\n"))]
    return from_lan, to_lan


def get_text():
    return input("Type the word/text you want to translate:\n").strip()


def show_header():
    print("Hello, you're welcome to the translator. Translator supports:")
    for k, v in __languages.items():
        print(f"{k}. {v}")


def show_translations(translations, language):
    print(f"\n{language} translations:", *translations, sep="\n")


def show_examples(examples, language):
    print(f"\n{language} examples:")
    for i in range(0, len(examples), 2):
        print(f"{examples[i]}:")
        print(f"{examples[i + 1]}\n")


def show_results(translations, examples, mode):
    show_translations(translations, mode[1])
    show_examples(examples, mode[1])
