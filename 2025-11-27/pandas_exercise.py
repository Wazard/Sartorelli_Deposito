import pandas as pd
import numpy as np
import __init__


class DataHandler():
    def __init__(self, path:str):
        
        self.file_path = path
        
        self.update_df()

    def update_df(self) -> None:
        self.df = pd.read_csv(self.file_path)
    
    def get_lines(self, amount=5) -> pd.DataFrame:
        return self.df.head(amount) if amount > 0 else self.df.tail(amount)
    
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

    def try_remove_duplicates(self) -> bool | tuple[bool, Exception]:
        try:
            self.df = self.df.drop_duplicates()
        except Exception as e:
            return False, e
        return True

    def try_add_age_category(self) -> bool | tuple[bool, Exception]:
        try:
            self.df['Age Category'] = ['Senior' if age > 65 else ('Adult' if age>18 else 'Young') for age in self.df['Age']]
        except Exception as e:
            return False, e
        return True
    
    def try_save(self) -> bool | tuple[bool, Exception]:
        try:
            new_file_path = self.file_path.replace('.csv', '_new.csv')
            self.df.to_csv(new_file_path)
        except Exception as e:
            return False, e
        return True


# Initialize handler with file path
handler = DataHandler("train.csv")

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

# Add age category
result = handler.try_add_age_category()
print("\nAdd age category result:", result)
print(handler.df)

# Save to new file
result = handler.try_save()
print("\nSave result:", result)
