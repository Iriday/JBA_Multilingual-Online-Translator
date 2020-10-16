def run(view, model):
    mode, word = view.get_mode(), view.get_word()
    response = model.get_page("english-french" if mode == "fr" else "french-english", word)

    view.show_header(mode, word, response)
    view.show_translations(model.get_translations(response.content))
