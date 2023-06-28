command= ""
startted = False
while True :
    command = input('>').lower()
    if command == 'start':
        if startted :
            print("Car is already startted ")
        else :
          startted = True
          print('Car started.... ')
    elif command== 'stop':
        if not startted :
            print("Car is already stopped ")
        else :
            startted = False
            print("Car stopped!")
    elif command== 'help':
        print('''
star - to start the car
stop - to stop the car
quit - to quit the game 
        ''')
    elif command==  'quit' :
        break
    else :
        print("Sorry i don't understand that! ")
