from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Loads the latest weekly Excel file from data/raw/Weekly_Data
    """

    def __init__(self, data_folder="data/raw/Weekly_Data"):
        self.data_folder = Path(data_folder)

    def get_latest_file(self):
        excel_files = list(self.data_folder.glob("*.xlsx"))

        if not excel_files:
            raise FileNotFoundError(
                f"No Excel files found in {self.data_folder}"
            )

        latest_file = max(excel_files, key=lambda x: x.stat().st_mtime)
        return latest_file

    def load_data(self):
        file_path = self.get_latest_file()

        print("=" * 60)
        print("Loading Weekly Dataset")
        print("=" * 60)
        print(f"File : {file_path.name}")

        df = pd.read_excel(file_path)

        print(f"Rows : {len(df):,}")
        print(f"Columns : {len(df.columns)}")
        print(f"Distinct Case IDs : {df['case_id'].nunique():,}")

        return df