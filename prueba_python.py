import pokepy
import random
import time

colaPokemon = []

def consultaEntrada():
    try:
        cantidadPokemones = input("Introducir cantidad de pokemones que ingresan: ")
        client = pokepy.V2Client()
        print "Pokemones entrando al gimnasio..."
        for i in range (0,cantidadPokemones):
            pokeID = random.randint(1,800)
            pokemon = client.get_pokemon(pokeID)
            colaPokemon.append([pokeID,str(pokemon.name)])
        colaPokemon.sort(key = lambda l:l[1], reverse=False)
        
    except:
        print "ERROR: Ingrese solo numeros"
        consultaEntrada()


def main():
    consultaEntrada()
    if len(colaPokemon)<18:
        for x in colaPokemon:
            print x
    else:
        for x in range(18):
            print colaPokemon[x]
        x+=1
        while True:
            time.sleep(1)
            if x < (len(colaPokemon)-1):
                x+=1
            else:
                x=0
            print colaPokemon[x]

if __name__ == "__main__":
    main()
