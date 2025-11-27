import pandas as pd
import numpy as np

class DataHandler():
    def __init__(self, path:str):
        
        self.file_path = path
        
        
        self.update_df()

    def update_df(self) -> None:
        self.df = pd.DataFrame(self.file_path)
    
    def get_lines(self, amount=5) -> pd.DataFrame:
        return self.df.head(amount) if amount > 0 else self.df.tail(amount)

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

    def try_remove_duplicates(self) -> True | tuple[False, Exception]:
        try:
            self.df = self.df.drop_duplicates()
        except Exception as e:
            return False, e
        return True

    def try_add_age_category(self) -> True | tuple[False, Exception]:
        try:
            self.df['Age Category'] = ['Senior' if age > 65 else ('Adult' if age>18 else 'Young') for age in self.df['Age']]
        except Exception as e:
            return False, e
        return True
    
    def try_save(self) -> True | tuple[False, Exception]:
        try:
            new_file_path = self.file_path.replace('.csv', '_new.csv')
            self.df.to_csv(new_file_path)
        except Exception as e:
            return False, e
        return True
