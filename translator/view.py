from sys import stdout
from translator.args_parser import __to_all_languages
import os


def get_input(languages):
    __show_header(languages)
    return __get_mode(languages), __get_text()


def __show_header(languages):
    print("Hello, you're welcome to the translator. Translator supports:")
    for i, v in enumerate(languages):
        print(f"{i + 1}. {v}")


def __get_mode(languages):
    from_lang_index = int(input("Type the number of your language:\n")) - 1
    to_lang_index = int(
        input("Type the number of language you want to translate to, or '0' to translate to all languages:\n")) - 1
    if to_lang_index != -1:
        return [(languages[from_lang_index], languages[to_lang_index])]
    return __to_all_languages(languages[from_lang_index], languages)


def __get_text():
    return input("Type the word/text you want to translate:\n").strip()


def __show_translations(translations, to_lang, out=stdout):
    print(f"\n{to_lang} translations:", *translations, sep="\n", file=out)


def __show_examples(examples, to_lang, out=stdout):
    print(f"\n{to_lang} examples:", file=out)
    for i in range(0, len(examples), 2):
        print(f"{examples[i]}:", file=out)
        print(f"{examples[i + 1]}\n", file=out)


def show_results(translations, examples, from_to_lang):
    __show_translations(translations, from_to_lang[1])
    __show_examples(examples, from_to_lang[1])


def save_results_to_file(translations, examples, from_to_lang, file_path, append=True):
    if not append and os.access(file_path, os.X_OK):
        os.remove(file_path)
    with open(file_path, "a", encoding="utf-8") as out_file:
        __show_translations(translations, from_to_lang[1], out=out_file)
        __show_examples(examples, from_to_lang[1], out=out_file)
