
def main():
    operation = ''
    count_operation = 0
    account_sum = 0

    print('Вас приветствует банкомат')

    while operation != 'Q':
        print(f'На вашем счете: {account_sum} у.е.')
        print('Чтобы положить денег введите + ')
        print('Чтобы снять денег введите - ')
        print('Чтобы выйти введите Q ')
        operation = input('Ввелите операцию: ')
        if account_sum > 5000000:
            account_sum = account_sum*0.9
        if len(operation) != 0 and (operation == '+' or operation == '-'):
            count_operation += 1
        else:
            continue
        input_sum = float(input('Введите сумму кратную 50: '))
        if input_sum % 50 != 0:
            continue
        account_sum = controller(operation, input_sum, account_sum)
        if count_operation == 3:
            account_sum = account_sum = account_sum*1.03
            count_operation = 0


def controller(operation, input_sum, account_sum):
    if operation == '+':
        account_sum = account_plus(input_sum, account_sum)
    elif operation == '-':
        account_sum = account_minus(input_sum, account_sum)
    
    return account_sum


def account_plus(input_sum, account_sum):
    account_sum += input_sum
    return account_sum


def account_minus(input_sum, account_sum):
    if check_sum(input_sum, account_sum):
        if input_sum*0.015 < 30:
            account_sum -= input_sum + 30
        elif input_sum*0.015 > 600:
            account_sum -= input_sum + 600
        else:
            account_sum -= input_sum * 1.015
    else:
        print('Недостаточно средств для выполнения операции')
    return account_sum


def check_sum(input_sum, account_sum):
    if input_sum*0.015 < 30 and input_sum+30 > account_sum:
        return False
    elif input_sum*0.015 > 600 and input_sum+600 > account_sum:
        return False
    elif input_sum*1.015 > account_sum:
        return False
    else:
        return True

main()
