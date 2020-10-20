from sys import stdout
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


def show_translations(translations, to_lang, out=stdout):
    print(f"\n{to_lang} translations:", *translations, sep="\n", file=out)


def show_examples(examples, to_lang, out=stdout):
    print(f"\n{to_lang} examples:", file=out)
    for i in range(0, len(examples), 2):
        print(f"{examples[i]}:", file=out)
        print(f"{examples[i + 1]}\n", file=out)


def show_results(translations, examples, mode):
    show_translations(translations, mode[1])
    show_examples(examples, mode[1])


def save_results_to_file(translations, examples, from_to_lang, file_path, append=True):
    if not append:  # clear file
        with open(file_path, "w", encoding="utf-8"):
            pass
    with open(file_path, "a", encoding="utf-8") as out_file:
        show_translations(translations, from_to_lang[1], out=out_file)
        show_examples(examples, from_to_lang[1], out=out_file)
