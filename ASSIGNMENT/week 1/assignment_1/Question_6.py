"""
Q6. Ask number of games played in a tournament. 
    Ask the user number of games won and number of games loss. 
    Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
"""

total_matches : int = int(input("Total Number of matches = "))
won_matches : int = int(input("won Number of matches = "))
lost_matches : int = int(input("lost Number of matches = "))

tie_matches = total_matches - won_matches - lost_matches
print(f"{tie_matches= }\n{total_matches = }\n{lost_matches = }")
points = print(f"points = {won_matches * 4 - lost_matches * 2}  ")




