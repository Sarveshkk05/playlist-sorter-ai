import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the song data
df = pd.read_csv("../data/songs.csv")

# Select features for clustering
X = df[['tempo']]  # we'll add more features later

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Show the result
print(df[['name', 'tempo', 'cluster']])

# Optional: visualize
plt.scatter(df['tempo'], [0]*len(df), c=df['cluster'], cmap='viridis')
plt.xlabel("Tempo")
plt.title("Clustered Songs")
plt.show()
