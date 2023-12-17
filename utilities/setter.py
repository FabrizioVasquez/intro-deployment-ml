import os 
from base64 import b64decode # usamos esto que vamos a usar el secret que estara en service acount key, esta codeado en 64 y debemos decodearlo

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open ('path.json','w') as json_file:
        json_file.write(b64decode(key).decode()) # Entonces aqui key es un string que se devuelve en bytes y luego decode a string

    print(os.path.realpath('path.json'))

if __name__ == '__main__':
    main()
