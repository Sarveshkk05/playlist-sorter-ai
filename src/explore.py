import pandas as pd

# Load the CSV file
df = pd.read_csv("../data/songs.csv")

# Print the first few rows
print("🎵 Top songs:")
print(df.head())

# Get unique genres
print("\n🎶 Genres:")
print(df['genre'].unique())

# Filter songs by mood
print("\n😌 Calm Songs:")
print(df[df['mood'] == 'calm'])

# Sort songs by tempo
print("\n🚀 Songs sorted by tempo:")
print(df.sort_values(by='tempo', ascending=False))
