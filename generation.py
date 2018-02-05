import numpy as np
import pandas as pd

def generate():
    locations = pd.read_csv('locations.csv')

    centroid = (np.sum(locations.Lat) / len(locations.Lat), np.sum(locations.Long) / len(locations.Long))

    lat_normalized = []
    for i in locations.Lat:
        lat_normalized.append(locations.Lat - centroid[0])

    long_normalized = []
    for i in locations.Long:
        long_normalized.append(locations.Long - centroid[1])

    cov = np.cov(lat_normalized, long_normalized)
    cov[0][0]
    cov[0][315] # len/2

    # set this range to however many values you want to generate
    out = []
    for i in range(0,100):
        out.append(np.random.multivariate_normal(centroid, [[cov[0][0], cov[0][315]],[cov[1][0], cov[1][315]]]))

    return out

print(generate())