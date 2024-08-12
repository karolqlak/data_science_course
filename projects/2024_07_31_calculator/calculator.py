class Calculator:
    def __init__(self):
        self.menu_string = '''
        Menu:
        1. Dodaj
        2. Odejmij
        3. Pomnóż
        4. Podziel
        5. Wyjdź'''

    def print_menu(self):
        print(self.menu_string)

    def calculate(self, option, number1, number2):
        match option:
            case 1:
                return number1 + number2
            case 2:
                return number1 - number2
            case 3:
                return number1 * number2
            case 4:
                if number2 == 0:
                    print("Nie dzielimy przez 0")
                else:
                    return number1 / number2

    def run(self):
        while True:
            self.print_menu()
            option = int(input("Wybierz opcję:"))
            if option == 5:
                break
            else:
                if option not in (1, 2, 3, 4):
                    print("Nie rozpoznano opcji. Wybierz jedną z poniższych")
                else:
                    number1 = int(input("Podaj Liczbę 1:"))
                    number2 = int(input("Podaj Liczbę 2:"))
                    result = self.calculate(option, number1, number2)
                    if result is not None:
                        print(f"Twój wynik to: {result}")
        print("Koniec programu")


cal = Calculator()
cal.run()
