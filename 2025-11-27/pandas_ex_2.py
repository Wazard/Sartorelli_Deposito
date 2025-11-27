import pandas as pd
import numpy as np
import __init__
from base_data_handler import BaseDataHandler

import pandas as pd
import numpy as np

def generate_sales_data(n: int = 300, seed: int = 42) -> pd.DataFrame:
    """
    Generate a synthetic sales dataset with n rows.
    Includes NaN values in Quantity and UnitPrice (~10%).
    
    Args:
        n (int): Number of rows to generate (default 300).
        seed (int): Random seed for reproducibility.
    
    Returns:
        pd.DataFrame: Synthetic sales dataset.
    """
    np.random.seed(seed)

    # Possible values
    customers = [f"Customer_{i}" for i in range(1, 51)]   # 50 customers
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
    cities = ["Turin", "Milan", "Rome", "Naples", "Venice"]

    # Build dataset
    data = {
        "Customer": np.random.choice(customers, size=n),
        "City": np.random.choice(cities, size=n),
        "Product": np.random.choice(products, size=n),
        "Quantity": np.random.randint(1, 10, size=n).astype(float),
        "UnitPrice": np.random.uniform(50, 2000, size=n),
        "Discount": np.random.choice([0, 0.05, 0.1, 0.2], size=n)
    }

    df = pd.DataFrame(data)

    # Introduce NaN values randomly (~10% of Quantity and UnitPrice)
    for col in ["Quantity", "UnitPrice"]:
        nan_indices = np.random.choice(df.index, size=int(0.1*n), replace=False)
        df.loc[nan_indices, col] = np.nan

    # Add computed column: Total = Quantity × UnitPrice × (1 - Discount)
    df["Total"] = df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

    return df

class DataHandler(BaseDataHandler):

    def get_sales_by_product(self) -> pd.Series:
        return self.df.groupby('Product')['Sales'].sum()

    def add_total_sales(self) -> bool | tuple[bool, Exception]:
        return self.try_add_col('Total Sales', lambda row: row['Quantity']*row['Price'])
    
    


