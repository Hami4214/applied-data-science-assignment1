import matplotlib.pyplot as plt
import pandas as pd

#  data is in a DataFrame
data = {
    'rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'prev_rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Manchester City', 'Bayern Munich', 'Barcelona', 'Real Madrid', 'Liverpool', 'Arsenal', 'Newcastle', 'Napoli', 'Borussia Dortmund', 'Brighton and Hove Albion'],
    'league': ['Barclays Premier League', 'German Bundesliga', 'Spanish Primera Division', 'Spanish Primera Division', 'Barclays Premier League', 'Barclays Premier League', 'Barclays Premier League', 'Italy Serie A', 'German Bundesliga', 'Barclays Premier League'],
    'off': [2.79, 3.04, 2.45, 2.56, 2.63, 2.53, 2.38, 2.3, 2.83, 2.47],
    'def': [0.28, 0.68, 0.43, 0.6, 0.67, 0.61, 0.53, 0.51, 0.84, 0.73],
    'spi': [92, 87.66, 86.4, 84.41, 83.93, 83.92, 83.7, 83.25, 82.91, 80.88]
}

df = pd.DataFrame(data)

# Sort the DataFrame by rank
df = df.sort_values(by='rank')

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.35
bar_positions = range(1, 11)

ax.bar(bar_positions, df['off'], bar_width, label='Offense')
ax.bar([p + bar_width for p in bar_positions], df['def'], bar_width, label='Defense')

ax.set_xlabel('Team Rank')
ax.set_ylabel('Performance')
ax.set_title('Team Performance Rankings')
ax.set_xticks([p + bar_width / 2 for p in bar_positions])
ax.set_xticklabels(df['name'])
ax.legend()

plt.show()
