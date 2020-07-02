import random


class TicTacToeAiUser:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def occup_or_not(self):
        while True:
            coord = tuple(map(str, input('Enter the coordinates: > ').split(' ')))
            if not coord[0].isdigit() or not coord[1].isdigit():
                print('You should enter numbers!')
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif int(coord[0]) <= 0 or int(coord[1]) <= 0:
                print('Coordinates should be from 1 to 3!')
            else:
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[0] = self.l3[0].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[0] = self.l2[0].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[0] = self.l1[0].replace('_', self.opt)
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[1] = self.l3[1].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[1] = self.l2[1].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[1] = self.l1[1].replace('_', self.opt)
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[2] = self.l3[2].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[2] = self.l2[2].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[2] = self.l1[2].replace('_', self.opt)
                            break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    self.steps += 1
                    self.occup_or_not()
                else:
                    print('Making move level "easy"')
                    self.steps += 1
                    self.ai_step_easy()
            else:
                print('Draw')

    def ai_step_easy(self):
        while True:
            c1 = str(random.randint(1, 3))
            c2 = str(random.randint(1, 3))
            coord = (c1, c2)
            if coord[0] == '1':
                if coord[1] == '1':
                    if self.l3[0] != '_':
                        continue
                    else:
                        self.l3[0] = self.l3[0].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[0] != '_':
                        continue
                    else:
                        self.l2[0] = self.l2[0].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[0] != '_':
                        continue
                    else:
                        self.l1[0] = self.l1[0].replace('_', 'O')
                        break
            elif coord[0] == '2':
                if coord[1] == '1':
                    if self.l3[1] != '_':
                        continue
                    else:
                        self.l3[1] = self.l3[1].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[1] != '_':
                        continue
                    else:
                        self.l2[1] = self.l2[1].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[1] != '_':
                        continue
                    else:
                        self.l1[1] = self.l1[1].replace('_', 'O')
                        break
            elif coord[0] == '3':
                if coord[1] == '1':
                    if self.l3[2] != '_':
                        continue
                    else:
                        self.l3[2] = self.l3[2].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[2] != '_':
                        continue
                    else:
                        self.l2[2] = self.l2[2].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[2] != '_':
                        continue
                    else:
                        self.l1[2] = self.l1[2].replace('_', 'O')
                        break
        self.print_area()
        self.game_situation()


class TicTacToeAiAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "easy"')
                    self.steps += 1
                    self.ai_step_easy()
                else:
                    print('Making move level "easy"')
                    self.steps += 1
                    self.ai_step_easy2()
            else:
                print('Draw')

    def ai_step_easy(self):
        while True:
            c1 = str(random.randint(1, 3))
            c2 = str(random.randint(1, 3))
            coord = (c1, c2)
            if coord[0] == '1':
                if coord[1] == '1':
                    if self.l3[0] != '_':
                        continue
                    else:
                        self.l3[0] = self.l3[0].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[0] != '_':
                        continue
                    else:
                        self.l2[0] = self.l2[0].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[0] != '_':
                        continue
                    else:
                        self.l1[0] = self.l1[0].replace('_', 'X')
                        break
            elif coord[0] == '2':
                if coord[1] == '1':
                    if self.l3[1] != '_':
                        continue
                    else:
                        self.l3[1] = self.l3[1].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[1] != '_':
                        continue
                    else:
                        self.l2[1] = self.l2[1].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[1] != '_':
                        continue
                    else:
                        self.l1[1] = self.l1[1].replace('_', 'X')
                        break
            elif coord[0] == '3':
                if coord[1] == '1':
                    if self.l3[2] != '_':
                        continue
                    else:
                        self.l3[2] = self.l3[2].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[2] != '_':
                        continue
                    else:
                        self.l2[2] = self.l2[2].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[2] != '_':
                        continue
                    else:
                        self.l1[2] = self.l1[2].replace('_', 'X')
                        break
        self.print_area()
        self.game_situation()

    def ai_step_easy2(self):
        while True:
            c1 = str(random.randint(1, 3))
            c2 = str(random.randint(1, 3))
            coord = (c1, c2)
            if coord[0] == '1':
                if coord[1] == '1':
                    if self.l3[0] != '_':
                        continue
                    else:
                        self.l3[0] = self.l3[0].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[0] != '_':
                        continue
                    else:
                        self.l2[0] = self.l2[0].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[0] != '_':
                        continue
                    else:
                        self.l1[0] = self.l1[0].replace('_', 'O')
                        break
            elif coord[0] == '2':
                if coord[1] == '1':
                    if self.l3[1] != '_':
                        continue
                    else:
                        self.l3[1] = self.l3[1].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[1] != '_':
                        continue
                    else:
                        self.l2[1] = self.l2[1].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[1] != '_':
                        continue
                    else:
                        self.l1[1] = self.l1[1].replace('_', 'O')
                        break
            elif coord[0] == '3':
                if coord[1] == '1':
                    if self.l3[2] != '_':
                        continue
                    else:
                        self.l3[2] = self.l3[2].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[2] != '_':
                        continue
                    else:
                        self.l2[2] = self.l2[2].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[2] != '_':
                        continue
                    else:
                        self.l1[2] = self.l1[2].replace('_', 'O')
                        break
        self.print_area()
        self.game_situation()


