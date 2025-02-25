# k mean clustering
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
# Replace 'sales_data_sample.csv' with the name of your uploaded file in Replit
data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Select relevant features for clustering
features = data[['QUANTITYORDERED', 'PRICEEACH', 'SALES']].copy()

# Handle missing values
features = features.fillna(features.mean())

# Normalize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # Change n_clusters if needed
kmeans.fit(scaled_features)

# Add cluster labels to the original data
data['Cluster'] = kmeans.labels_

# Visualize the clusters 
plt.figure(figsize=(8, 6))
plt.scatter(features['QUANTITYORDERED'], features['SALES'], c=data['Cluster'], cmap='viridis')
plt.title('Sales vs Quantity Ordered (Clustered)')
plt.xlabel('Quantity Ordered')
plt.ylabel('Sales')
plt.colorbar(label='Cluster')
plt.show()

# Save the clustered data to a new CSV file
data.to_csv('clustered_sales_data.csv', index=False)
print("Clustered data saved to 'clustered_sales_data.csv'.")
