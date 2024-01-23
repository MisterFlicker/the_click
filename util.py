"""Модуль содержит две вспомогательные функции для """


def change_stop_button(input: str):
    new_file = open('stop_button.txt', "w")
    new_file.write(input.upper())
    new_file.close()
    return


def change_m_button(button: str):
    new_file = open('mouse_button.txt', "w")
    new_file.write(button)
    new_file.close()
    return


def valid(input: str) -> bool:
    """Функция проверяет валидность изменения символа остановки записи и воспроизведения кликов

    Функция возвращает True если, длина input не должна равнятся 1 и не входить в число спец-символов banned_symbols.
    В противном случае функция возвращает False.

    Parameters
    ----------
    input: str
        введенный пользователем текст
    """

    banned_symbols = ('!', '@', '#', '$', '%', '^', '&', '*',
                      '(', ')', '-', '+', '=', '"', "'", '№',
                      ';', ':', '?', '`', '~')
    if len(input) != 1 or input in banned_symbols:
        return False
    else:
        return True
