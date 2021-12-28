def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingresa numeros positivos")
        divisors = [i for i in range(1,num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
    return "No se pudo ejecutar el programa "
def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Terminó el programa")
    except ValueError:
        print("Ingrese un numero valido")
       

if __name__ == '__main__':
    run()