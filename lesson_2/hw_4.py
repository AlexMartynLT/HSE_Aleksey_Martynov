def is_valid_inn(inn_str):
    """Функция валидации ИНН. Возвращает True, если ИНН корректен, иначе False."""
    if not inn_str.isdigit():
        return False
    length = len(inn_str)
    if length not in (10, 12):
        return False

    if length == 10:
        return _validate_company_inn(inn_str)
    else:
        return _validate_individual_inn(inn_str)

def _validate_company_inn(inn_str):
    """Валидация ИНН организации (10 цифр)."""
    coefficients = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    part = inn_str[:9]
    total = sum(int(digit)*coeff for digit, coeff in zip(part, coefficients))
    control = total % 11
    if control > 9:
        control %= 10
    return control == int(inn_str[9])

def _validate_individual_inn(inn_str):
    """Валидация ИНН физического лица/ИП (12 цифр)."""
    coeffs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    part1 = inn_str[:10]
    total1 = sum(int(d)*c for d,c in zip(part1, coeffs1))
    control1 = total1 % 11
    if control1 >9:
        control1 %=10
    if control1 != int(inn_str[10]):
        return False

    coeffs2 = [3,7,2,4,10,3,5,9,4,6,8]
    part2 = inn_str[:11]
    total2 = sum(int(d)*c for d,c in zip(part2, coeffs2))
    control2 = total2 %11
    if control2 >9:
        control2 %=10
    return control2 == int(inn_str[11])

if __name__ == "__main__":
    # Точка входа программы: запрос ИНН у пользователя [[7]]
    inn = input("Введите ИНН для проверки: ")
    # Проверка и вывод результата
    if is_valid_inn(inn):
        print("ИНН валиден ✅")
    else:
        print("ИНН НЕ валиден ❌")
