import argparse
import math


parser = argparse.ArgumentParser(prog = 'Loan Calculator')
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()


def differentiated_payments():
    principal = float(args.principal)
    interest = float(args.interest)
    periods = int(args.periods)
    monthly_i = ((interest / 100) / 12)
    m = 1
    diff_count = 0
    while m <= periods:
        diff_payment = math.ceil((principal / periods) + monthly_i * (principal - ((principal * (m - 1)) / periods)))
        print(f'Month {m}: payment is {diff_payment}')
        diff_count +=diff_payment
        m += 1
    print(f'\n\nOverpayment = {int(diff_count - principal)}')


def annuity_payment():
    num_periods = int(args.periods)
    principal_amount = float(args.principal)
    interest = float(args.interest)
    monthly_i = ((interest / 100) / 12)
    a_payment = math.ceil(principal_amount * ((monthly_i * (1 + monthly_i)**num_periods) /
                                         ((1 + monthly_i)**num_periods - 1)))
    print(f'Your monthly payment = {a_payment}!')
    print(f'Overpayment = {int((a_payment * num_periods) - principal_amount)}')
    
    
    
def num_payments():
    principal_amount = float(args.principal)
    a_payment = float(args.payment)
    interest = float(args.interest)    
    monthly_i = ((interest / 100) / 12)
    x = (a_payment / (a_payment - (monthly_i * principal_amount)))
    num_months = math.ceil(math.log(x, 1 + monthly_i))
    years = num_months // 12
    months = num_months % 12
    if num_months % 12 == 0:
        print(f'It will take {years} years to repay this loan!')
    elif years == 0:
        print(f'It will take {months} months to repay this loan!')
    else:
        print(f'It will take {years} years and {months} months to repay this loan!')
    print(f'Overpayment = {int((a_payment * num_months) - principal_amount)}')


def loan_principal():
    num_periods = int(args.periods)
    interest = float(args.interest)
    a_payment = float(args.payment)
    monthly_i = ((interest / 100) / 12)
    l_principal = int(round(a_payment / ((monthly_i * (1 + monthly_i)**num_periods) /
                                         ((1 + monthly_i)**num_periods - 1)), 0))
    print(f'Your loan principal = {l_principal}!')
    print(f'Overpayment = {int((a_payment * num_periods) - l_principal)}')


_list_ = [args.periods,args.interest,args.payment,args.principal,args.type]
if _list_.count(None) >= 2:
    print('Incorrect parameters 0')
elif args.interest == None:
    print('Incorrect parameters 1')
elif args.payment != None and args.type == 'diff':
    print('Incorrect parameters 2')
elif args.type != 'annuity' and args.type != 'diff' and args.type == None:
    print('Incorrect parameters 3')
elif args.type == 'diff':
    differentiated_payments()
elif args.type == 'annuity':
    if args.payment == None:
        annuity_payment()
    elif args.periods == None:
        num_payments()
    else:
        loan_principal()
else:
    print('HELP')
