import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    data = np.asarray(data, dtype=float)

    # Standardization: (x - mean) / std
    mean = data.mean(axis=0)
    std = data.std(axis=0)
    standardized = (data - mean) / std

    # Min-Max normalization: (x - min) / (max - min)
    min_val = data.min(axis=0)
    max_val = data.max(axis=0)
    normalized = (data - min_val) / (max_val - min_val)

    standardized = np.round(standardized, 4)
    normalized = np.round(normalized, 4)

    # print(standardized, normalized)
    return standardized, normalized