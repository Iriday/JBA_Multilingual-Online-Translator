from itertools import product


def get_mode(languages):
    show_header(languages)
    from_lang_index = int(input("Type the number of your language:\n"))
    to_lang_index = int(input("Type the number of language you want to translate to, or '0' to translate to all languages:\n"))
    if to_lang_index != 0:
        return [(languages[from_lang_index], languages[to_lang_index])]
    modes = list(product([(languages[from_lang_index])], languages.values()))
    modes.remove((languages[from_lang_index], languages[from_lang_index]))
    return modes


def get_text():
    return input("Type the word/text you want to translate:\n").strip()


def show_header(languages):
    print("Hello, you're welcome to the translator. Translator supports:")
    for k, v in languages.items():
        print(f"{k}. {v}")


def show_translations(translations, to_lang):
    print(f"\n{to_lang} translations:", *translations, sep="\n")


def show_examples(examples, to_lang):
    print(f"\n{to_lang} examples:")
    for i in range(0, len(examples), 2):
        print(f"{examples[i]}:")
        print(f"{examples[i + 1]}\n")


def show_results(translations, examples, mode):
    show_translations(translations, mode[1])
    show_examples(examples, mode[1])
