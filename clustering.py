import random
import math

# data: iterable containing data instances
# k: how many clusters we need to find
# columns: list containing which columns to use for clustering
# centers: none = randomly, given = list of cluster centers
# n: given = max number of iterations
# eps: given = threshold for how much cluster centers have to move at least to continue

# 1. assign each data point to the nearest cluster center
# 2. compute new cluster center as mean of all data points assigned to each cluster

def normalisation(data, col) :
    # data[col][n]
    #     [grabs all info in a column][nth element of said column]
    # returns all data passed in
    colData = []
    count = 0
    while count < len(data[col]) :
        try :
            colData.append(float(data[col][count]))
        except :
            if data[col][count] == "low" or data[col][count] == "False" :
                colData.append(0)
            elif data[col][count] == "middle" or data[col][count] == "True" :
                colData.append(1)
            elif data[col][count] == "high" :
                colData.append(2)
        count += 1
    return colData
    
# DO NOT CHANGE THE FOLLOWING LINE
def lloyds(data, k, columns, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    clusterCenters = []
    
    for col in columns:
        print(normalisation(data, col))

    # for all cluster centers, set mean of the cluster to intial value
    # while totalDistance has not converged

    
    # This function has to return a list of k cluster centers (lists of floats of the same length as columns)
    return clusterCenters
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    pass

