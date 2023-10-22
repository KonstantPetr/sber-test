import re


def create_good_nums(statement):
    good_nums = []
    special_nums = re.findall(r'(\d{2,4})\\(\d{2,5})', statement)
    for num in special_nums:
        start, end = num
        good_nums.append(f'{start.zfill(4)}\\{end.zfill(5)}')
    return good_nums


# cases
fast_tests = (
'Адрес 5467\\456. Номер 405\\549',  # ['5467\\00456', '0405\\00549']
'20\\15 103\\80553',                # ['0020\\00015', '0103\\80553']
'Привет, анаконда номер 151\\7611. На кого ты нас оставила? На кобру номер 11\\11? \
Что скажешь, насчёт питона номер 777\\9151? Он же круче, чем гадюка номер 9999\\19152!'
                                    # ['0151\\07611', '0011\\00011', '0777\\09151', '9999\\19152']
            )

for strng in fast_tests:
    print(f'initial input:\n{strng}\nresult:')
    for num in create_good_nums(strng):
        print(num)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
