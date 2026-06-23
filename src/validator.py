import pandas as pd


class DataValidator:
    """
    Validates the weekly NBA dataset before KPI calculations.
    """

    REQUIRED_COLUMNS = [
        "case_id",
        "cls_fisc_wk_val",
        "like_status_bala",
        "nbacoverage_bala",
        "is_helpful",
        "confidence_scr_val",
        "case_detailed_category",
        "sltn_type_desc",
        "global_lob",
        "assoc_country_name"
    ]

    def validate(self, df: pd.DataFrame):

        print("\n" + "=" * 60)
        print("DATA VALIDATION")
        print("=" * 60)

        # -------------------------
        # Required Columns
        # -------------------------
        missing_cols = [
            col for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_cols:
            raise Exception(f"Missing Columns : {missing_cols}")

        print("✓ Required columns present")

        # -------------------------
        # Duplicate Cases
        # -------------------------
        total_rows = len(df)
        distinct_cases = df["case_id"].nunique()

        print(f"Total Recommendation Records : {total_rows:,}")
        print(f"Distinct Cases              : {distinct_cases:,}")
        print(f"Recommendations / Case      : {round(total_rows/distinct_cases,2)}")

        # -------------------------
        # Missing Values
        # -------------------------
        print("\nMissing Values")

        missing = (
            df[self.REQUIRED_COLUMNS]
            .isna()
            .sum()
            .sort_values(ascending=False)
        )

        print(missing)

        # -------------------------
        # Feedback Distribution
        # -------------------------
        print("\nAgent Feedback")

        print(df["like_status_bala"].fillna("Blank").value_counts())

        # -------------------------
        # Coverage
        # -------------------------
        print("\nCoverage")

        print(df["nbacoverage_bala"].fillna("Blank").value_counts())

        # -------------------------
        # Helpful Recommendation
        # -------------------------
        print("\nHelpful Recommendation")

        print(df["is_helpful"].fillna("Blank").value_counts())

        # -------------------------
        # Confidence
        # -------------------------
        print("\nConfidence Score")

        print(df["confidence_scr_val"].describe())

        print("\nValidation Completed Successfully.")