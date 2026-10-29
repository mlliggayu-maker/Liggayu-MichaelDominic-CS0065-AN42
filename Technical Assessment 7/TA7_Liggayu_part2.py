
# CS054 - Intelligent Systems
# K-means Clustering: Iteration 2 and 3

# Dataset
data = [2, 4, 10, 12, 3, 20, 30, 11, 25]

# Initial centroids from Iteration 1
M1 = 4
M2 = 11


# Function to perform one iteration
def kmeans_iteration(data, M1, M2, iteration):

    cluster1 = []
    cluster2 = []

    print(f"\nITERATION {iteration}")
    print("-" * 45)
    print(f"{'Datapoint':<12}{'D1':<10}{'D2':<10}Cluster")

    # Assign data points to the nearest centroid
    for point in data:
        D1 = abs(point - M1)
        D2 = abs(point - M2)

        if D1 <= D2:
            cluster1.append(point)
            cluster = "C1"
        else:
            cluster2.append(point)
            cluster = "C2"

        print(f"{point:<12}{D1:<10.2f}{D2:<10.2f}{cluster}")

    # Calculate new centroids
    new_M1 = sum(cluster1) / len(cluster1)
    new_M2 = sum(cluster2) / len(cluster2)

    print("\nC1 =", cluster1)
    print("C2 =", cluster2)
    print("New M1 =", round(new_M1, 2))
    print("New M2 =", round(new_M2, 2))

    return new_M1, new_M2


# Iteration 2
M1, M2 = kmeans_iteration(data, M1, M2, 2)

# Iteration 3
M1, M2 = kmeans_iteration(data, M1, M2, 3)
