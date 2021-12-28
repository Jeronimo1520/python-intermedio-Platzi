def run():

   word = str(input("Ingrese la palabra: "))
   word = word.replace(' ', '').lower()

   if word == word[::-1]:
      print(True)
   else:
      print(False)
if __name__ == '__main__':
    run()