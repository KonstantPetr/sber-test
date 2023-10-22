def find_biggest_num(data):
    data.sort(reverse=True)
    return int(''.join(data))


# cases
fast_tests = (
            ['11', '234', '005', '89'],  # 89 234 11 005
            ['89', '7625', '38', '04', '2', '74'],  # 89 7625 74 38 2 04
            ['6', '5', '2', '7', '9', '0', '1', '3', '4', '8'],  # 9 8 7 6 5 4 3 2 1 0
            ['74', '041', '531', '541', '542', '537', '5341', '535']  # 74 542 541 537 535 5341 531 041
            )
for lst in fast_tests:
    print(f'initial input: lst = {lst}\nresult: {find_biggest_num(lst)}')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
