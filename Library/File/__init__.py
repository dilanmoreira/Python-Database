from Database.Library.Interface import *

def arqExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArq(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('ERROR!')
    else:
        print(f'File {name} created successfully.')

def lerArquivo(name):
    try:
        a = open(name, 'rt')
    except:
        print('File error!')
    else:
        header('Registered people')
        for linha in a:
            data = linha.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years old')
    finally:
        a.close()

def cadastrar(arq, name='Unknown', age='0'):
    try:
        a = open(arq, 'at')
    except:
        print('There was an error.')
    else:
        try:
            a.write(f'{name}; {age}\n')
        except:
            print('There was an error.')
        else:
            print(f'New record {name} added.')
            a.close()

