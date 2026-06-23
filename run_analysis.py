from src.data_loader import DataLoader
from src.validator import DataValidator
from src.kpi_engine import KPIEngine

import pandas as pd

# Display all dataframe columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# ==========================================================
# Load Weekly Dataset
# ==========================================================

loader = DataLoader()
df = loader.load_data()

print("\nDataset Loaded Successfully!")

# ==========================================================
# Validate Dataset
# ==========================================================

validator = DataValidator()
validator.validate(df)

# ==========================================================
# Calculate KPIs
# ==========================================================

overall_kpis, weekly_kpis = KPIEngine.calculate_kpis(df)

# ==========================================================
# Overall KPI Summary
# ==========================================================

print("\n" + "=" * 60)
print("OVERALL KPI SUMMARY")
print("=" * 60)

for key, value in overall_kpis.items():
    print(f"{key:<20}: {value}")

# ==========================================================
# Fiscal Week KPI Summary
# ==========================================================

print("\n" + "=" * 60)
print("FISCAL WEEK KPI SUMMARY")
print("=" * 60)

print(weekly_kpis)

print("\n" + "=" * 60)
print("Analysis Completed Successfully")
print("=" * 60)