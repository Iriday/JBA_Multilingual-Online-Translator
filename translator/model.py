import requests as rq
from bs4 import BeautifulSoup

LANGUAGES = ("Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese",
             "Romanian", "Russian", "Turkish")


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
