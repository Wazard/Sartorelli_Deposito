import pandas as pd
import numpy as np
import __init__
from base_data_handler import BaseDataHandler


class DataHandler(BaseDataHandler):
    
    def print_data_type(self) -> None:
        self.df.info()

    def get_df_types(self) -> pd.Series:
        return self.df.dtypes

    def get_numerical_cols_mean(self) -> pd.Series:
        df_numeric = self.df.select_dtypes(include=[np.number])
        return df_numeric.mean()
    
    def get_numerical_cols_median(self) -> pd.Series:
        df_numeric = self.df.select_dtypes(include=[np.number])
        return df_numeric.median()

    def get_numerical_cols_std(self) -> pd.Series:
        df_numeric = self.df.select_dtypes(include=[np.number])
        return df_numeric.std()

    def add_age_category(self) -> bool | tuple[bool, Exception]:
        return self.try_add_col('Age Category', lambda row: 'Senior' if row['Age'] > 65 else ('Adult' if row['Age']>18 else 'Young'))


# Initialize handler with file path
handler = DataHandler("./train.csv")

# Show first 3 rows
print("First 3 rows:\n", handler.get_lines(3))

# Show last 2 rows
print("Last 2 rows:\n", handler.get_lines(-2))

# Print schema info
print("\nData types:")
handler.print_data_type()

# Get dtypes as Series
print("\nColumn dtypes:\n", handler.get_df_types())

# Numerical stats
print("\nMeans:\n", handler.get_numerical_cols_mean())
print("\nMedians:\n", handler.get_numerical_cols_median())
print("\nStandard deviations:\n", handler.get_numerical_cols_std())

# Remove duplicates
result = handler.try_remove_duplicates()
print("\nRemove duplicates result:", result)

# Fill Nan
result = handler.try_fill_nan()
print("\nFill Nan:", result)

# Add age category
result = handler.add_age_category()
print("\nAdd age category result:", result)
print(handler.df)

# Save to new file
result = handler.try_save()
print("\nSave result:", result)
