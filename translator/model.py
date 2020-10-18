import requests as rq
from bs4 import BeautifulSoup


def get_page(languages, text) -> rq.Response:
    return rq.get(f"https://context.reverso.net/translation/{f'{languages[0].lower()}-{languages[1].lower()}'}/{text}",
                  headers={"user-agent": "Anonymous/999 Give me the content! please)"})


def get_translations(content):
    return get_text(content, "translations-content", "translation")


def get_examples(content):
    return get_text(content, "examples-content", "ltr")


def get_text(content, container_id, text_class):
    tags = BeautifulSoup(content, "html.parser").find(attrs={"id": container_id}).findAll(attrs={"class": text_class})
    return [text for text in (tag.text.strip() for tag in tags) if text]
