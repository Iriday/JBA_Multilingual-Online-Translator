import requests as rq
from bs4 import BeautifulSoup


def get_page(languages, text) -> rq.Response:
    return rq.get(f"https://context.reverso.net/translation/{languages}/{text}",
                  headers={"user-agent": "Anonymous/999 Give me the content! please)"})


def get_translations(content):
    tags = BeautifulSoup(content, "html.parser").find(attrs={"id": "translations-content"}).findAll(attrs={"class": "translation"})
    return [word for word in (tag.text.strip() for tag in tags) if word]
