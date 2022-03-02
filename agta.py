def agta_three():

    player_one = ['h']
    player_two = ['h']

    p1h = 1 if player_one[0] == 'h' else 0 # times player 1 played h
    p1t = 1 if player_one[0] == 't' else 0 # times player 1 played t

    p2h = 1 if player_two[0] == 'h' else 0 # times player 2 played h
    p2t = 1 if player_two[0] == 't' else 0 # times player 2 played t

    i = 1
    while i <= 40:
        pr1h = p1h / i # probability of player 1 playing h
        pr1t = p1t / i # probability of player 1 playing t

        pr2h = p2h / i # probability of player 2 playing h
        pr2t = p2t / i # probability of player 2 playing t

        if pr2h > pr2t:
            p = 'h'
        elif pr2h < pr2t:
            p = 't'
        else:
            p = 'h' if(player_two[-1] == 'h') else 't'

        if p == 'h':
            p1h += 1
        else:
            p1t += 1

        player_one.append(p)

        if pr1h < pr1t:
            m = 'h'
        elif pr1h > pr1t:
            m = 't'
        else:
            m = 't' if(player_one[-2] == 'h') else 'h'

        if m == 'h':
            p2h += 1
        else:
            p2t += 1

        player_two.append(m)
        i += 1

    print(list(zip(player_one, player_two)))


def main():
    agta_three()

if __name__ == '__main__':
    main()
