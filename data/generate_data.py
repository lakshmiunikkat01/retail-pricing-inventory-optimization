import pandas as pd
import numpy as np

def generate_data(n=5, seed=42):
    np.random.seed(seed)

    return pd.DataFrame({
        "product": [f"P{i}" for i in range(n)],
        "demand": np.random.randint(100, 300, n),
        "holding_cost": np.random.uniform(2, 5, n),
        "ordering_cost": np.random.uniform(1, 3, n),
        "min_price": np.random.uniform(20, 30, n),
        "max_price": np.random.uniform(40, 60, n),
        "storage": np.random.uniform(1, 3, n)
    })
