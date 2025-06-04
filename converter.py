def convert_number(number: str, from_base: int) -> dict:
    """
    Конвертирует число из указанной системы в другие (2, 8, 10, 16).
    Возвращает словарь с результатами или None при ошибке.
    """
    try:
        decimal = int(number, from_base)  
        return {
            "binary": bin(decimal)[2:],       
            "octal": oct(decimal)[2:],      
            "decimal": decimal,
            "hexadecimal": hex(decimal)[2:].upper()  
        }
    except (ValueError, TypeError):
        return None

def main():
    print("=== Конвертер систем счисления ===")
    print("Доступные системы: 2 (двоичная), 8 (восьмеричная), 10 (десятичная), 16 (шестнадцатеричная)\n")
    
    number = input("Введите число: ").strip()
    from_base = int(input("Исходная система счисления (2/8/10/16): "))
    
    result = convert_number(number, from_base)
    
    if result:
        print("\nРезультат:")
        for system, value in result.items():
            print(f"{system.capitalize()}: {value}")
    else:
        print("Ошибка: некорректный ввод!")

if __name__ == "__main__":
    main()