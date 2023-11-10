import pandas as pd
import matplotlib.pyplot as plt

# data is in the provided format
data = {
    'Owner': ['Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Adam Silver', 'Alan Smolinisky', 'Alan Smolinisky', 'Alex Meruelo', 'Alex Meruelo', 'Alex Meruelo', 'Amy Adams Strunk', 'Amy Adams Strunk', 'Amy Adams Strunk'],
    'Team': ['Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Commissioner', 'Los Angeles Dodgers', 'Los Angeles Dodgers', 'Arizona Coyotes', 'Arizona Coyotes', 'Arizona Coyotes', 'Tennessee Titans', 'Tennessee Titans', 'Tennessee Titans'],
    'League': ['NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'NBA', 'MLB', 'MLB', 'NHL', 'NHL', 'NHL', 'NFL', 'NFL', 'NFL'],
    'Recipient': ['WRIGHT 2016', 'BIDEN FOR PRESIDENT', 'CORY 2020', 'Kamala Harris for the People', 'Win The Era PAC', 'KOHL FOR CONGRESS', 'BETO FOR TEXAS', 'MONTANANS FOR TESTER', 'SERVE AMERICA PAC', 'ADAM SCHLEIFER FOR CONGRESS', 'ELISSA SLOTKIN FOR CONGRESS', 'DELGADO FOR CONGRESS', "Americans for Tomorrow's Future", 'Stand with Sanchez', 'All For Our Country Leadership PAC', 'Nevadans for Steven Horsford', 'Esmeralda Soria for Congress', 'Gridiron-PAC', 'Gridiron-PAC', 'Gridiron-PAC'],
    'Amount': [4000, 2800, 2700, 2700, 2700, 2000, 1000, 1000, 1000, 1000, 1000, 500, 10000, 2800, 5000, 2800, 500, 10000, 10000, 5000],
    'Election Year': [2016, 2020, 2020, 2020, 2020, 2018, 2018, 2018, 2018, 2020, 2020, 2018, 2020, 2020, 2020, 2020, 2020, 2016, 2018, 2020],
    'Party': ['Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'N/A', 'Democrat', 'Democrat', 'Democrat', 'Democrat', 'Bipartisan', 'Bipartisan', 'Bipartisan']
}

df = pd.DataFrame(data)

# Group the data by party and sum the contribution amounts
party_contribution = df.groupby('Party')['Amount'].sum().reset_index()

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(party_contribution['Amount'], labels=party_contribution['Party'], autopct='%1.1f%%', colors=['blue', 'red', 'green', 'gray', 'orange', 'purple'])
plt.title('Distribution of Contributions by Party')
plt.show()
