import random

# List of 14 players and their corresponding strength
players = [
    ("Mario", 70), ("Monte", 80), ("Baraa", 75), ("Nabil", 85),
    ("Awad", 78), ("Safwat", 82), ("Ibrahim", 88), ("HamzeR", 74),
    ("Momen", 90), ("Arabiat", 77), ("Elias", 81), ("Abed", 79),
    ("Omar", 73), ("Mutaz", 76)
]

# Sort players by their strength (in descending order to balance stronger players first)
players.sort(key=lambda x: x[1], reverse=True)

# Initialize two teams
team_white = []
team_black = []

# Function to calculate the total strength of a team
def team_strength(team):
    return sum(player[1] for player in team)

# Distribute players alternately while considering random tolerance for each player's strength
for player in players:
    # Generate a random tolerance between -10% and +10% for the current player
    tolerance_factor = random.uniform(-0.10, 0.10)
    
    # Apply the tolerance to the player's strength
    adjusted_strength = player[1] * (1 + tolerance_factor)
    
    # Calculate the current strength difference between teams
    strength_white = team_strength(team_white)
    strength_black = team_strength(team_black)
    
    # Assign the player to the team with the lesser total strength
    if strength_white <= strength_black:
        team_white.append((player[0], adjusted_strength))
    else:
        team_black.append((player[0], adjusted_strength))

# Print the teams with adjusted strengths
print("Team White:")
for player in team_white:
    print(f"{player[0]:<15} {player[1]:.2f}")

print("\nTeam Black:")
for player in team_black:
    print(f"{player[0]:<15} {player[1]:.2f}")
