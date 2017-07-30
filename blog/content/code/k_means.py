import numpy as np
import pandas as pd
#from pydataset import data
import seaborn as sns # Nice plots
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from scipy.spatial.distance import cdist

#faith = data('faithful').to_csv('old_faithful.csv') # Alternatively you can download the dataset from the internet
df = pd.read_csv('old_faithful.csv')
df.round(2) # Round all data to two decimal places
df.drop(df.columns[0], axis=1, inplace=True) # The first column is garbage, drop it, we now have: 'eruptions' and 'waiting'
df = (df - df.mean()) / df.std() # Standarize the data (make each variable zero mean and unit standard deviation)
df.plot(x='eruptions', y='waiting', kind='scatter')


"""
We have a dataset of N observations of a D-dimensional variable (D=2, eruptions and waiting), we want to
partition de data in K clusters
each cluster will have a center mu_k (also D-dimensional).
Now every datapoint should be assigned to one of the clusters.
Our goal is to both assign each data point to the closer (sum of squares) cluster and choose the centers mu_k of the clusters.
we define a matrix labels which tell us to which cluster is each point assigned
"""
# Error function
def J(distances, labels):
    error = 0
    for n, distance in enumerate(distances):
        # we could have made it even more vectorial, but it's not worth it
        error += distance[labels[n]]
    return error

X = df.as_matrix()
N = X.shape[0]
K = 2
D = X.shape[1] # number of dimensions of the problem
# Initialize random centers, you can do it randomly if you want to
# MU = np.array([[np.random.uniform(low=df[df.columns[d]].min(), high=df[df.columns[d]].max()) for d in range(D)] for k in range(K)])
MU = np.array([[-2.0, 2.0], [1.5, -2.5]])
max_iterations = 6

for _ in range(max_iterations):
    # Calculate distance from each datapoint to each cluster center
    squared_distances = cdist(X, MU, 'sqeuclidean') # NxK matrix
    #distances = np.linalg.norm(X[:,None,:] - MU[None,:,:], axis=2)**2 #  X[:,None,:] - MU[None,:,:] -> (NxKxD). TODO: Link broadcasting tutorial https://stackoverflow.com/questions/32171917/copy-2d-array-into-3rd-dimension-n-times-python
    labels = np.argmin(squared_distances, axis=1) # Nx1 and each value tell us which index is associated which each datapoint

    # calculate the means of all datapoints assigned to each cluster (Kx1)
    for k in range(K):
        # points_of_cluster k -> X[labels == k]
        # update centers
        MU[k] = np.mean(X[labels == k], axis=0)
    # Error should be decreasing
    print("Current error: {0}".format(J(squared_distances, labels)))
    # end of iteration, now we have labels of which cluster the datapoint is associated and the new cluster locations (MU)


df = df.assign(labels=labels)
df.plot.scatter(x='eruptions', y='waiting',c='labels', colormap=cmx.coolwarm, colorbar=False)

plt.scatter(MU[:, 0], MU[:, 1], marker='o', linewidths=5, color=['c', '#DA0AF0'])
plt.show()
