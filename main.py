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


def all_banks(money):
    out_list = '\n'
    for b, p in per_cent.items():
        profit = round(float(p / 100 * money), 2)
        profit_year = round(float(profit * 12), 2)
        bank_list = f'{b} ставка {str(p)}% ваша прибыль составит: ' \
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
    try:
        get_value = user_money.get()
        if get_value > 0:
            bank_info.pack()
            out_one_bank = percent_calc(get_value)
            button_all_banks.pack(pady=5)
            bank_info['text'] = str(out_one_bank)
        else:
            bank_info.pack()
            bank_info['text'] = 'Введите число больше 0'
    except TclError:
        bank_info.pack()
        bank_info['text'] = 'Введите число'


def all_banks_get():
    try:
        get_value = int(user_money.get())
        if get_value > 0:
            banks_info.pack()
            all_banks_func = all_banks(get_value)
            banks_info['text'] = str(all_banks_func)
        else:
            banks_info['text'] = 'Введите число больше 0'
    except TclError:
        banks_info['text'] = 'Введите число'


window = Tk()
window.title('Percent calculator')
window.geometry('700x400')
window['bg'] = '#01452c'

user_money = IntVar()
label = Label(window, text='Введите сумму', font='Consolas 25', bg='#01452c', fg='#b9e5ae')
entry = Entry(window, textvariable=user_money, font='Consolas 25', bg='#0a2619',
              fg='#b9e5ae', relief='solid', justify='center', )
button_ok = Button(command=get_user_money, text='Рассчитать',
            font='Consolas 20', bg='#01452c', fg='#01452c', relief='ridge', width=7, height=1,
                   justify='center')
bank_info = Label(window, font='Consolas 15', bg='#01452c',
              fg='#9dc20c', justify='center')
banks_info = Label(window, font='Consolas 13', bg='#01452c',
              fg='#9dc20c', justify='center')
button_all_banks = Button(command=all_banks_get, text='Все банки',
                          font='Consolas 20', bg='#01452c', fg='#01452c', relief='ridge',
                          width=7, height=1)

label.pack(pady=5)
entry.pack()
button_ok.pack(pady=10)
window.mainloop()

# percent_calc(user_money)
