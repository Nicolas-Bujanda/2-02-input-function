import datetime

def calculate_birth_year(current_year, age, had_birthday):
    if had_birthday:
        birth_year = current_year - age
    else:
        birth_year = current_year - age - 1
    return birth_year

def main():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    had_birthday_str = input("Did you already have your birthday this year? (yes/no) ").lower()
    had_birthday = had_birthday_str == "yes"

    current_year = datetime.datetime.now().year
    birth_year = calculate_birth_year(current_year, age, had_birthday)

    print(f"{name}, you were born in the year {birth_year}.")

if __name__ == "__main__":
    main()

main()