def get_mode():
    mode = input('Type "en" if you want to translate from French into English,'
                 ' or "fr" if you want to translate from English into French: ').strip()
    return ("english", "french") if mode == "fr" else ("french", "english")  # temp


def get_text():
    return input("Type the word/text you want to translate: ").strip()


def show_header(language, text, response):
    print(f'You chose "{language}" as the language to translate "{text}" to.')
    print(f'{response.status_code} {"OK" if response.ok else "ERROR"}')


def show_translations(translations, language):
    print(f"\n{language} translations:", *translations, sep="\n")


def show_examples(examples, language):
    print(f"\n{language} examples:")
    for i in range(0, len(examples), 2):
        print(f"{examples[i]}:")
        print(f"{examples[i + 1]}\n")


def show_results(translations, examples, mode, text, response):
    language = mode[1].capitalize()
    show_header(language, text, response)
    print("\nContent examples:")
    show_translations(translations, language)
    show_examples(examples, language)
