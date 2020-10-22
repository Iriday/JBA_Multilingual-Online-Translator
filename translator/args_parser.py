from itertools import product
from argparse import ArgumentParser


def parse_args(args, languages):
    parser = ArgumentParser()
    parser.add_argument("from_lang", help=f"choose from: {', '.join(languages)}")
    parser.add_argument("to_lang", help=f"choose from: {', '.join(languages)}, or All")
    parser.add_argument("text", help="word/text to translate")
    parsed_args = parser.parse_args(args)

    from_lang = parsed_args.from_lang.capitalize()
    to_lang = parsed_args.to_lang.capitalize()
    text = parsed_args.text

    err_msg = __check_input(from_lang, to_lang, languages)
    if err_msg:
        print(err_msg)
        exit()

    if to_lang != "All":
        return [(from_lang, to_lang)], text
    return __to_all_languages(from_lang, languages), text


def __check_input(from_lang, to_lang, languages):
    if from_lang not in languages:
        return f"Sorry the program doesn't support {from_lang}"
    if to_lang not in languages and to_lang != "All":
        return f"Sorry the program doesn't support {to_lang}"
    if from_lang == to_lang:
        return f"Translation from {from_lang} to {to_lang} is not possible"
    return None


def __to_all_languages(from_lang, languages):
    from_to_langs = list(product([from_lang], languages))
    from_to_langs.remove((from_lang, from_lang))
    return from_to_langs
