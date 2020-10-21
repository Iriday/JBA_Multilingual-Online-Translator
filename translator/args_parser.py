from itertools import product
from argparse import ArgumentParser


def parse_args(args, languages):
    parser = ArgumentParser()
    parser.add_argument("from_lang")
    parser.add_argument("to_lang")
    parser.add_argument("text", help="word/text to translate")

    parsed_args = parser.parse_args(args)
    from_lang = parsed_args.from_lang.capitalize()
    to_lang = parsed_args.to_lang.capitalize()
    text = parsed_args.text

    if to_lang != "All":
        return [(from_lang, to_lang)], text
    return to_all_languages(from_lang, languages), text


def to_all_languages(from_lang, languages):
    from_to_langs = list(product([from_lang], languages))
    from_to_langs.remove((from_lang, from_lang))
    return from_to_langs
