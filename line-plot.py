import matplotlib.pyplot as plt

# Data for the selected teams ("RII" and "STP")
teams = ["RII", "STP"]
elo_data = {
    "RII": [1503.947, 1516.108, 1542.135],
    "STP": [1300, 1287.838, 0],  # Assuming the third value is the post-season Elo rating
}

# Matchups (assuming three matchups)
matchups = ["Matchup 1", "Matchup 2", "Matchup 3"]

# Plotting the Elo ratings over time
plt.figure(figsize=(10, 6))

for team in teams:
    plt.plot(matchups, elo_data[team], label=team, marker='o')

plt.title('Elo Ratings Over Time for Teams "RII" and "STP"')
plt.xlabel('Matchups')
plt.ylabel('Elo Rating')
plt.legend()
plt.grid(True)
plt.show()
