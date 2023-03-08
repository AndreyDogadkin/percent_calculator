from tkinter import *

# ____________________
# MAIN PROGRAM
# ____________________

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# user_money = ''


def get_sum():
    user_money = input('Введите сумму: ')
    return float(user_money)


def get_key(per_cent, value):
    for k, v in per_cent.items():
        if v == value:
            return k


def percent_calc(money=1):
    try:
        # money = get_sum()
        if money > 0:
            max_val = max(per_cent.values())
            bank = get_key(per_cent, max_val)
            profit = round(float(max_val / 100 * money), 2)
            profit_year = round(float(profit * 12), 2)
            return_inf = (f'\nЛучшее предложение от {bank}, ставка {max_val}%. \n'
                  f'Ваша прибыль в месяц составит: {profit} рублей.\n'
                  f'Ваша прибыль в год составит: {profit_year} рублей.\n')
            return return_inf
            all_banks(money)
            restart_calc()
        else:
            print('Введите число больше 0')
            percent_calc(user_money)
    except ValueError:
        print('Пожалуйста, введите число')
        percent_calc(user_money)


# def all_banks(money):
#     all_b = input('Нажмите [ENTER] для расчета по всем возможным банкам или [ЛЮБОЙ СИМВОЛ] для выхода.\n')
#     if all_b == '':
#         for b, p in per_cent.items():
#             profit = round(float(p / 100 * money), 2)
#             profit_year = round(float(profit * 12), 2)
#             bank_list = f'{b} ставка {str(p)} ваша прибыль составит: ' \
#                         f'{profit} рублей в месяц и {profit_year} рублей в год.'
#             return (f'{bank_list} \n')
#     else:
#         return ('')

def all_banks(money):
    out_list = ''
    for b, p in per_cent.items():
        profit = round(float(p / 100 * money), 2)
        profit_year = round(float(profit * 12), 2)
        bank_list = f'{b} ставка {str(p)} ваша прибыль составит: ' \
                    f'{profit} рублей в месяц и {profit_year} рублей в год.'
        out_list = out_list + bank_list + '\n'
    return out_list


def restart_calc():
    restart = input('Хотите посчитать другую сумму?\n'
                    'Введите [Y] - для ввода другой суммы или [ЛЮБОЙ ДРУГОЙ СИМВОЛ] для выхода.\n'
                    'Введите ответ: ')
    if restart.casefold() == 'y':
        percent_calc(user_money)
    else:
        print('Досвидания!')
# ____________
# GUI
# ____________
def get_user_money():
    get_value = user_money.get()
    out_one_bank = percent_calc(get_value)
    all_banks_get = all_banks(get_value)
    banks_info['text'] = out_one_bank, all_banks_get


window = Tk()
window.title('Percent calculator')
window.geometry('500x500')

user_money = IntVar(value=1)
all_banks_get = StringVar()
banks_info = IntVar()
label = Label(text='Введите сумму')
e = Entry(textvariable=user_money)
button_ok = Button(command=get_user_money, text='OK')
banks_info = Label(text=percent_calc)
button_all_banks = Button(command=all_banks, text='Все банки')

label.pack()
e.pack()
button_ok.pack()
banks_info.pack()
# button_all_banks.pack()


window.mainloop()

# percent_calc(user_money)
