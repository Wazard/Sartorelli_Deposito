import pandas as pd
import numpy as np
import __init__
from base_data_handler import BaseDataHandler

def create_random_clients(n: int = 100) -> pd.DataFrame:
    """
    Create a DataFrame with n random clients.
    Columns: id_client, Age, Monthly Cost, Data Usage, Churn
    Adds ~10% NaNs in each column.
    """
    np.random.seed(42)  # reproducibility

    data = {
        "id_client": np.arange(1, n+1),
        "Age": np.random.randint(18, 70, size=n),                # ages between 18–70
        "Monthly Cost": np.random.randint(20, 250, size=n),      # monthly cost between 20–250
        "Data Usage": np.random.randint(1, 100, size=n),         # GB usage between 1–100
        "Churn": np.random.choice([0, 1], size=n, p=[0.7, 0.3])  # 30% churn rate
    }

    df = pd.DataFrame(data)

    # Inject ~10% NaNs per column
    for col in df.columns:
        nan_indices = np.random.choice(df.index, size=int(n * 0.1), replace=False)
        df.loc[nan_indices, col] = np.nan

    return df


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


# --- Sample dataset ---

df = pd.DataFrame(create_random_clients())

# --- Initialize handler ---
handler = DataHandler(df=df)

print("\n=== Original Data ===")
print(handler.df)

# --- Clean Age ---
handler.try_clean_age()
print("\n=== After Cleaning Age ===")
print(handler.df)

# --- Clamp Monthly Costs ---
handler.try_clamp_monthly_costs(min_v=0, max_v=200)
print("\n=== After Clamping Monthly Costs ===")
print(handler.df)

# --- Clamp Data Usage ---
handler.try_clamp_data_usage(min_v=0, max_v=999)
print("\n=== After Clamping Data Usage ===")
print(handler.df)

# --- Drop NaN in ID and Monthly Cost ---
handler.try_drop_nan_id()
print("\n=== After Dropping NaN in id_client & Monthly Cost ===")
print(handler.df)

# --- Add Cost per GB ---
handler.try_add_cost_per_GB()
print("\n=== After Adding Cost per GB ===")
print(handler.df[["Monthly Cost", "Data Usage", "Cost per GB"]])

# --- Add Age Group ---
handler.try_add_age_group()
print("\n=== After Adding Age Group ===")
print(handler.df)

# --- Add Cost Range ---
handler.try_add_cost_range()
print("\n=== After Adding Cost Range ===")
print(handler.df)

# --- Get Churn Rate by Age Group & Cost Range ---
success, churn_rate = handler.try_get_churn_rate()
if success:
    print("\n=== Churn Rate by Age Group & Cost Range ===")
    print(churn_rate)

# --- Pivot Table Example ---
pivot = handler.get_pivot(values="Monthly Cost", index="Age Group", columns="Cost Range")
print("\n=== Pivot Table (Monthly Cost by Age Group & Cost Range) ===")
print(pivot)

# --- GroupBy Example ---
success, grouped = handler.try_get_groupby("Age Group", "Monthly Cost")
if success:
    print("\n=== GroupBy (Average Monthly Cost per Age Group) ===")
    print(grouped.mean())

