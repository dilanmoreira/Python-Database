from Database.Library.Interface import *
from Database.Library.File import *
from time import sleep

arq = 'pythonproject.txt'

if not arqExist(arq):
    createArq(arq)

while True:
    answer = menu(['Registered people', 'Register a new person', 'Exit the system'])
    if answer == 1:
        lerArquivo(arq)
    elif answer == 2:
        header('New record')
        name = str(input('Name: '))
        age = readInt('Age: ')
        cadastrar(arq, name, age)
    elif answer == 3:
        header('Exiting to the system...')
        break
    else:
        print('\033[31mERROR! ENTER AN AVAILABLE OPTION.\033[M')
    sleep(2)
