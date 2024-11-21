def create_book():
    """Создает словарь для преобразования слов в числа и операции."""
    return {
        'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5',
        'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9',
        'десять': '10', 'одиннадцать': '11', 'двенадцать': '12',
        'тринадцать': '13', 'четырнадцать': '14', 'пятнадцать': '15',
        'шестнадцать': '16', 'семнадцать': '17', 'восемнадцать': '18',
        'девятнадцать': '19', 'двадцать': '20', 'тридцать': '30',
        'сорок': '40', 'пятьдесят': '50', 'шестьдесят': '60',
        'семьдесят': '70', 'восемьдесят': '80', 'девяносто': '90',
        'минус': '-', 'плюс': '+', 'умножить': '*',
        'на': '', 'открывается': '(', 'закрывается': ')',
        'скобка': '', 'сто': '100', 'ноль': '0'
    }


def translate_to_expression(words, book):
    """Переводит слова в математическое выражение."""
    result = ''
    for i, word in enumerate(words):
        if word in book:
            if book[word].isnumeric() and i > 0 and book[words[i - 1]].isnumeric():
                continue  # Пропускаем, если это число после другого числа
            result += book[word]
        else:
            return None  # Неверный ввод
    return result


def convert_result_to_words(result, invbook):
    """Преобразует числовой результат обратно в слова."""
    total = ''
    str_result = str(result)

    if result < 0:
        total += "минус "
        str_result = str_result[1:]

    if result == 0:
        total += invbook['0']
    elif 11 <= abs(result) <= 19:
        total += invbook[str_result]
    else:
        delit = 10 ** (len(str_result) - 1)
        for i in range(len(str_result)):
            current_digit = int(str_result[i])
            if current_digit > 0:
                total += invbook[str(current_digit * delit)] + " "
            delit //= 10

    return total.strip()


def calc(line):
    """Основная функция калькулятора."""
    book = create_book()
    invbook = {v: k for k, v in book.items()}

    if not line.strip():
        return "Попробуйте снова"

    words = line.split()
    expression = translate_to_expression(words, book)

    if expression is None:
        return "Неверный ввод"

    if expression.count('(') != expression.count(')'):
        return "Не то кол-во скобок"

    try:
        int_result = eval(expression)
    except Exception:
        return "Ошибка при вычислении"

    return convert_result_to_words(int_result, invbook)


print("Пожалуйста, введите строковое выражение для калькулятора.")
numeric = input()
print(calc(numeric))