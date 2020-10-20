import requests as rq
from bs4 import BeautifulSoup

supported_languages = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French", 6: "Hebrew", 7: "Japanese",
                       8: "Dutch", 9: "Polish", 10: "Portuguese", 11: "Romanian", 12: "Russian", 13: "Turkish"}


def get_page(from_lang, to_lang, text) -> rq.Response:
    return rq.get(f"https://context.reverso.net/translation/{f'{from_lang.lower()}-{to_lang.lower()}'}/{text}",
                  headers={"user-agent": "Anonymous/999 Give me the content! please)"})


def get_translations(content):
    return get_text(content, "#translations-content .translation")


def get_examples(content):
    return get_text(content, "#examples-content .text")


def get_text(content, selector):
    tags = BeautifulSoup(content, "html.parser").select(selector)
    return [text for text in (tag.text.strip() for tag in tags) if text]
