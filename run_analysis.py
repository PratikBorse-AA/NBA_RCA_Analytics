from src.data_loader import DataLoader
from src.validator import DataValidator
from src.kpi_engine import KPIEngine
from src.trend_engine import TrendEngine
from src.report_writer import ReportWriter

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

# Convert overall KPIs to DataFrame
overall_kpi_df = pd.DataFrame(
    list(overall_kpis.items()),
    columns=["KPI", "Value"]
)

# ==========================================================
# Calculate Trends
# ==========================================================

trend_df = TrendEngine.calculate_trends(weekly_kpis)

# ==========================================================
# Export Reports
# ==========================================================

ReportWriter.write_sheet(
    dataframe=overall_kpi_df,
    sheet_name="Overall KPI"
)

ReportWriter.write_sheet(
    dataframe=weekly_kpis,
    sheet_name="Weekly KPI"
)

ReportWriter.write_sheet(
    dataframe=trend_df,
    sheet_name="Trends"
)

# ==========================================================
# Display Results
# ==========================================================

print("\n" + "=" * 60)
print("OVERALL KPI SUMMARY")
print("=" * 60)

for key, value in overall_kpis.items():
    print(f"{key:<20}: {value}")

print("\n" + "=" * 60)
print("FISCAL WEEK KPI SUMMARY")
print("=" * 60)

print(weekly_kpis)

print("\n" + "=" * 60)
print("WEEK-OVER-WEEK KPI TRENDS")
print("=" * 60)

print(trend_df)

print("\n" + "=" * 60)
print("Excel Report Generated Successfully")
print("=" * 60)
print(f"Location : {ReportWriter.OUTPUT_FILE}")

print("\n" + "=" * 60)
print("Analysis Completed Successfully")
print("=" * 60)