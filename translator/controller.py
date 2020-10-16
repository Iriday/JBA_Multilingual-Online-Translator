from translator.view import output_status, get_mode, get_word


def run():
    output_status(get_mode(), get_word())
