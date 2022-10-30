from tictactoe import Board

def game(board):

    i = 0
    print(board)
    print(f'Начинаем игру с крестика\n')
    while i <= 9:
        try:
            g1 = int(input('Укажите координаты поля от 0 до 2, где х=: '))
            g2 = int(input('Укажите координаты поля от 0 до 2, где y=: '))

            if board.is_empty((g1, g2)):
                board.push((g1, g2))
                if board.result() == 1:
                    print(f"\nПоздравляю!!! Выиграл игрок начавший игру с крестика")
                    print(board)
                    break
                elif board.result() == 2:
                    print(f"\nПоздравляю!! Выиграл игрок с ноликом")
                    print(board)
                    break
            else:
                print("ячейка занята")
                i -= 1
            i += 1
            if i == 9:
                print(f"\nНикто не выиграл - ничья!!!")
                print(board)
                break
            print(board)
        except:
            print("Не верно выбрано значение")

desk = Board((3, 3), 3)
game(desk)
