import os

"""
Crear un algoritmo que lea un fichero de texto secuencial que contiene la contabilidad de X dias de un pequeño
comercio y distribuya cada carpeta las fechas de dichas operaciones en un fichero de texto llamado total.txt que contendrá la 
recaudación total de ese día

NOTA : Se puede ejecutar el script generador_contabilidad.py para simular la contabilidad de x dias

"""

current_path = os.path.join(os.getcwd(),'working_with_directories')

accounting_file = [file for file in os.listdir(current_path) if file.lower().__contains__('.txt')]

if len(accounting_file) > 0:

    accounting_file = accounting_file[0]

    file_path = os.path.join(current_path,accounting_file)

    # Leemos el fichero linea por linea
    with open(file_path) as file:

        for line in file.readlines():
            date = line[:8]
            amount = int(line[8:]) / 100

            date_path = os.path.join(current_path,date)

            # Por cada dia , creamos una subcarpeta
            if os.path.exists(date_path) is False:
                os.mkdir(date_path)

            total_file_path = os.path.join(date_path, 'total.txt')

            if os.path.exists(total_file_path) and os.path.getsize(total_file_path) > 0:
                with open(total_file_path, 'r') as total_file:
                        amount = amount + float(total_file.readline())

            with open(total_file_path, 'w') as total_file:
                    total_file.write('{}'.format(round(amount,2)))













else:
    print('Error any file was processed')


