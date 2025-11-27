import pandas as pd

class BaseDataHandler():
    def __init__(self, path:str | None = None, df:pd.DataFrame | None = None):
        
        self.file_path = path
        
        success, e = self.try_update_df(df)
        if not success:
            print(e)
    
    def try_update_df(self, df) -> bool | tuple[bool, any]:
        try:
            if df is not None:
                self.df = df
            else:
                self.df = pd.read_csv(self.file_path)
        except Exception as e:
            return False,e
        return True, None

    def get_lines(self, amount=5) -> pd.DataFrame:
        return self.df.head(amount) if amount > 0 else self.df.tail(amount)

    def try_fill_nan(self, use_mean:bool = True) -> bool | tuple[bool, Exception]:
        try:
            self.df = self.df.fillna(0 if use_mean else self.df.mean(numeric_only=True))
        except Exception as e:
            return False, e
        return True
    
    def try_add_col(self, target_col:str, criteria, axis:int=1) -> bool | tuple[bool, Exception]:
        try:
            self.df[target_col] = self.df.apply(criteria, axis=axis)
        except Exception as e:
            return False, e
        return True
    
    def try_remove_duplicates(self) -> bool | tuple[bool, Exception]:
        try:
            self.df = self.df.drop_duplicates()
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
    