class TicTacToeUserUser:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def occup_or_not(self):
        while True:
            coord = tuple(map(str, input('Enter the coordinates: > ').split(' ')))
            if not coord[0].isdigit() or not coord[1].isdigit():
                print('You should enter numbers!')
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif int(coord[0]) <= 0 or int(coord[1]) <= 0:
                print('Coordinates should be from 1 to 3!')
            else:
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'X')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'X')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'X')
                            break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    self.steps += 1
                    self.occup_or_not()
                else:
                    self.steps += 1
                    self.occup_or_not2()
            else:
                print('Draw')

    def occup_or_not2(self):
        while True:
            coord = tuple(map(str, input('Enter the coordinates: > ').split(' ')))
            if not coord[0].isdigit() or not coord[1].isdigit():
                print('You should enter numbers!')
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif int(coord[0]) <= 0 or int(coord[1]) <= 0:
                print('Coordinates should be from 1 to 3!')
            else:
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()


class TicTacToeMedAiEasyAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def ai_step_easy(self):
        while True:
            c1 = str(random.randint(1, 3))
            c2 = str(random.randint(1, 3))
            coord = (c1, c2)
            if coord[0] == '1':
                if coord[1] == '1':
                    if self.l3[0] != '_':
                        continue
                    else:
                        self.l3[0] = self.l3[0].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[0] != '_':
                        continue
                    else:
                        self.l2[0] = self.l2[0].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[0] != '_':
                        continue
                    else:
                        self.l1[0] = self.l1[0].replace('_', 'X')
                        break
            elif coord[0] == '2':
                if coord[1] == '1':
                    if self.l3[1] != '_':
                        continue
                    else:
                        self.l3[1] = self.l3[1].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[1] != '_':
                        continue
                    else:
                        self.l2[1] = self.l2[1].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[1] != '_':
                        continue
                    else:
                        self.l1[1] = self.l1[1].replace('_', 'X')
                        break
            elif coord[0] == '3':
                if coord[1] == '1':
                    if self.l3[2] != '_':
                        continue
                    else:
                        self.l3[2] = self.l3[2].replace('_', 'X')
                        break
                elif coord[1] == '2':
                    if self.l2[2] != '_':
                        continue
                    else:
                        self.l2[2] = self.l2[2].replace('_', 'X')
                        break
                elif coord[1] == '3':
                    if self.l1[2] != '_':
                        continue
                    else:
                        self.l1[2] = self.l1[2].replace('_', 'X')
                        break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "easy"')
                    self.steps += 1
                    self.ai_step_easy()
                else:
                    print('Making move level "medium"')
                    self.steps += 1
                    self.ai_step_med()
            else:
                print('Draw')

    def ai_step_med(self):
        if self.med_ai():
            pass
        else:
            while True:
                c1 = str(random.randint(1, 3))
                c2 = str(random.randint(1, 3))
                coord = (c1, c2)
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            continue
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            continue
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            continue
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            continue
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            continue
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            continue
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            continue
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            continue
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            continue
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()

    def med_ai(self):
        # left and right horizont
        if self.l1[0] == self.l1[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        elif self.l1[1] == self.l1[2] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l3[0] == self.l3[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[1] == self.l3[2] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        # 0, 1 vertical
        elif self.l1[0] == self.l2[0] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l1[1] == self.l2[1] != '_' and self.l3[1] == '_':
            self.l3[1] = self.l3[1].replace('_', 'O')
            return True
        elif self.l1[2] == self.l2[2] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        # 1, 2 vertical
        elif self.l2[0] == self.l3[0] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l3[1] != '_' and self.l1[1] == '_':
            self.l1[1] = self.l1[1].replace('_', 'O')
            return True
        elif self.l2[2] == self.l3[2] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # left diagonal
        elif self.l1[0] == self.l2[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[0] == self.l2[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # right diagonal
        elif self.l1[2] == self.l2[1] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l3[2] == self.l2[1] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True


class TicTacToeMedAiUser:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def occup_or_not(self):
        while True:
            coord = tuple(map(str, input('Enter the coordinates: > ').split(' ')))
            if not coord[0].isdigit() or not coord[1].isdigit():
                print('You should enter numbers!')
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif int(coord[0]) <= 0 or int(coord[1]) <= 0:
                print('Coordinates should be from 1 to 3!')
            else:
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[0] = self.l3[0].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[0] = self.l2[0].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[0] = self.l1[0].replace('_', self.opt)
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[1] = self.l3[1].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[1] = self.l2[1].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[1] = self.l1[1].replace('_', self.opt)
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[2] = self.l3[2].replace('_', self.opt)
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[2] = self.l2[2].replace('_', self.opt)
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[2] = self.l1[2].replace('_', self.opt)
                            break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    self.steps += 1
                    self.occup_or_not()
                else:
                    print('Making move level "medium"')
                    self.steps += 1
                    self.ai_step_med()
            else:
                print('Draw')

    def ai_step_med(self):
        if self.med_ai():
            pass
        else:
            while True:
                c1 = str(random.randint(1, 3))
                c2 = str(random.randint(1, 3))
                coord = (c1, c2)
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            continue
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            continue
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            continue
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            continue
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            continue
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            continue
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            continue
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            continue
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            continue
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()

    def med_ai(self):
        # left and right horizont
        if self.l1[0] == self.l1[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        elif self.l1[1] == self.l1[2] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[0] == self.l2[1] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l3[0] == self.l3[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[1] == self.l3[2] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        # 0, 1 vertical
        elif self.l1[0] == self.l2[0] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l1[1] == self.l2[1] != '_' and self.l3[1] == '_':
            self.l3[1] = self.l3[1].replace('_', 'O')
            return True
        elif self.l1[2] == self.l2[2] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        # 1, 2 vertical
        elif self.l2[0] == self.l3[0] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l3[1] != '_' and self.l1[1] == '_':
            self.l1[1] = self.l1[1].replace('_', 'O')
            return True
        elif self.l2[2] == self.l3[2] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # left diagonal
        elif self.l1[0] == self.l2[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[0] == self.l2[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # right diagonal
        elif self.l1[2] == self.l2[1] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l3[2] == self.l2[1] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True


class TicTacToeMedAiMedAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "medium"')
                    self.steps += 1
                    self.ai_step_med2()
                else:
                    print('Making move level "medium"')
                    self.steps += 1
                    self.ai_step_med()
            else:
                print('Draw')

    def ai_step_med(self):
        if self.med_ai():
            pass
        else:
            while True:
                c1 = str(random.randint(1, 3))
                c2 = str(random.randint(1, 3))
                coord = (c1, c2)
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            continue
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            continue
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            continue
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            continue
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            continue
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            continue
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            continue
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            continue
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            continue
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()

    def med_ai(self):
        # left and right horizont
        if self.l1[0] == self.l1[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        elif self.l1[1] == self.l1[2] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l3[0] == self.l3[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[1] == self.l3[2] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        # 0, 1 vertical
        elif self.l1[0] == self.l2[0] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l1[1] == self.l2[1] != '_' and self.l3[1] == '_':
            self.l3[1] = self.l3[1].replace('_', 'O')
            return True
        elif self.l1[2] == self.l2[2] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        # 1, 2 vertical
        elif self.l2[0] == self.l3[0] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l3[1] != '_' and self.l1[1] == '_':
            self.l1[1] = self.l1[1].replace('_', 'O')
            return True
        elif self.l2[2] == self.l3[2] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # left diagonal
        elif self.l1[0] == self.l2[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[0] == self.l2[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # right diagonal
        elif self.l1[2] == self.l2[1] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l3[2] == self.l2[1] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True

    def ai_step_med2(self):
        if self.med_ai2():
            pass
        else:
            while True:
                c1 = str(random.randint(1, 3))
                c2 = str(random.randint(1, 3))
                coord = (c1, c2)
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            continue
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            continue
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            continue
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'X')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            continue
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            continue
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            continue
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'X')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            continue
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'X')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            continue
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'X')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            continue
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'X')
                            break
        self.print_area()
        self.game_situation()

    def med_ai2(self):
        # left and right horizont
        if self.l1[0] == self.l1[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'X')
            return True
        elif self.l1[1] == self.l1[2] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'X')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'X')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'X')
            return True
        elif self.l3[0] == self.l3[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'X')
            return True
        elif self.l3[1] == self.l3[2] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'X')
            return True
        # 0, 1 vertical
        elif self.l1[0] == self.l2[0] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'X')
            return True
        elif self.l1[1] == self.l2[1] != '_' and self.l3[1] == '_':
            self.l3[1] = self.l3[1].replace('_', 'X')
            return True
        elif self.l1[2] == self.l2[2] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'X')
            return True
        # 1, 2 vertical
        elif self.l2[0] == self.l3[0] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'X')
            return True
        elif self.l2[1] == self.l3[1] != '_' and self.l1[1] == '_':
            self.l1[1] = self.l1[1].replace('_', 'X')
            return True
        elif self.l2[2] == self.l3[2] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'X')
            return True
        # left diagonal
        elif self.l1[0] == self.l2[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'X')
            return True
        elif self.l3[0] == self.l2[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'X')
            return True
        # right diagonal
        elif self.l1[2] == self.l2[1] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'X')
            return True
        elif self.l3[2] == self.l2[1] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'X')
            return True


class TicTacToeHardAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def occup_or_not(self):
        while True:
            coord = tuple(map(str, input('Enter the coordinates: > ').split(' ')))
            if not coord[0].isdigit() or not coord[1].isdigit():
                print('You should enter numbers!')
            elif int(coord[0]) > 3 or int(coord[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif int(coord[0]) <= 0 or int(coord[1]) <= 0:
                print('Coordinates should be from 1 to 3!')
            else:
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            print('This cell is occupied! Choose another one!')
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "hard"')
                    self.steps += 1
                    self.hard_ai()
                else:
                    self.steps += 1
                    self.occup_or_not()
            else:
                print('Draw')

    def hard_ai(self):
        huPlayer = "O"
        aiPlayer = "X"
        origBoard = []
        l_all = self.l1 + self.l2 + self.l3
        for zse in range(len(l_all)):
            if l_all[zse] == '_':
                origBoard.append(str(zse))
            else:
                origBoard.append(l_all[zse])
        # returns the available spots on the board
        def emptyIndexies(board):
            board_new = []
            for i in board:
                if i.isdigit():
                    board_new.append(int(i))
            return board_new

        # the main minimax function
        def minimax(newBoard, player):
            # available spots var
            availSpots = emptyIndexies(newBoard)
            # checks for the terminal states such as win, lose, and tie and returning a value accordingly
            if winning(newBoard, huPlayer):
                return -10
            elif winning(newBoard, aiPlayer):
                return 10
            else:
                if len(availSpots) == 0:
                    return 0
            # an array to collect all the objects
            moves = []
            # loop through available spots
            for i in availSpots:
                # create an object for each and store the index of that spot that was stored as a number in the object's
                # index key
                move = {}
                move['index'] = newBoard[i]
                # set the empty spot to the current player
                newBoard[i] = player
                # if collect the score resulted from calling minimax on the opponent of the current player
                if player == aiPlayer:
                    result = minimax(newBoard, huPlayer)
                    move['score'] = result
                else:
                    result = minimax(newBoard, aiPlayer)
                    move['score'] = result
                # reset the spot to empty
                newBoard[i] = move['index']
                # push the object to the array
                moves.append(move)
            # if it is the computer's turn loop over the moves and choose the move with the highest score
            bestMove = 0
            if player == aiPlayer:
                bestScore = -10000
                for i in range(len(moves)):
                    # print(moves[i])
                    if moves[i]['score'] > bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            else:
                # else loop over the moves and choose the move with the lowest score
                bestScore = 10000
                for i in range(len(moves)):
                    if moves[i]['score'] < bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            # return the chosen move (object) from the array to the higher depth
            return bestMove

        #  winning combinations using the board indexies for instace the first win could be 3 xes in a row
        def winning(board, player):
            if board[0] == player and board[1] == player and board[2] == player or \
                    board[3] == player and board[4] == player and board[5] == player or \
                    board[6] == player and board[7] == player and board[8] == player or \
                    board[0] == player and board[3] == player and board[6] == player or \
                    board[1] == player and board[4] == player and board[7] == player or \
                    board[2] == player and board[5] == player and board[8] == player or \
                    board[0] == player and board[4] == player and board[8] == player or \
                    board[2] == player and board[4] == player and board[6] == player:
                return True
            else:
                return False

        # finding the ultimate play on the game that favors the computer
        bestSpot = minimax(origBoard, aiPlayer)
        if bestSpot <= 2:
            self.l1[bestSpot] = 'X'
        elif 5 >= bestSpot >= 3:
            self.l2[bestSpot - 3] = 'X'
        elif 8 >= bestSpot >= 6:
            self.l3[bestSpot - 6] = 'X'
        self.print_area()
        self.game_situation()


class TicTacToeHardAiHardAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def hard_ai2(self):
        huPlayer = "O"
        aiPlayer = "X"
        origBoard = []
        l_all = self.l1 + self.l2 + self.l3
        for zse in range(len(l_all)):
            if l_all[zse] == '_':
                origBoard.append(str(zse))
            else:
                origBoard.append(l_all[zse])
        # returns the available spots on the board
        def emptyIndexies(board):
            board_new = []
            for i in board:
                if i.isdigit():
                    board_new.append(int(i))
            return board_new

        # the main minimax function
        def minimax(newBoard, player):
            # available spots var
            availSpots = emptyIndexies(newBoard)
            # checks for the terminal states such as win, lose, and tie and returning a value accordingly
            if winning(newBoard, huPlayer):
                return -10
            elif winning(newBoard, aiPlayer):
                return 10
            else:
                if len(availSpots) == 0:
                    return 0
            # an array to collect all the objects
            moves = []
            # loop through available spots
            for i in availSpots:
                # create an object for each and store the index of that spot that was stored as a number in the object's
                # index key
                move = {}
                move['index'] = newBoard[i]
                # set the empty spot to the current player
                newBoard[i] = player
                # if collect the score resulted from calling minimax on the opponent of the current player
                if player == aiPlayer:
                    result = minimax(newBoard, huPlayer)
                    move['score'] = result
                else:
                    result = minimax(newBoard, aiPlayer)
                    move['score'] = result
                # reset the spot to empty
                newBoard[i] = move['index']
                # push the object to the array
                moves.append(move)
            # if it is the computer's turn loop over the moves and choose the move with the highest score
            bestMove = 0
            if player == aiPlayer:
                bestScore = -10000
                for i in range(len(moves)):
                    # print(moves[i])
                    if moves[i]['score'] > bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            else:
                # else loop over the moves and choose the move with the lowest score
                bestScore = 10000
                for i in range(len(moves)):
                    if moves[i]['score'] < bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            # return the chosen move (object) from the array to the higher depth
            return bestMove

        #  winning combinations using the board indexies for instace the first win could be 3 xes in a row
        def winning(board, player):
            if board[0] == player and board[1] == player and board[2] == player or \
                    board[3] == player and board[4] == player and board[5] == player or \
                    board[6] == player and board[7] == player and board[8] == player or \
                    board[0] == player and board[3] == player and board[6] == player or \
                    board[1] == player and board[4] == player and board[7] == player or \
                    board[2] == player and board[5] == player and board[8] == player or \
                    board[0] == player and board[4] == player and board[8] == player or \
                    board[2] == player and board[4] == player and board[6] == player:
                return True
            else:
                return False

        # finding the ultimate play on the game that favors the computer
        bestSpot = minimax(origBoard, aiPlayer)
        if bestSpot <= 2:
            self.l1[bestSpot] = 'O'
        elif 5 >= bestSpot >= 3:
            self.l2[bestSpot - 3] = 'O'
        elif 8 >= bestSpot >= 6:
            self.l3[bestSpot - 6] = 'O'
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "hard"')
                    self.steps += 1
                    self.hard_ai()
                else:
                    print('Making move level "hard"')
                    self.steps += 1
                    self.hard_ai2()
            else:
                print('Draw')

    def hard_ai(self):
        huPlayer = "O"
        aiPlayer = "X"
        origBoard = []
        l_all = self.l1 + self.l2 + self.l3
        for zse in range(len(l_all)):
            if l_all[zse] == '_':
                origBoard.append(str(zse))
            else:
                origBoard.append(l_all[zse])
        # returns the available spots on the board
        def emptyIndexies(board):
            board_new = []
            for i in board:
                if i.isdigit():
                    board_new.append(int(i))
            return board_new

        # the main minimax function
        def minimax(newBoard, player):
            # available spots var
            availSpots = emptyIndexies(newBoard)
            # checks for the terminal states such as win, lose, and tie and returning a value accordingly
            if winning(newBoard, huPlayer):
                return -10
            elif winning(newBoard, aiPlayer):
                return 10
            else:
                if len(availSpots) == 0:
                    return 0
            # an array to collect all the objects
            moves = []
            # loop through available spots
            for i in availSpots:
                # create an object for each and store the index of that spot that was stored as a number in the object's
                # index key
                move = {}
                move['index'] = newBoard[i]
                # set the empty spot to the current player
                newBoard[i] = player
                # if collect the score resulted from calling minimax on the opponent of the current player
                if player == aiPlayer:
                    result = minimax(newBoard, huPlayer)
                    move['score'] = result
                else:
                    result = minimax(newBoard, aiPlayer)
                    move['score'] = result
                # reset the spot to empty
                newBoard[i] = move['index']
                # push the object to the array
                moves.append(move)
            # if it is the computer's turn loop over the moves and choose the move with the highest score
            bestMove = 0
            if player == aiPlayer:
                bestScore = -10000
                for i in range(len(moves)):
                    # print(moves[i])
                    if moves[i]['score'] > bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            else:
                # else loop over the moves and choose the move with the lowest score
                bestScore = 10000
                for i in range(len(moves)):
                    if moves[i]['score'] < bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            # return the chosen move (object) from the array to the higher depth
            return bestMove

        #  winning combinations using the board indexies for instace the first win could be 3 xes in a row
        def winning(board, player):
            if board[0] == player and board[1] == player and board[2] == player or \
                    board[3] == player and board[4] == player and board[5] == player or \
                    board[6] == player and board[7] == player and board[8] == player or \
                    board[0] == player and board[3] == player and board[6] == player or \
                    board[1] == player and board[4] == player and board[7] == player or \
                    board[2] == player and board[5] == player and board[8] == player or \
                    board[0] == player and board[4] == player and board[8] == player or \
                    board[2] == player and board[4] == player and board[6] == player:
                return True
            else:
                return False

        # finding the ultimate play on the game that favors the computer
        bestSpot = minimax(origBoard, aiPlayer)
        if bestSpot <= 2:
            self.l1[bestSpot] = 'X'
        elif 5 >= bestSpot >= 3:
            self.l2[bestSpot - 3] = 'X'
        elif 8 >= bestSpot >= 6:
            self.l3[bestSpot - 6] = 'X'
        self.print_area()
        self.game_situation()


class TicTacToeHardAiMedAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def ai_step_med(self):
        if self.med_ai():
            pass
        else:
            while True:
                c1 = str(random.randint(1, 3))
                c2 = str(random.randint(1, 3))
                coord = (c1, c2)
                if coord[0] == '1':
                    if coord[1] == '1':
                        if self.l3[0] != '_':
                            continue
                        else:
                            self.l3[0] = self.l3[0].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[0] != '_':
                            continue
                        else:
                            self.l2[0] = self.l2[0].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[0] != '_':
                            continue
                        else:
                            self.l1[0] = self.l1[0].replace('_', 'O')
                            break
                elif coord[0] == '2':
                    if coord[1] == '1':
                        if self.l3[1] != '_':
                            continue
                        else:
                            self.l3[1] = self.l3[1].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[1] != '_':
                            continue
                        else:
                            self.l2[1] = self.l2[1].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[1] != '_':
                            continue
                        else:
                            self.l1[1] = self.l1[1].replace('_', 'O')
                            break
                elif coord[0] == '3':
                    if coord[1] == '1':
                        if self.l3[2] != '_':
                            continue
                        else:
                            self.l3[2] = self.l3[2].replace('_', 'O')
                            break
                    elif coord[1] == '2':
                        if self.l2[2] != '_':
                            continue
                        else:
                            self.l2[2] = self.l2[2].replace('_', 'O')
                            break
                    elif coord[1] == '3':
                        if self.l1[2] != '_':
                            continue
                        else:
                            self.l1[2] = self.l1[2].replace('_', 'O')
                            break
        self.print_area()
        self.game_situation()

    def med_ai(self):
        # left and right horizont
        if self.l1[0] == self.l1[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        elif self.l1[1] == self.l1[2] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l2[2] != '_' and self.l2[0] == '_':
            self.l2[0] = self.l2[0].replace('_', 'O')
            return True
        elif self.l3[0] == self.l3[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[1] == self.l3[2] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        # 0, 1 vertical
        elif self.l1[0] == self.l2[0] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l1[1] == self.l2[1] != '_' and self.l3[1] == '_':
            self.l3[1] = self.l3[1].replace('_', 'O')
            return True
        elif self.l1[2] == self.l2[2] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        # 1, 2 vertical
        elif self.l2[0] == self.l3[0] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True
        elif self.l2[1] == self.l3[1] != '_' and self.l1[1] == '_':
            self.l1[1] = self.l1[1].replace('_', 'O')
            return True
        elif self.l2[2] == self.l3[2] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # left diagonal
        elif self.l1[0] == self.l2[1] != '_' and self.l3[2] == '_':
            self.l3[2] = self.l3[2].replace('_', 'O')
            return True
        elif self.l3[0] == self.l2[1] != '_' and self.l1[2] == '_':
            self.l1[2] = self.l1[2].replace('_', 'O')
            return True
        # right diagonal
        elif self.l1[2] == self.l2[1] != '_' and self.l3[0] == '_':
            self.l3[0] = self.l3[0].replace('_', 'O')
            return True
        elif self.l3[2] == self.l2[1] != '_' and self.l1[0] == '_':
            self.l1[0] = self.l1[0].replace('_', 'O')
            return True

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "hard"')
                    self.steps += 1
                    self.hard_ai()
                else:
                    print('Making move level "medium"')
                    self.steps += 1
                    self.med_ai()
            else:
                print('Draw')

    def hard_ai(self):
        huPlayer = "O"
        aiPlayer = "X"
        origBoard = []
        l_all = self.l1 + self.l2 + self.l3
        for zse in range(len(l_all)):
            if l_all[zse] == '_':
                origBoard.append(str(zse))
            else:
                origBoard.append(l_all[zse])
        # returns the available spots on the board
        def emptyIndexies(board):
            board_new = []
            for i in board:
                if i.isdigit():
                    board_new.append(int(i))
            return board_new

        # the main minimax function
        def minimax(newBoard, player):
            # available spots var
            availSpots = emptyIndexies(newBoard)
            # checks for the terminal states such as win, lose, and tie and returning a value accordingly
            if winning(newBoard, huPlayer):
                return -10
            elif winning(newBoard, aiPlayer):
                return 10
            else:
                if len(availSpots) == 0:
                    return 0
            # an array to collect all the objects
            moves = []
            # loop through available spots
            for i in availSpots:
                # create an object for each and store the index of that spot that was stored as a number in the object's
                # index key
                move = {}
                move['index'] = newBoard[i]
                # set the empty spot to the current player
                newBoard[i] = player
                # if collect the score resulted from calling minimax on the opponent of the current player
                if player == aiPlayer:
                    result = minimax(newBoard, huPlayer)
                    move['score'] = result
                else:
                    result = minimax(newBoard, aiPlayer)
                    move['score'] = result
                # reset the spot to empty
                newBoard[i] = move['index']
                # push the object to the array
                moves.append(move)
            # if it is the computer's turn loop over the moves and choose the move with the highest score
            bestMove = 0
            if player == aiPlayer:
                bestScore = -10000
                for i in range(len(moves)):
                    # print(moves[i])
                    if moves[i]['score'] > bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            else:
                # else loop over the moves and choose the move with the lowest score
                bestScore = 10000
                for i in range(len(moves)):
                    if moves[i]['score'] < bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            # return the chosen move (object) from the array to the higher depth
            return bestMove

        #  winning combinations using the board indexies for instace the first win could be 3 xes in a row
        def winning(board, player):
            if board[0] == player and board[1] == player and board[2] == player or \
                    board[3] == player and board[4] == player and board[5] == player or \
                    board[6] == player and board[7] == player and board[8] == player or \
                    board[0] == player and board[3] == player and board[6] == player or \
                    board[1] == player and board[4] == player and board[7] == player or \
                    board[2] == player and board[5] == player and board[8] == player or \
                    board[0] == player and board[4] == player and board[8] == player or \
                    board[2] == player and board[4] == player and board[6] == player:
                return True
            else:
                return False

        # finding the ultimate play on the game that favors the computer
        bestSpot = minimax(origBoard, aiPlayer)
        if bestSpot <= 2:
            self.l1[bestSpot] = 'X'
        elif 5 >= bestSpot >= 3:
            self.l2[bestSpot - 3] = 'X'
        elif 8 >= bestSpot >= 6:
            self.l3[bestSpot - 6] = 'X'
        self.print_area()
        self.game_situation()



class TicTacToeHardAiEasyAi:
    def __init__(self, field):
        self.field = field
        self.l1 = list(field[0:3])
        self.l2 = list(field[3:6])
        self.l3 = list(field[6:])
        self.steps = 1
        self.opt = 'X'

    def print_area(self):
        print('---------')
        print('|', *self.l1, '|')
        print('|', *self.l2, '|')
        print('|', *self.l3, '|')
        print('---------')

    def ai_step_easy(self):
        while True:
            c1 = str(random.randint(1, 3))
            c2 = str(random.randint(1, 3))
            coord = (c1, c2)
            if coord[0] == '1':
                if coord[1] == '1':
                    if self.l3[0] != '_':
                        continue
                    else:
                        self.l3[0] = self.l3[0].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[0] != '_':
                        continue
                    else:
                        self.l2[0] = self.l2[0].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[0] != '_':
                        continue
                    else:
                        self.l1[0] = self.l1[0].replace('_', 'O')
                        break
            elif coord[0] == '2':
                if coord[1] == '1':
                    if self.l3[1] != '_':
                        continue
                    else:
                        self.l3[1] = self.l3[1].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[1] != '_':
                        continue
                    else:
                        self.l2[1] = self.l2[1].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[1] != '_':
                        continue
                    else:
                        self.l1[1] = self.l1[1].replace('_', 'O')
                        break
            elif coord[0] == '3':
                if coord[1] == '1':
                    if self.l3[2] != '_':
                        continue
                    else:
                        self.l3[2] = self.l3[2].replace('_', 'O')
                        break
                elif coord[1] == '2':
                    if self.l2[2] != '_':
                        continue
                    else:
                        self.l2[2] = self.l2[2].replace('_', 'O')
                        break
                elif coord[1] == '3':
                    if self.l1[2] != '_':
                        continue
                    else:
                        self.l1[2] = self.l1[2].replace('_', 'O')
                        break
        self.print_area()
        self.game_situation()

    def game_situation(self):
        if self.l1[0] == self.l1[1] == self.l1[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l2[0] == self.l2[1] == self.l2[2] != '_':
            print(f'{self.l2[0]} wins')
        elif self.l3[0] == self.l3[1] == self.l3[2] != '_':
            print(f'{self.l3[0]} wins')
        elif self.l1[0] == self.l2[0] == self.l3[0] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[1] == self.l2[1] == self.l3[1] != '_':
            print(f'{self.l1[1]} wins')
        elif self.l1[2] == self.l2[2] == self.l3[2] != '_':
            print(f'{self.l1[2]} wins')
        elif self.l1[0] == self.l2[1] == self.l3[2] != '_':
            print(f'{self.l1[0]} wins')
        elif self.l1[2] == self.l2[1] == self.l3[0] != '_':
            print(f'{self.l1[2]} wins')
        else:
            l_all = self.l1 + self.l2 + self.l3
            if l_all.count('X') + l_all.count('O') != 9:
                if self.steps % 2 == 0:
                    print('Making move level "hard"')
                    self.steps += 1
                    self.hard_ai()
                else:
                    print('Making move level "easy"')
                    self.steps += 1
                    self.ai_step_easy()
            else:
                print('Draw')

    def hard_ai(self):
        huPlayer = "O"
        aiPlayer = "X"
        origBoard = []
        l_all = self.l1 + self.l2 + self.l3
        for zse in range(len(l_all)):
            if l_all[zse] == '_':
                origBoard.append(str(zse))
            else:
                origBoard.append(l_all[zse])
        # returns the available spots on the board
        def emptyIndexies(board):
            board_new = []
            for i in board:
                if i.isdigit():
                    board_new.append(int(i))
            return board_new

        # the main minimax function
        def minimax(newBoard, player):
            # available spots var
            availSpots = emptyIndexies(newBoard)
            # checks for the terminal states such as win, lose, and tie and returning a value accordingly
            if winning(newBoard, huPlayer):
                return -10
            elif winning(newBoard, aiPlayer):
                return 10
            else:
                if len(availSpots) == 0:
                    return 0
            # an array to collect all the objects
            moves = []
            # loop through available spots
            for i in availSpots:
                # create an object for each and store the index of that spot that was stored as a number in the object's
                # index key
                move = {}
                move['index'] = newBoard[i]
                # set the empty spot to the current player
                newBoard[i] = player
                # if collect the score resulted from calling minimax on the opponent of the current player
                if player == aiPlayer:
                    result = minimax(newBoard, huPlayer)
                    move['score'] = result
                else:
                    result = minimax(newBoard, aiPlayer)
                    move['score'] = result
                # reset the spot to empty
                newBoard[i] = move['index']
                # push the object to the array
                moves.append(move)
            # if it is the computer's turn loop over the moves and choose the move with the highest score
            bestMove = 0
            if player == aiPlayer:
                bestScore = -10000
                for i in range(len(moves)):
                    # print(moves[i])
                    if moves[i]['score'] > bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            else:
                # else loop over the moves and choose the move with the lowest score
                bestScore = 10000
                for i in range(len(moves)):
                    if moves[i]['score'] < bestScore:
                        bestScore = moves[i]['score']
                        bestMove = int(moves[i]['index'])
            # return the chosen move (object) from the array to the higher depth
            return bestMove

        #  winning combinations using the board indexies for instace the first win could be 3 xes in a row
        def winning(board, player):
            if board[0] == player and board[1] == player and board[2] == player or \
                    board[3] == player and board[4] == player and board[5] == player or \
                    board[6] == player and board[7] == player and board[8] == player or \
                    board[0] == player and board[3] == player and board[6] == player or \
                    board[1] == player and board[4] == player and board[7] == player or \
                    board[2] == player and board[5] == player and board[8] == player or \
                    board[0] == player and board[4] == player and board[8] == player or \
                    board[2] == player and board[4] == player and board[6] == player:
                return True
            else:
                return False

        # finding the ultimate play on the game that favors the computer
        bestSpot = minimax(origBoard, aiPlayer)
        if bestSpot <= 2:
            self.l1[bestSpot] = 'X'
        elif 5 >= bestSpot >= 3:
            self.l2[bestSpot - 3] = 'X'
        elif 8 >= bestSpot >= 6:
            self.l3[bestSpot - 6] = 'X'
        self.print_area()
        self.game_situation()


cells = '_________'
while True:
    command_to_start = input('Input command: > ').split(' ')
    if command_to_start[0] == 'start' and len(command_to_start) == 3:
        if command_to_start[1] == 'easy' and command_to_start[2] == 'user':
            fieldd = TicTacToeAiUser(cells)
            fieldd.print_area()
            fieldd.occup_or_not()
        elif command_to_start[1] == 'user' and command_to_start[2] == 'easy':
            fieldd = TicTacToeAiUser(cells)
            fieldd.print_area()
            fieldd.occup_or_not()
        elif command_to_start[1] == 'easy' and command_to_start[2] == 'easy':
            field1 = TicTacToeAiAi(cells)
            field1.print_area()
            field1.ai_step_easy()
        elif command_to_start[1] == 'user' and command_to_start[2] == 'user':
            fieldd = TicTacToeUserUser(cells)
            fieldd.print_area()
            fieldd.occup_or_not()
        elif command_to_start[1] == 'easy' and command_to_start[2] == 'medium':
            fieldd = TicTacToeMedAiEasyAi(cells)
            fieldd.print_area()
            fieldd.ai_step_easy()
        elif command_to_start[1] == 'medium' and command_to_start[2] == 'easy':
            fieldd = TicTacToeMedAiEasyAi(cells)
            fieldd.print_area()
            fieldd.ai_step_easy()
        elif command_to_start[1] == 'user' and command_to_start[2] == 'medium':
            fieldd = TicTacToeMedAiUser(cells)
            fieldd.print_area()
            fieldd.occup_or_not()
        elif command_to_start[1] == 'medium' and command_to_start[2] == 'user':
            fieldd = TicTacToeMedAiUser(cells)
            fieldd.print_area()
            fieldd.occup_or_not()
        elif command_to_start[1] == 'medium' and command_to_start[2] == 'medium':
            field1 = TicTacToeMedAiMedAi(cells)
            field1.print_area()
            field1.med_ai2()
        elif command_to_start[1] == 'hard' and command_to_start[2] == 'user':
            field1 = TicTacToeHardAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'user' and command_to_start[2] == 'hard':
            field1 = TicTacToeHardAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'hard' and command_to_start[2] == 'hard':
            field1 = TicTacToeHardAiHardAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'medium' and command_to_start[2] == 'hard':
            field1 = TicTacToeHardAiMedAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'hard' and command_to_start[2] == 'medium':
            field1 = TicTacToeHardAiMedAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'easy' and command_to_start[2] == 'hard':
            field1 = TicTacToeHardAiEasyAi(cells)
            field1.print_area()
            field1.hard_ai()
        elif command_to_start[1] == 'hard' and command_to_start[2] == 'easy':
            field1 = TicTacToeHardAiEasyAi(cells)
            field1.print_area()
            field1.hard_ai()
        else:
            print('Bad parameters!')
    elif command_to_start[0] == 'exit':
        break
    else:
        print('Bad parameters!')
