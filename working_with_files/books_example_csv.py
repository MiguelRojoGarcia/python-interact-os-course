import csv
import os
import random

FILE_PATH = os.path.join(os.getcwd(),'files','books.csv')

FIELDS = ['title','author','topic','num_pages','publisher']

def write_csv_file(data:dict,file_path:str):

    if os.path.exists(file_path) is False:
        with open(file_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(FIELDS)

    with open(file_path,'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([data['title'], data['author'], data['topic'], data['num_pages'], data['publisher']])

def write_csv_from_dict(data:list,file_path:str):

    if os.path.exists(file_path) is False:
        with open(file_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
            writer.writeheader()

    with open(file_path,'a') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=FIELDS)
        writer.writerows(data)

def print_cvs_file(file_path:str):
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            title , author , topic , num_pages , publisher = row
            print(title , author , topic , num_pages , publisher)

data = [
    {'title':'My book 1.0','author':'Miguel Rojo','topic':'Python course','num_pages': random.randint(200,400),'publisher':'Me'}
]

write_csv_file(data[0],FILE_PATH)
write_csv_from_dict(data,FILE_PATH)
print_cvs_file(FILE_PATH)




