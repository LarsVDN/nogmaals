repeatBack = input("Voer wat in \nQuit om programma te sluiten: ")

empty = None
nummer = 1

while empty != 'quit':
    empty = input(repeatBack)
    print(empty, nummer)
    nummer=nummer+1
