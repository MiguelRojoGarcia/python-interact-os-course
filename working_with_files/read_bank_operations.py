from entities.bank_operation.domain.bank_operation import BankOperation

sizes = {'BANK_ACCOUNT':0,'AMOUNT':20,'DATETIME':30}

#Read file example

with open('files/bank-example.txt') as my_file:

    for index,line in enumerate(my_file.readlines()):

        stripped_line = line.strip()

        bank_account = stripped_line[0:sizes['AMOUNT']]

        amount = int(stripped_line[sizes['AMOUNT']:sizes['DATETIME']]) / 100

        date_time = stripped_line[sizes['DATETIME']:]

        bank_operation = BankOperation(bank_account,amount,date_time)

        print('{}'.format(bank_operation ))