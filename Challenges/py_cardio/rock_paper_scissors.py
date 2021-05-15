#Reto 2 - Piedra, papel o tijera
#Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.
#Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

OPTIONS = ("rock", "paper", "scissors")
player1 = { "name": "player1", "value": ""}
player2 = { "name": "player2", "value": ""}

def get_nemesis_of(player):
    player_index = OPTIONS.index(player)
    nemesis_index = 0 if (player_index == len(OPTIONS) - 1) else player_index + 1
    return OPTIONS[nemesis_index]

def define_winner(player1, player2):
    nemesis = get_nemesis_of(player1["value"])

    return player2["name"] if player2["value"] == nemesis else player1["name"]

def player_select_option(player_name):
    player_option = ''
    index = 0

    while player_option not in OPTIONS:
        message = f"Hi {player_name}\nPlease, select" if index==0 else "It must be"
        player_option = input(f"{message} one of these options {OPTIONS}: ")
        index += 1

    return player_option

def run():
    player1["value"] = player_select_option(player1["name"])
    player2["value"] = player_select_option(player2["name"])

    winner = define_winner(player1, player2)
    print(f"the winner is: {winner}")

if __name__ == "__main__":
    run()
