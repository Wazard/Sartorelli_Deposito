import pandas as pd

from base_data_handler import BaseDataHandler

class SalesDataHandler(BaseDataHandler):

    def try_get_sales_by_product(self) -> tuple[bool, any]:
        return self.try_get_groupby('Product', 'Total Sales')

    def add_total_sales(self) -> bool | tuple[bool, Exception]:
        return self.try_add_col('Total Sales', lambda row: row['Quantity']*row['UnitPrice'])
    
    def try_filter_sales_greater_than(self, n:float) -> tuple[bool, any]:
        try:
            new_df = self.og_df[self.og_df['Total Sales']>n]
        except Exception as e:
            return False, e
        return True, new_df

    def try_order_by_sales(self) -> tuple[bool, any]:
        return self.try_order_by(cols='Total Sales', ascending=False)

    def try_get_sales_by_city(self) -> tuple[bool, any]:
        return self.try_get_groupby('City','Total Sales')

    def get_total_sales_pivot(self) -> pd.DataFrame:
        return self.get_pivot(values='Total Sales', index='Product')
