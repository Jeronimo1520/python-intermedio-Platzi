import os
from random import choice

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
        
        Tienes 7 intentos para adivinar la palabra correcta
        
        
    ''') 

    #pics para los intentos
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

    #lista donde se almacenaran las palabras
    words = []
    #abriendo el archivo y llenando la lista
    with open("archivos\data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip("\n"))
    # se elige la palabra de manera aleatoria
    word = choice(words)
    
    #INTENTOS Y JUEGO
    underscores = []
    for i in range (len(word)):
        underscores.append("_ ")

    repetidas = []
    intentos= 1
    while intentos<=7:
        index = 0
        print (''.join(underscores))
        letter = str(input("Ingresa una letra: ")).lower()
        if len(letter) >= 2 or letter.isalpha() == False:
            print("Ingrese una letra valida y solo una")
            intentos= intentos

        elif letter in repetidas:
            print("Ya usaste esa letra")
            intentos=intentos
            
        else:
            repetidas.append(letter)
            for i in range(len(word)):
                if letter == word[i]:
                        underscores[i] = letter + ' '
                        intentos= intentos
                else:
                    os.system ("cls")
            index +=1
        print(HANGMANPICS[index])
        intentos +=1

        if intentos == 8:
            print("perdiste")
        elif word == (''.join(underscores)):
            print("ganaste")
                        
if __name__ == '__main__':
    run()