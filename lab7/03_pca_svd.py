import numpy as np

# Rows are observations; columns are features.
data = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1]
])

# PCA using covariance matrix and eigenvectors.
mean = np.mean(data, axis=0)
centered = data - mean
covariance = np.cov(centered, rowvar=False)
values, vectors = np.linalg.eigh(covariance)
order = np.argsort(values)[::-1]
components = vectors[:, order[:1]]
reduced = centered @ components

print("Principal component:\n", components)
print("PCA reduced data:\n", reduced)

# SVD factorization
u, singular_values, vt = np.linalg.svd(centered, full_matrices=False)
print("\nSingular values:", singular_values)
reconstructed = u @ np.diag(singular_values) @ vt
print("Reconstruction close to original:",
      np.allclose(centered, reconstructed))
