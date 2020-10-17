def run(view, model):
    mode, text = view.get_mode(), view.get_text()
    response = model.get_page(mode, text)
    translations = model.get_translations(response.content)
    examples = model.get_examples(response.content)

    view.show_results(translations, examples, mode, text, response)
