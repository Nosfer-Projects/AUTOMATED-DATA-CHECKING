import pandas as pd


class DataExcel:
    @staticmethod
    def create_data(list_of_pcs):
        df = pd.DataFrame(list_of_pcs)
        df.sort_values(by=['Price'], inplace=True)


        writer = pd.ExcelWriter("data.xlsx")
        df.to_excel(writer, sheet_name='my_analysis', index=False, na_rep='NaN')

        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets['my_analysis'].set_column(col_idx, col_idx, column_width)

        writer.save()