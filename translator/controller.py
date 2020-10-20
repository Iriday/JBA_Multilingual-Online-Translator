def run(view, model):
    mode, text = view.get_mode(model.supported_languages), view.get_text()
    for from_to_lang in mode:
        response = model.get_page(from_to_lang[0], from_to_lang[1], text)
        translations = model.get_translations(response.content)
        examples = model.get_examples(response.content)
        view.show_results(translations, examples, from_to_lang)
