new_odd_turn = [[[1, 1], [1, 1]]]
new_even_turn = []

end_odd_turn = []
end_even_turn = []
current_com = 0
loop_lst = []
n = int(input("number of rounds: "))


for i in range(1, n+1):
    for x in new_odd_turn:
        if len(x) == 1:
            continue
        elif len(x[0]) == 2 and len(x[1]) == 2:
            if x[0][0] == x[0][1] and x[1][0] == x[1][1]:
                a = (x[0][0] + x[1][0]) % 5
                if a == 0:
                    end_odd_turn.append([[x[0][0], x[0][1]], [x[1][1]]])
                else:
                    end_odd_turn.append([[x[0][0], x[0][1]], [a, x[1][1]]])
            elif x[0][0] == x[0][1]:
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
            elif x[1][0] == x[1][1]:
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
            else:
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

        elif len(x[0]) == 1 and len(x[1]) == 2:
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

        elif len(x[1]) == 1 and len(x[0]) == 2:
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

        elif len(x[1]) == 1 and len(x[0]) == 1:
            a = (x[0][0] + x[1][0]) % 5
            if a == 0:
                end_odd_turn.append([[x[0][0]]])
            else:
                end_odd_turn.append([[x[0][0]], [a]])

    for x in end_odd_turn:
        if x == [[1, 4], [2, 3]] or x == [[1, 4], [3, 2]] or x == [[4, 1], [2, 3]] or x == [[4, 1], [3, 2]]:
            loop_lst.append((i*2)-1)
            break

    current_com = current_com + len(end_odd_turn)
    print("turn", (i*2)-1, ":", current_com)
    new_even_turn = end_odd_turn.copy()
    end_odd_turn.clear()

    for x in new_even_turn:
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
