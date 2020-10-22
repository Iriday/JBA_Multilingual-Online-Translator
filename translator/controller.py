from requests.exceptions import ConnectionError


def run(view, model, args=None):
    mode, text = args if args else view.get_input(model.LANGUAGES)

    for i, from_to_lang in enumerate(mode):
        try:
            response = model.get_page(from_to_lang[0], from_to_lang[1], text)
        except ConnectionError:
            view.connection_error()
            exit()
        else:
            if not response:
                view.no_results_error(text)
                exit()
            else:
                translations = model.get_translations(response.content)
                examples = model.get_examples(response.content)
                view.show_results(translations, examples, from_to_lang)
                view.save_results_to_file(translations, examples, from_to_lang, f"{text[:80]}.txt", append=bool(i))
