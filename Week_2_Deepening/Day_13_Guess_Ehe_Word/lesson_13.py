# Игра "Угадай слово" - упрощённая версия

import random

# Список загаданных слов
words = ["python", "программирование", "компьютер", "алгоритм"]

def display_word(word, guessed_letters):
    """Отображает текущее состояние слова с открытыми буквами"""
    return ''.join(letter if letter in guessed_letters else '*' for letter in word)

def check_letter(letter, word, guessed_letters):
    """Проверяет, есть ли буква в слове и обновляет список угаданных букв"""
    if letter in word and letter not in guessed_letters:
        guessed_letters.append(letter)
        return True
    return False

def main():
    # Случайный выбор слова из списка
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    errors_count = 6

    print("Добро пожаловать в игру \"Угадай слово\"!")
    print(f"Загадано слово из {len(chosen_word)} букв: {display_word(chosen_word, guessed_letters)}")
    print(f"Осталось ошибок: {errors_count}")

    while errors_count > 0 and display_word(chosen_word, guessed_letters) != chosen_word:
        letter = input("Введите букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if check_letter(letter, chosen_word, guessed_letters):
            print(f"Отлично! \"{letter}\" есть в слове.")
        else:
            errors_count -= 1
            print(f"Буквы \"{letter}\" нет в слове. Осталось ошибок: {errors_count}")

        print(display_word(chosen_word, guessed_letters))

    if display_word(chosen_word, guessed_letters) == chosen_word:
        print(f"\nПоздравляю! Вы угадали слово \"{chosen_word}\" за {6 - errors_count} попыток!")
    else:
        print(f"\nВы проиграли. Правильный ответ: \"{chosen_word}\".")

if __name__ == "__main__":
    main()