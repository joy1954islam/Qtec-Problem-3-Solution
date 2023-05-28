from scipy.spatial.distance import pdist, squareform
import pandas as pd
from python_tsp.exact import solve_tsp_dynamic_programming

data = [
    [1, 23.8728568, 90.3984184, "Uttara Branch"],
    [2, 23.8513998, 90.3944536, "City Bank Airport"],
    [3, 23.8330429, 90.4092871, "City Bank Nikunja"],
    [4, 23.8679743, 90.3840879, "City Bank Beside Uttara Diagnostic"],
    [5, 23.8248293, 90.3551134, "City Bank Mirpur 12"],
    [6, 23.827149, 90.4106238, "City Bank Le Meridien"],
    [7, 23.8629078, 90.3816318, "City Bank Shaheed Sarani"],
    [8, 23.8673789, 90.429412, "City Bank Narayanganj"],
    [9, 23.8248938, 90.3549467, "City Bank Pallabi"],
    [10, 23.813316, 90.4147498, "City Bank JFP"]
]

df = pd.DataFrame(data, columns=["ID", "Latitude", "Longitude", "Address"])

# Calculate distance matrix using coordinates
dist_matrix = squareform(pdist(df[['Latitude', 'Longitude']].values))

# Solve TSP using dynamic programming
optimal_permutation, distance = solve_tsp_dynamic_programming(dist_matrix)

# Generate optimal route
optimal_route = df.iloc[optimal_permutation]["Address"].tolist()
optimal_route.append(optimal_route[0])

print("Optimal Route: {}".format(" ---> ".join(optimal_route)))
