new_odd_turn = [[[1, 1], [1, 1]]]  # starting position
new_even_turn = []

end_odd_turn = []
end_even_turn = []
current_com = 0
loop_lst = []
n = int(input("number of rounds: "))  # setting number of rounds


for i in range(1, n+1):
    for x in new_odd_turn:  # player 1's turn
        if len(x) == 1:  # check any position where the game is finished (i.e one of the player lost)
            continue
        elif len(x[0]) == 2 and len(x[1]) == 2:  # check if players have both hands
            if x[0][0] == x[0][1] and x[1][0] == x[1][1]:  # If both players are holding the same fingers on both hands
                a = (x[0][0] + x[1][0]) % 5  # adding fingers
                if a == 0:  # if p1 touching the hand causes p2 to extend all 5 fingers
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
            elif x[0][0] == x[0][1]:  # if p1 holds same number of fingers on both hands
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][0] + x[1][1]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                elif b == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
            elif x[1][0] == x[1][1]:  # if p2 holds the same number of fingers on both hands
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][1] + x[1][1]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                elif b == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
            else:  # both are holding different numbers
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][0] + x[1][1]) % 5
                c = (x[0][1] + x[1][0]) % 5
                d = (x[0][1] + x[1][1]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [c, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], d]])
                elif b == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [c, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], d]])
                elif c == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], d]])
                elif d == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [c, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], b]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [c, x[1][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][0], d]])

        elif len(x[0]) == 1 and len(x[1]) == 2:  # if p1 has one hand and p2 has 2
            if x[1][0] == x[1][1]:
                a = (x[0][0] + x[1][0]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0]], [x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0]], [a, x[1][1]]])
            else:
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][0] + x[1][1]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0]], [x[1][1]]])
                    end_odd_turn.append([[x[0][0]], [x[1][0], b]])
                elif b == 0:
                    end_odd_turn.append([[x[0][0]], [x[1][0]]])
                    end_odd_turn.append([[x[0][0]], [a, x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0]], [a, x[1][1]]])
                    end_odd_turn.append([[x[0][0]], [x[1][0], b]])

        elif len(x[1]) == 1 and len(x[0]) == 2:  # if p2 has one hand and p1 has two
            if x[0][0] == x[0][1]:
                a = (x[0][0] + x[1][0]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a]])
            else:
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][1] + x[1][0]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [b]])
                elif b == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [a]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a]])
                    end_odd_turn.append([[x[0][0], x[0][1]], [b]])

        elif len(x[1]) == 1 and len(x[0]) == 1:  # if both have one hand each
            a = (x[0][0] + x[1][0]) % 5
            if a == 0:
                end_odd_turn.append([[x[0][0]]])
            else:
                end_odd_turn.append([[x[0][0]], [a]])

    for x in end_odd_turn:  # looking for the 1432
        if x == [[1, 4], [2, 3]] or x == [[1, 4], [3, 2]] or x == [[4, 1], [2, 3]] or x == [[4, 1], [3, 2]]:
            loop_lst.append((i*2)-1)
            break

    current_com = current_com + len(end_odd_turn)  # adding up number of combinations in that round
    print("turn", (i*2)-1, ":", current_com)  # printing current total of combinations
    new_even_turn = end_odd_turn.copy()
    end_odd_turn.clear()

    for x in new_even_turn:  # p2 turn (the rest is similar to above)
        if len(x) == 1:
            continue
        elif len(x[0]) == 2 and len(x[1]) == 2:
            if x[1][0] == x[1][1] and x[0][0] == x[0][1]:
                a = (x[1][0] + x[0][0]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[x[0][0], a], [x[1][0], x[1][1]]])
            elif x[0][0] == x[0][1]:
                a = (x[1][0] + x[0][0]) % 5
                b = (x[1][1] + x[0][0]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], b], [x[1][0], x[1][1]]])
                elif b == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], a], [x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[x[0][0], a], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][1], b], [x[1][0], x[1][1]]])
            elif x[1][0] == x[1][1]:
                a = (x[1][0] + x[0][0]) % 5
                b = (x[1][1] + x[0][1]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], b], [x[1][0], x[1][1]]])
                elif b == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][1], a], [x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[x[0][1], a], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], b], [x[1][0], x[1][1]]])
            else:
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][0] + x[1][1]) % 5
                c = (x[0][1] + x[1][0]) % 5
                d = (x[0][1] + x[1][1]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[b, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], c], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], d], [x[1][0], x[1][1]]])
                elif b == 0:
                    end_even_turn.append([[a, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], c], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], d], [x[1][0], x[1][1]]])
                elif c == 0:
                    end_even_turn.append([[a, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[b, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], d], [x[1][0], x[1][1]]])
                elif d == 0:
                    end_even_turn.append([[a, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[b, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], c], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0]], [x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[a, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[b, x[0][1]], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], c], [x[1][0], x[1][1]]])
                    end_even_turn.append([[x[0][0], d], [x[1][0], x[1][1]]])

        elif len(x[0]) == 1 and len(x[1]) == 2:
            if x[1][0] == x[1][1]:
                a = (x[0][0] + x[1][0]) % 5
                if a == 0:
                    end_even_turn.append([[x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[a], [x[1][0], x[1][1]]])
            else:
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][0] + x[1][1]) % 5
                if a == 0:
                    end_even_turn.append([[x[1][0], x[1][1]]])
                    end_even_turn.append([[b], [x[1][0], x[1][1]]])
                elif b == 0:
                    end_even_turn.append([[x[1][0], x[1][1]]])
                    end_even_turn.append([[a], [x[1][0], x[1][1]]])
                else:
                    end_even_turn.append([[a], [x[1][0], x[1][1]]])
                    end_even_turn.append([[b], [x[1][0], x[1][1]]])

        elif len(x[0]) == 2 and len(x[1]) == 1:
            if x[0][0] == x[0][1]:
                a = (x[0][0] + x[1][0]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0]]])
                else:
                    end_even_turn.append([[x[0][0], a], [x[1][0]]])
            else:
                a = (x[0][0] + x[1][0]) % 5
                b = (x[0][1] + x[1][0]) % 5
                if a == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0]]])
                    end_even_turn.append([[x[0][0], b], [x[1][0]]])
                elif b == 0:
                    end_even_turn.append([[x[0][0]], [x[1][0]]])
                    end_even_turn.append([[x[0][0], a], [x[1][0]]])
                else:
                    end_even_turn.append([[x[0][0], a], [x[1][0]]])
                    end_even_turn.append([[x[0][0], b], [x[1][0]]])

        elif len(x[1]) == 1 and len(x[0]) == 1:
            a = (x[0][0] + x[1][0]) % 5
            if a == 0:
                end_even_turn.append([[x[1][0]]])
            else:
                end_even_turn.append([[a], [x[1][0]]])

    for x in end_even_turn:
        if x == [[1, 4], [2, 3]] or x == [[1, 4], [3, 2]] or x == [[4, 1], [2, 3]] or x == [[4, 1], [3, 2]]:
            loop_lst.append((i*2))
            break

    current_com = current_com + len(end_even_turn)
    print("turn", i*2, ":", current_com)
    new_odd_turn = end_even_turn.copy()
    end_even_turn.clear()

print("   ")
print("1432 loop combinations:")
for i in loop_lst:
    print("found in turn", i)
