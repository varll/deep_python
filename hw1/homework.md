# Домашнее задание к лекции #1

### 1. Написать консольную игру крестики-нолики.

Пример того, как схематично можно изобразить класс игры.

```py
class TicTacGame:

    def show_board():
        pass

    def validate_input():
        pass

    def start_game():
        pass

    def check_winner():
        pass


if __name__ == "__main__":
    game = TicTac()
    game.start_game()

```
Допустима реалиция без использоавния классов.

Пользовательский ввод осуществляется с помощью input, который необходимо валидировать и выводить понятное описание ошибки.

Схема класса не обязательно должна быть такой, можно добавлять и менять методы, держа в голове грамотную организацию кода, ненужное дублирование и код-лапшу.

По желанию, можно написать вспомогательную функцию, запустив которую, компьютер сыграет сам с собой без участия человека, либо сделать возможным игру между человеком и компьютером.


### 2. Написать тесты (unittest, assert) для игры, покрыв тестами основные методы

### 3. Проверить корректность и стиль кода с помощью pylint или flake8