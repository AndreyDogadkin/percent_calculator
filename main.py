per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
user_money = ''


def get_sum():
    user_money = input('Введите сумму: ')
    return float(user_money)


def get_key(per_cent, value):
    for k, v in per_cent.items():
        if v == value:
            return k


def percent_calc(money=1):
    try:
        money = get_sum()
        if money > 0:
            max_val = max(per_cent.values())
            bank = get_key(per_cent, max_val)
            profit = round(float(max_val / 100 * money), 2)
            profit_year = round(float(profit * 12), 2)
            print(f'\nЛучшее предложение от {bank}, ставка {max_val}%. \n'
                  f'Ваша прибыль в месяц составит: {profit} рублей.\n'
                  f'Ваша прибыль в год составит: {profit_year} рублей.\n')
            all_banks(money)
            restart_calc()
        else:
            print('Введите число больше 0')
            percent_calc(user_money)
    except ValueError:
        print('Пожалуйста, введите число')
        percent_calc(user_money)


def all_banks(money):
    all_b = input('Нажмите [ENTER] для расчета по всем возможным банкам или [ЛЮБОЙ СИМВОЛ] для выхода.\n')
    if all_b == '':
        for b, p in per_cent.items():
            profit = round(float(p / 100 * money), 2)
            profit_year = round(float(profit * 12), 2)
            bank_list = f'{b} ставка {str(p)} ваша прибыль составит: ' \
                        f'{profit} рублей в месяц и {profit_year} рублей в год.'
            print(f'{bank_list} \n')
    else:
        print('')


def restart_calc():
    restart = input('Хотите посчитать другую сумму?\n'
                    'Введите [Y] - для ввода другой суммы или [ЛЮБОЙ ДРУГОЙ СИМВОЛ] для выхода.\n'
                    'Введите ответ: ')
    if restart.casefold() == 'y':
        percent_calc(user_money)
    else:
        print('Досвидания!')


percent_calc(user_money)

