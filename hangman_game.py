import os
from random import choice
import unicodedata 
import time

def run():

    #bienvenida
    print('''BIENVENIDOS AL JUEGO DEL AHORCADO
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/         
        
        Tienes 7 intentos para adivinar la palabra correcta, recuerda ingresar solo letras
        
        
    ''')
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
   
    words = []
    with open("archivos\data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip("\n"))


    word = choice(words)
    word = unicodedata.normalize("NFKD", word).encode("ascii","ignore").decode("ascii") #Quita las tildes de las palabras
    

    underscores = []
    for i in range (len(word)):
        underscores.append("_ ")

    usadas= []
    intentos= 1
    index = 0
    underscores_comp= []
    for char in word:
        underscores_comp.append(char + " ")
    while intentos<=7:
        print(HANGMANPICS[index])
        print (''.join(underscores))
        print("letras usadas: ",  ' , '.join(usadas))
        print("Intento actual: ", intentos)
        try :
            letter = str(input("Ingresa una letra:")).lower()
            if len(letter) >= 2 or letter.isalpha() == False:
                raise ValueError("Ingresa una letra valida")
        except ValueError as ve:
            print(ve)
            time.sleep(0.8)
            os.system("cls")
            
        else:
    
            if letter in usadas:
                print("Ya usaste esa letra")
            else:

                fallo = True
                usadas.append(letter)
                for i in range(len(word)):
                    if letter == word[i]:
                            underscores[i] = letter + ' '
                            os.system("cls")
                            print("Excelente, adivinaste una palabra")
                            fallo = False
                if fallo:
                    os.system("cls")
                    intentos +=1 
                    index +=1
            if underscores_comp == underscores:
                print(''.join(underscores))
                print("ganaste")
                
                break
                    
            if intentos == 8:
                print("perdiste")

                        
if __name__ == '__main__':
   
    
    run()
