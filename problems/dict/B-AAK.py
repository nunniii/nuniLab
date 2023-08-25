
player = {'health' : 100 , 'attack' : 10 , 'heal' : 10}
monster = {'health' : 120 , 'attack' : 12}
run = True

def guide():
    print("{1} : Atacar;")
    print("{2} : Curar;")
    print("{L} : Guide.")

def show_status():
    print("monster life : {}".format(monster['health']))
    print("Your life : {}".format(player['health']))

guide()
while run:
    command = input('give a command: . . . ')
    if command == str(1):
        monster['health'] -= player['attack']
        player['health'] -= monster['attack']
        show_status()
    if command == str(2):
        if player['health'] >= 90:
            pass
        else:
            player['health'] += player['heal']
        show_status()
    if command.lower() == 'l':
        guide()


    if monster['health'] <= 0:
        print("You win! =)")
        run = False
    if player['health'] <= 0:
        print("You lose. =(")
        run = False
