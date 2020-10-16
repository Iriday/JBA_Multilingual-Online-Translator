def get_mode():
    return input('Type "en" if you want to translate from French into English,'
                 ' or "fr" if you want to translate from English into French: ').strip()


def get_word():
    return input("Type the word you want to translate: ").strip()


def create_status_msg(mode, word):
    return f'You chose "{mode}" as the language to translate "{word}" to.'


def output_status(mode, word):
    print(create_status_msg(mode, word))
