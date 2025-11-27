import pandas as pd
import numpy as np
import __init__
from base_data_handler import BaseDataHandler

class DataHandler(BaseDataHandler):

    def try_clean_age(self) -> tuple[bool,any]:
        try:
            self.__df[self.df['Age']<0] *= -1
            self.__df = self.__df[self.df['Age']>12]
        except Exception as e:
            return False, e
        return True, None
    
    def try_clamp_monthly_costs(self, min_v:float=0, max_v:float=200) -> tuple[bool, any]:
        return self.try_clamp_cols('Monthly Cost', min_v, max_v)
    
    def try_clamp_data_usage(self, min_v:float=0, max_v:float=999) -> tuple[bool,any]:
        return self.try_clamp_cols('Data Usage', min_v, max_v)

    def try_drop_nan_id(self):
        return self.try_drop_nan(['id_client','Monthly Cost'])
    
    def try_add_cost_per_GB(self) -> tuple[bool, any]:
        return self.try_add_col(
            target_col='Cost per GB', 
            criteria= lambda row: row['Monthly Cost']/row['Data Usage']
            )
    
    def try_add_age_group(self) -> tuple[bool, any]:
        return self.try_add_col(
            target_col="Age Group",
            criteria=lambda row: (
                "<25" if row["Age"] < 25 else
                "25-35" if row["Age"] < 35 else
                "35-50" if row["Age"] < 50 else"50+")
            )

    def try_add_cost_range(self) -> tuple[bool, any]:
        return self.try_add_col(
            target_col="Cost Range",
            criteria=lambda row: (
                "Low" if row["Monthly Cost"] <= 50 else
                "Medium" if row["Monthly Cost"] <= 100 else
                "High")
            )

    def try_get_churn_rate(self) -> tuple[bool, any]:
        try:
            # Ensure Age Group exists
            if "Age Group" not in self.df.columns:
                ok, err = self.try_add_age_group()
                if not ok:
                    return False, err

            # Ensure Cost Range exists
            if "Cost Range" not in self.df.columns:
                ok, err = self.try_add_cost_range()
                if not ok:
                    return False, err

            # Group by Age Group and Cost Range, compute churn rate
            churn_rate = (
                self.df.groupby(["Age Group", "Cost Range"])["Churn"]
                .mean()
                .reset_index()
                .rename(columns={"Churn": "Churn Rate"})
            )

        except Exception as e:
            return False, e

        return True, churn_rate



