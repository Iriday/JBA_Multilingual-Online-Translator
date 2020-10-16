def get_mode():
    return input('Type "en" if you want to translate from French into English,'
                 ' or "fr" if you want to translate from English into French: ').strip()


def get_word():
    return input("Type the word you want to translate: ").strip()


def show_header(mode, word, response):
    print(f'You chose "{mode}" as the language to translate "{word}" to.\n' +
          f'{response.status_code} {"OK" if response.ok else "ERROR"}')


def show_translations(translations):
    print("Translations", translations, sep="\n")
