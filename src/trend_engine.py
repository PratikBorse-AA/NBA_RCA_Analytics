import pandas as pd


class TrendEngine:
    """
    Calculates week-over-week KPI trends.

    Input:
        Weekly KPI DataFrame from KPIEngine

    Output:
        trend_df : Week-over-week KPI comparison
    """

    @staticmethod
    def calculate_trends(weekly_kpis: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate week-over-week KPI trends.

        Parameters
        ----------
        weekly_kpis : pd.DataFrame
            Fiscal week KPI table.

        Returns
        -------
        pd.DataFrame
            Week-over-week trend comparison.
        """

        # KPI columns to compare
        kpi_columns = [
            "Coverage %",
            "Usage %",
            "Thumbs Up %",
            "Thumbs Down %"
        ]

        # Sort by fiscal week
        weekly_kpis = (
            weekly_kpis
            .sort_values("Fiscal Week")
            .reset_index(drop=True)
        )

        trend_rows = []

        # Compare current week with previous week
        for i in range(1, len(weekly_kpis)):

            previous_week = weekly_kpis.iloc[i - 1]
            current_week = weekly_kpis.iloc[i]

            for kpi in kpi_columns:

                previous_value = previous_week[kpi]
                current_value = current_week[kpi]

                change = round(current_value - previous_value, 2)

                # Trend direction
                if change > 0:
                    trend = "↑"
                elif change < 0:
                    trend = "↓"
                else:
                    trend = "→"

                trend_rows.append({
                    "Fiscal Week": current_week["Fiscal Week"],
                    "KPI": kpi,
                    "Previous Week": previous_week["Fiscal Week"],
                    "Previous Value": previous_value,
                    "Current Value": current_value,
                    "Change": change,
                    "Trend": trend
                })

        trend_df = pd.DataFrame(trend_rows)

        return trend_df