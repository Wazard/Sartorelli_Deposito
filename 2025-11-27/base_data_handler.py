import pandas as pd

class BaseDataHandler():
    def __init__(self, path:str | None = None, df:pd.DataFrame | None = None):
        
        self.file_path = path
        
        success, e = self.try_update_df(df)
        if not success:
            print(e)
    
    @property
    def df(self) -> pd.DataFrame:
        return self.__df

    def get_lines(self, amount=5) -> pd.DataFrame:
        # returns rows from top or bottom like lists would
        return self.df.head(amount) if amount > 0 else self.df.tail(amount)

    def print_dataframe(self):
        print(self.df)
    
    def get_pivot(self, values=None, index=None, columns=None, aggfunc:str="mean") -> pd.DataFrame:
        return pd.pivot_table(self.df, values=values, index=index, columns=columns, aggfunc=aggfunc)
    
    def try_get_groupby(self, target_col: str | list[str], col:str) -> tuple[bool, any]:
        try:
            tmp_df = self.df.groupby(by=target_col)[col]
        except Exception as e:
            return False, e
        return True, tmp_df

    def try_update_df(self, df) -> tuple[bool, any]:
        try:
            if df is not None:
                self.__df = df
            else:
                self.__df = pd.read_csv(self.file_path)
        except Exception as e:
            return False, e
        return True, None
    
    def try_order_by(self, cols:str | list[str], ascending:bool | list[bool]=True) -> tuple[bool, any]:
        try:
            self.__df = self.df.sort_values(by=cols, ascending=ascending).reset_index()
        except Exception as e:
            return False, e
        return True, None

    def try_fill_nan(self, use_mean:bool = True) -> tuple[bool, any]:
        try:
            self.__df = self.df.fillna(0 if use_mean else self.df.mean(numeric_only=True))
        except Exception as e:
            return False, e
        return True, None
    
    def try_add_col(self, target_col:str, criteria, axis:int=1) -> tuple[bool, any]:
        try:
            self.__df[target_col] = self.df.apply(criteria, axis=axis)
        except Exception as e:
            return False, e
        return True, None
    
    def try_remove_duplicates(self) -> tuple[bool, any]:
        try:
            self.__df = self.df.drop_duplicates()
        except Exception as e:
            return False, e
        return True, None
    
    def try_save(self) -> tuple[bool, any]:
        try:
            new_file_path = self.file_path.replace('.csv', '_new.csv')
            self.df.to_csv(new_file_path)
        except Exception as e:
            return False, e
        return True, None
    
    def try_drop_nan(self, cols:str|list[str]) -> tuple[bool, any]:
        try:
            self.__df = self.df.dropna(subset=cols)
            self.__df = self.df.dropna(axis=1, how='all')
        except Exception as e:
            return False, e
        return True, None
    
    def try_clamp_cols(self, cols:str|list[str], min_v:float=0, max_v:float=200) -> tuple[bool, any]:
        try:
            self.__df[cols] = self.df[cols].clip(min_v,max_v)
        except Exception as e:
            return False, e
        return True, None