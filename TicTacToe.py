def main():
   
    Replay = 'Y'
    while Replay == 'Y':
        Player = NextTurn('O')
        Spot = NumberGen()
        while not (ChickenDinner(Spot) or Stalemate(Spot)):
            BoardGen(Spot)
            MakeMove(Player, Spot)
            Player = NextTurn(Player)
        BoardGen(Spot)
        Challenge = input('Good Game! Want to play again?(Y/N): ')
        Replay = Challenge.upper()
    print('Thanks for playing!')

def NumberGen():
    Spot = []
    for Position in range(9):
        Spot.append(Position + 1)
    return Spot

def BoardGen(Spot):
    print()
    print(f'{Spot[0]}|{Spot[1]}|{Spot[2]}')
    print('-----')
    print(f'{Spot[3]}|{Spot[4]}|{Spot[5]}')
    print('-----')
    print(f'{Spot[6]}|{Spot[7]}|{Spot[8]}')
    print()

def NextTurn(Player):
    if Player == 'O':
        return 'X'
    elif Player == 'X':
        return 'O'

def MakeMove(Player, Spot):
    Position = int(input(f'{Player}\'s Turn: Pick a spot (1-9): '))
    Spot[Position-1] = Player

def ChickenDinner(Spot):
    return (Spot[0] == Spot[1] == Spot[2] or
            Spot[3] == Spot[4] == Spot[5] or
            Spot[6] == Spot[7] == Spot[8] or
            Spot[0] == Spot[3] == Spot[6] or
            Spot[1] == Spot[4] == Spot[7] or
            Spot[2] == Spot[5] == Spot[8] or
            Spot[0] == Spot[4] == Spot[8] or
            Spot[2] == Spot[4] == Spot[6])

def Stalemate(Spot):
    for Square in range(9):
        if Spot[Square] != "X" and Spot[Square] != "O":
            return False
    return True 
        
if __name__ == "__main__":
    main()