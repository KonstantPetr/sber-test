# sber-test
![image](https://i.ibb.co/Jy11cyn/kandinsky-download-1698015283896.png)


## Python


### Задание 1

Особенный номер – строка формата *\[2-4 цифры]\\\[2-5 цифр]*. Хороший номер - строка формата *\[4 цифры]\\\[5 цифр]*. Хороший номер можно получить из особенного дополнением нулей слева к обоим числам.

    Пример:
    17\234 => 0017\00234 

Напишите функцию, которая принимает на вход строку и для каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.

| Ввод  | Вывод |
| ------------- | ------------- |
| Адрес 5467\456. Номер  | 5467\00456  |
| 405\549  | 0405\00549  |


### Задание 2

На прямой дороге расположено *n* банкоматов. Было решено построить ещё *k* банкоматов для того, чтобы уменьшить расстояние между соседними банкоматами. 
На вход подаются натуральные числа *n* и *k*, а также *n* расстояний *L*, где *Li* – расстояние между банкоматами *i* и  *i+1*. Напишите функцию, которая добавляет *k* банкоматов таким образом, чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, и возвращает список новых расстояний между банкоматами.

| Ввод  | Вывод |
| ------------- | ------------- |
| 5 3  | 50  |
| 100  | 50  |
| 180  | 90  |
| 50  | 90  |
| 60  | 50  |
| 150  | 60  |
|   | 75  |
|   | 75  |


### Задание 3

Напишите функцию, которая принимает на вход список строк, состоящих из цифр, и возвращает максимальное возможное число, которое может получиться в результате конкатенации всех строк из этого списка.

| Ввод  | Вывод |
| ------------- | ------------- |
| 11  | 8923411005  |
| 234  |   |
| 005  |   |
| 89  |   |



## PostgreSQL


### Задание 1

Требуется составить расписание случайных проверок. Создайте оператор выбора, который выдаст *100* дат, начиная с текущей, при этом каждая дата отличается от предыдущей на *2-7* дней.

| Пример |
| ------------- |
| 25.02.2023  |
| 28.02.2023  |
| 04.03.2023  |
| 06.03.2023  |
| 13.03.2023  |
| 16.03.2023  |
| ...  |


### Задание 2

Требуется оценить эффективность продавцов. Создайте запрос, который вернёт количество и сумму продаж для каждого продавца, а также ранжирует продавцов по количеству продаж и по сумме продаж.

| | Таблица employee | |
| ------------- | ------------- | ------------- |
| ключ  | id  | int  |
|  | name  | varchar  |

|  | Таблица sales | |
| ------------- | ------------- | ------------- |
| ключ  | id  | int  |
| внешний ключ  | employee_id  | int  |
|  | price  | int  |

Результат запроса должен содержать столбцы **id**, **name** из таблицы **employee**, а также столбцы:
- **sales_c** - количество продаж, 
- **sales_rank_c** - ранг по количеству продаж, 
- **sales_s** - сумма продаж, 
- **sales_rank_s** -  ранг по сумме продаж.


### Задание 3

Имеется таблица денежных переводов **transfers**.

| Таблица transfers |  |
| ------------- | ------------- |
| from | int  |
| to  | int  |
| amount | int  |
| tdate | date  |

- **from** – номер аккаунта, с которого сделан перевод,
- **to** – номер аккаунта, на который сделан перевод,
- **amount** – сумма перевода,
- **tdate** – дата перевода.

Требуется создать оператор выбора, который для каждого аккаунта выведет периоды постоянства остатков (Дата конца последнего периода – 01.01.3000). Результат запроса должен содержать столбцы:
- **acc** – номер аккаунта,
- **dt_from** - начало периода,
- **dt_to** - конец периода,
- **balance** – остаток на счёте в данном периоде.

Таблица **transfers**

| from | to | amount | tdate |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 2 | 500 | 23.02.2023 |
| 2 | 3 | 300 | 01.03.2023 |
| 3 | 1 | 200 | 05.03.2023 |
| 1 | 3 | 400 | 05.04.2023 |

Результат запроса

| acc | dt_from | dt_to | balance |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 23.02.2023 | 05.03.2023 | -500 |
| 1 | 05.03.2023 | 05.04.2023 | -300 |
| 1 | 05.04.2023 | 01.01.3000 | -700 |
| 2 | 23.02.2023 | 01.03.2023 | 500 |
| 2 | 01.03.2023 | 01.01.3000 | 200 |
| 3 | 01.03.2023 | 05.03.2023 | 300 |
| 3 | 05.03.2023 | 05.04.2023 | 100 |
| 3 | 05.04.2023 | 01.01.3000 | 500 |



**!!GL!!HF!!**
 
