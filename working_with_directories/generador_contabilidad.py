# Usaremos este script para simular la caja de una semana
import os
from datetime import date, timedelta
from random import randint
from os import path
num_days = 7
start_date = date.today()

filename = path.join(os.getcwd(),'working_with_directories','contabilidad.txt')

with open(filename,'w') as file:

    for num_day in range(1,num_days):
        str_date = start_date.strftime('%Y%m%d')
        num_customers = randint(10, 20)
        start_date = start_date - timedelta(days=1)

        for num_customer in range(1,num_customers):
            random_amount = randint(999,9999)
            file.write('{}{}\n'.format(str_date,random_amount))




