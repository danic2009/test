# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = int(input("Введите, пожалуйста, номер месяца: "))
print('Вы ввели', user_input)
name_months = {1: "Январь 31 день",
               2: "Февраль 28 дней",
               3: "Март 31 день",
               4: "Апрерь 30 дней",
               5: "Май 31 день",
               6: "Июнь 30 дней",
               7: "Июль 31 день",
               8: "Август 31 день",
               9: "Сентябрь 30 дней",
               10: "Октябрь 31 день",
               11: "Ноябрь 30 днй",
               12: "Декабрь 31 день",
               }

if user_input in name_months:
    print(name_months.get(user_input))
else:
    print('Что то пошло не так')
