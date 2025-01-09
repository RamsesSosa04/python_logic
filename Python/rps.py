"""
    Determines the winner of a Rock-Paper-Scissors game.

    Args:
        p1: The choice of player 1 ("rock", "paper", or "scissors").
        p2: The choice of player 2 ("rock", "paper", or "scissors").

    Returns:
        "Player 1 won!", "Player 2 won!", or "Draw!" 
"""
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "scissors"):
         return "Player 1 won!"
    else:
        return "Player 2 won!"
print(rps("scissors", "paper"))
print(rps("rock", "rock"))