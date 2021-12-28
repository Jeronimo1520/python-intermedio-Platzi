def run():
   
#    dict = {}
#    for i in range(1,101):
#        if i % 3 != 0 :
#             dict[i] = i**3
#    print(dict)

   dict = {i: i**3 for i in range(1,101) if  i % 3 != 0 }

if __name__ == '__main__':
    run()