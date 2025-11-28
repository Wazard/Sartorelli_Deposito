import pandas as pd
import numpy as np

class BaseDataHandler():
    def __init__(self, path:str | None = None, df:pd.DataFrame | None = None):
        
        self.file_path = path
        
        success, e = self.try_init_df(df)
        if not success:
            print(e)
    
    @property
    def og_df(self) -> pd.DataFrame:
        return self.__df
    
    @property
    def df(self) -> pd.DataFrame:
        return self.__curr_df if not None else self.df
    
    def df_log(self, base:float='e') -> pd.DataFrame:
        numeric_cols = self.df.select_dtypes(include='number').columns
        df_log = self.df.copy()

        if base == 'e':
            df_log[numeric_cols] = df_log[numeric_cols].apply(lambda x: np.log(x.clip(lower=1e-9)))
        else:
            df_log[numeric_cols] = df_log[numeric_cols].apply(lambda x: np.log(x.clip(lower=1e-9)) / np.log(base))

        return df_log

    def get_lines(self, amount=5) -> pd.DataFrame:
        # returns rows from top or bottom like lists would
        return self.og_df.head(amount) if amount > 0 else self.og_df.tail(amount)

    def print_dataframe(self, full=False):
        row = self.og_df.shape[0] if full else 5
        return self.og_df.head(row)
    
    def get_pivot(self, values=None, index=None, columns=None, aggfunc:str="mean") -> pd.DataFrame:
        return pd.pivot_table(self.og_df, values=values, index=index, columns=columns, aggfunc=aggfunc)
    
    def try_get_groupby(self, target_col: str | list[str], col:str) -> tuple[bool, any]:
        try:
            tmp_df = self.og_df.groupby(by=target_col)[col]
        except Exception as e:
            return False, e
        return True, tmp_df

    def try_init_df(self, df) -> tuple[bool, any]:
        try:
            if df is not None:
                self.__df = df
                self.__curr_df = df
            else:
                self.__df = pd.read_csv(self.file_path)
                self.__curr_df = self.og_df.copy()
        except Exception as e:
            return False, e
        return True, None
    
    def try_reset_df(self) -> tuple[bool, any]:
        try:
            self.__curr_df = self.og_df.copy()
        except Exception as e:
            return False, e
        return True, None
    
    def try_update_og_df(self) -> tuple[bool, any]:
        try:
            self.__df = self.__curr_df.copy()
        except Exception as e:
            return False, e
        return True, None
    
    def try_order_by(self, cols:str | list[str], ascending:bool | list[bool]=True) -> tuple[bool, any]:
        try:
            self.__curr_df = self.og_df.sort_values(by=cols, ascending=ascending).reset_index()
        except Exception as e:
            return False, e
        return True, None

    def try_fill_nan(self, use_mean:bool = True) -> tuple[bool, any]:
        try:
            self.__curr_df = self.og_df.fillna(0 if use_mean else self.og_df.mean(numeric_only=True))
        except Exception as e:
            return False, e
        return True, None
    
    def try_add_col(self, target_col:str, criteria, axis:int=1) -> tuple[bool, any]:
        try:
            self.__curr_df[target_col] = self.og_df.apply(criteria, axis=axis)
        except Exception as e:
            return False, e
        return True, None
    
    def try_remove_duplicates(self) -> tuple[bool, any]:
        try:
            self.__curr_df = self.og_df.drop_duplicates()
        except Exception as e:
            return False, e
        return True, None
    
    def try_save(self) -> tuple[bool, any]:
        try:
            new_file_path = self.file_path.replace('.csv', '_new.csv')
            self.og_df.to_csv(new_file_path)
        except Exception as e:
            return False, e
        return True, None
    
    def try_drop_nan(self, cols:str|list[str]) -> tuple[bool, any]:
        try:
            self.__curr_df = self.og_df.dropna(subset=cols)
            self.__curr_df = self.og_df.dropna(axis=1, how='all')
        except Exception as e:
            return False, e
        return True, None
    
    def try_clamp_cols(self, cols:str|list[str], lower_bounds:float=0, upper_bounds:float=200, use_og:bool = False) -> tuple[bool, any]:
        try:
            self.__curr_df[cols] = self.og_df[cols].clip(lower_bounds,upper_bounds) if use_og else self.__curr_df[cols].clip(lower_bounds,upper_bounds)
        except Exception as e:
            return False, e
        return True, None
    
    def df_norm(self, method:str="minmax") -> pd.DataFrame:
        numeric_cols = self.df.select_dtypes(include='number').columns
        df_norm = self.df.copy()
        if method == "minmax":
            df_norm[numeric_cols] = df_norm[numeric_cols].apply(
                lambda x: (x - x.min()) / (x.max() - x.min())
            )
        elif method == "zscore":
            df_norm[numeric_cols] = df_norm[numeric_cols].apply(
                lambda x: (x - x.mean()) / x.std(ddof=0)
            )
        return df_norm