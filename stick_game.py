def stick_game (player_1 = 'first player', player_2 = 'second player'):
    sticks = 10
    while sticks > 0:
        print(f'Сейчас в игре {sticks} палочек.')
        player_1_inp = int(input(f'Твой ход {player_1}! '))
        player_2_inp = int(input(f'Твой ход {player_2}! '))
        if 1 >= player_1_inp >= 3 or 1 >= player_2_inp >= 3:
            print('Нужно выбирать от 1 до 3 палочек')
            continue
        sticks -= player_1_inp
        if sticks == 1:
            print(f'{player_2} проиграл!')
            break
        sticks -= player_2_inp
        if sticks == 1:
            print(f'{player_1} проиграл!')
            break

stick_game()