#from https://docs.google.com/document/d/1_248kH-w16kv-tCte_WJfQph6xr1jqGQpsm5I_mqMi8/edit?usp=sharing

items = {
    'int_item': 10,
    'comp_item': 18,
    'item_2': True,
    'item_3': False,
    'item_4': 0,
    'item_5': 1
}

currencies_items = {
    'usd': 1,
    'eur': 0.86,
    'uah': 26.23,
    'chf': 0.91,
    'rub': 71.88,
    'byn': 2.46
}

mult_int = items.get('int_item') * 2
if mult_int > items.get('comp_item'):
    print('Переменная mult_int больше', items.get('comp_item'))

div_int = items.get('int_item') / 2
if div_int < items.get('comp_item'):
    print('Переменная div_int меньше', items.get('comp_item'))

item_1 = items.get('int_item') + 10
if item_1 < items.get('comp_item'):
    print('Переменная item_1 меньше', items.get('comp_item'))
else:
    print('Переменная item_1 больше или равна', items.get('comp_item'))

if items.get('item_2'):
    print('Переменная item_2 = ', items.get('item_2'))
else:
    print('Переменная item_2 = ', items.get('item_3'))

if items.get('item_3'):
    print('Переменная item_3 = ', items.get('item_2'))
else:
    print('Переменная item_3 = ', items.get('item_3'))

if items.get('item_5'):
    print('Переменная item_3 = ', items.get('item_5'))
else:
    print('Переменная item_3 = ', items.get('item_4'))

if items.get('item_4'):
    print('Переменная item_4 =', items.get('item_5'))
else:
    print('Переменная item_4 =', items.get('item_4'))

currency_convertor = items.get('item_2')
if currency_convertor:
    user_answer = input('Введите валюту (usd, eur, uah, chf, rub или byn): ')
    while user_answer not in currencies_items.keys():
        print('Введите корректную валюту')
        user_answer = input('Введите валюту (usd, eur, uah, chf, rub или byn): ')
    cur_item = currencies_items.get(user_answer, 'Unknown currency')
    while True:
        try:
            user_answer2 = float(input('Введите количество валюты: '))
            break
        except ValueError:
            print('Введите корректное количество валюты')
    target_currency_amount = float(user_answer2)
    currency_result = round(target_currency_amount / cur_item, 2)
    print(target_currency_amount, user_answer, '=', currency_result, 'usd')
else:
    print('Переменная currency_convertor = ', items.get('item_3'))
