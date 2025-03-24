def sum_strings(x, y):
    # Удаляем ведущие пробелы и нули
    x = x.lstrip('0').strip()
    y = y.lstrip('0').strip()

    # Если строки пустые, заменяем на '0'
    x = x if x else '0'
    y = y if y else '0'

    # Если одна из строк не состоит из цифр, считаем её нулём
    if not x.isdigit() or not y.isdigit():
        return '0' if not x.isdigit() and not y.isdigit() else (x if y == '0' else y)

    # Инвертируем строки для удобства обработки (начинаем с младших разрядов)
    x_rev = x[::-1]
    y_rev = y[::-1]

    max_len = max(len(x_rev), len(y_rev))
    carry = 0  # Перенос в следующий разряд
    result = []

    for i in range(max_len):
        # Получаем текущие цифры (или 0, если разряд отсутствует)
        digit_x = int(x_rev[i]) if i < len(x_rev) else 0
        digit_y = int(y_rev[i]) if i < len(y_rev) else 0

        # Суммируем цифры и перенос
        total = digit_x + digit_y + carry
        carry = total // 10  # Новый перенос
        result.append(str(total % 10))  # Текущая цифра результата

    # Если остался перенос, добавляем его
    if carry > 0:
        result.append(str(carry))

    # Разворачиваем результат обратно и убираем ведущие нули
    result_str = ''.join(reversed(result)).lstrip('0')

    return result_str if result_str else '0'  # На случай, если результат "0...0"


print(sum_strings('10000000000000000000763634643664364367674367436734676743673467346346736746734763467346734673467459834985734985735983745934759347534879543000000000000000', '1000000000000000000000000000000000000000000000'))