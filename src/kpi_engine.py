import pandas as pd


class KPIEngine:
    """
    KPI Engine

    Calculates:
    1. Overall KPIs
    2. Fiscal Week-wise KPIs

    Note:
    All calculations are based on DISTINCT case_id.
    """

    @staticmethod
    def calculate_kpis(df: pd.DataFrame):

        def calculate_metrics(data):

            # Total Cases
            # Source: case_id
            total_cases = data["case_id"].nunique()

            # Coverage Cases
            # Source: nbacoverage_bala = Coverage
            coverage_cases = data.loc[
                data["nbacoverage_bala"] == "Coverage",
                "case_id"
            ].nunique()

            # Yes Cases
            # Source: is_helpful = Yes
            yes_cases = data.loc[
                data["is_helpful"] == "Yes",
                "case_id"
            ].nunique()

            # No Cases
            # Source: is_helpful = No
            no_cases = data.loc[
                data["is_helpful"] == "No",
                "case_id"
            ].nunique()

            # Feedback Cases
            # Source: is_helpful = Yes or No
            feedback_cases = data.loc[
                data["is_helpful"].isin(["Yes", "No"]),
                "case_id"
            ].nunique()

            # Coverage % = Coverage Cases / Total Cases
            coverage_pct = round(
                (coverage_cases / total_cases) * 100, 2
            ) if total_cases else 0

            # Usage % = Feedback Cases / Coverage Cases
            usage_pct = round(
                (feedback_cases / coverage_cases) * 100, 2
            ) if coverage_cases else 0

            # Thumbs Up % = Yes Cases / Feedback Cases
            thumbs_up_pct = round(
                (yes_cases / feedback_cases) * 100, 2
            ) if feedback_cases else 0

            # Thumbs Down % = 100 - Thumbs Up %
            thumbs_down_pct = round(
                100 - thumbs_up_pct, 2
            ) if feedback_cases else 0

            return {
                "Total Cases": total_cases,
                "Coverage Cases": coverage_cases,
                "Feedback Cases": feedback_cases,
                "Yes Cases": yes_cases,
                "No Cases": no_cases,
                "Coverage %": coverage_pct,
                "Usage %": usage_pct,
                "Thumbs Up %": thumbs_up_pct,
                "Thumbs Down %": thumbs_down_pct
            }

        # ======================================================
        # Overall KPIs
        # ======================================================

        overall_kpis = calculate_metrics(df)

        # ======================================================
        # Fiscal Week-wise KPIs
        # ======================================================

        weekly_kpis = []

        for week, week_df in df.groupby("cls_fisc_wk_val"):

            metrics = calculate_metrics(week_df)
            metrics["Fiscal Week"] = week

            weekly_kpis.append(metrics)

        weekly_kpis = pd.DataFrame(weekly_kpis)

        weekly_kpis = weekly_kpis[
            [
                "Fiscal Week",
                "Total Cases",
                "Coverage Cases",
                "Feedback Cases",
                "Yes Cases",
                "No Cases",
                "Coverage %",
                "Usage %",
                "Thumbs Up %",
                "Thumbs Down %",
            ]
        ]

        weekly_kpis = weekly_kpis.sort_values(
            by="Fiscal Week"
        ).reset_index(drop=True)

        return overall_kpis, weekly_kpis