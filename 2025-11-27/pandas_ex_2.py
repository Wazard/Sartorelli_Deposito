import pandas as pd
import numpy as np
import __init__
from base_data_handler import BaseDataHandler


def generate_sales_data(n: int = 50, seed: int = 42) -> pd.DataFrame:
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

    # Add computed column: Total Sales = Quantity × UnitPrice × (1 - Discount)
    df["Total Sales"] = df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

    return df

class SalesDataHandler(BaseDataHandler):

    def try_get_sales_by_product(self) -> tuple[bool, any]:
        return self.try_get_groupby('Product', 'Total Sales')

    def add_total_sales(self) -> bool | tuple[bool, Exception]:
        return self.try_add_col('Total Sales', lambda row: row['Quantity']*row['UnitPrice'])
    
    def try_filter_sales_greater_than(self, n:float) -> tuple[bool, any]:
        try:
            new_df = self.df[self.df['Total Sales']>n]
        except Exception as e:
            return False, e
        return True, new_df

    def try_order_by_sales(self) -> tuple[bool, any]:
        return self.try_order_by(cols='Total Sales', ascending=False)

    def try_get_sales_by_city(self) -> tuple[bool, any]:
        return self.try_get_groupby('City','Total Sales')

    def get_total_sales_pivot(self) -> pd.DataFrame:
        return self.get_pivot(values='Total Sales', index='Product')
""" 
# --- Create a synthetic sales dataset ---
df = pd.DataFrame(generate_sales_data())

# --- Use DataHandler ---
handler = SalesDataHandler(df=df)

# 1. Preview first rows
print("Initial dataset:")
handler.print_dataframe()

# 2. Add a computed column: Total Sales
success, err = handler.add_total_sales()
if not success:
    print("Error adding Total Sales:", err)

print("\nDataset with Total Sales:")
print(handler.get_lines())

# 3. Filter rows where Total Sales > 5000
success, result = handler.try_filter_sales_greater_than(5000)
if success:
    print("\nSales greater than 5000:")
    print(result)
else:
    print("Error filtering:", result)

# 4. Order by Total Sales
success, err = handler.try_order_by_sales()
if not success:
    print("Error ordering:", err)

print("\nOrdered by Total Sales:")
print(handler.get_lines())

# 5. Group by Product
success, grouped = handler.try_get_sales_by_product()
if success:
    print("\nGrouped by Product:")
    print(grouped.sum())   # aggregate example
else:
    print("Error grouping:", grouped)

# 6. Group by City
success, grouped = handler.try_get_sales_by_city()
if success:
    print("\nGrouped by City:")
    print(grouped.sum())
else:
    print("Error grouping:", grouped)

# 7. Pivot table
result = handler.get_total_sales_pivot()
print("\nPivot Table: mean sales per product")
print(result)
"""