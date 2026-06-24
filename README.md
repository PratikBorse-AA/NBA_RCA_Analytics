# NBA RCA Analytics

## Overview

NBA RCA Analytics is a modular analytics framework designed to analyze the performance of the Next Best Action (NBA) recommendation system. The project processes weekly recommendation data, calculates business KPIs, identifies week-over-week trends, and lays the foundation for Root Cause Analysis (RCA), dashboards, and AI-powered business insights.

The project is designed with a scalable architecture where each module has a single responsibility, making it easy to extend and maintain.

---

# Objectives

* Analyze weekly NBA recommendation performance.
* Calculate business KPIs at overall and weekly levels.
* Monitor KPI trends across fiscal weeks.
* Export analysis into a formatted Excel workbook.
* Build a reusable Root Cause Analysis engine.
* Enable future dashboarding and LLM-based business reasoning.

---

# Current Features

### Data Loader

* Automatically loads the latest weekly Excel dataset.
* Detects the newest file from the Weekly_Data folder.
* Displays dataset information:

  * File name
  * Number of rows
  * Number of columns
  * Distinct Case IDs

---

### Data Validator

Validates the incoming dataset before analysis.

Checks include:

* Required columns
* Missing values
* Duplicate case statistics
* Agent feedback distribution
* NBA coverage distribution
* Helpful recommendation distribution
* Confidence score statistics

---

### KPI Engine

Calculates overall and fiscal week KPIs.

KPIs include:

* Total Cases
* Coverage Cases
* Feedback Cases
* Yes Cases
* No Cases
* Coverage %
* Usage %
* Thumbs Up %
* Thumbs Down %

Business formulas:

Coverage %

```
Coverage Cases / Total Cases
```

Usage %

```
(Yes Cases + No Cases) / Coverage Cases
```

Thumbs Up %

```
Yes Cases / (Yes Cases + No Cases)
```

Thumbs Down %

```
1 - Thumbs Up %
```

---

### Trend Engine

Performs week-over-week KPI comparison.

Features:

* Previous week comparison
* Current week comparison
* KPI change
* Trend direction

Supported KPIs:

* Coverage %
* Usage %
* Thumbs Up %
* Thumbs Down %

---

### Report Writer

Exports all analytics into a single Excel workbook.

Current workbook contains:

* Overall KPI
* Weekly KPI
* Trends

Automatic formatting:

* Header styling
* Auto filters
* Frozen header
* Auto column width
* Existing worksheet replacement
* Workbook creation if missing

---

# Project Architecture

```
Weekly Excel Dataset
          │
          ▼
     Data Loader
          │
          ▼
    Data Validator
          │
          ▼
      KPI Engine
          │
          ▼
     Trend Engine
          │
          ▼
    Report Writer
          │
          ▼
NBA_RCA_Report.xlsx
```

---

# Project Structure

```
NBA_RCA_Analytics/

│
├── data/
│   ├── raw/
│   │   └── Weekly_Data/
│   └── output/
│       └── Reports/
│
├── src/
│   ├── data_loader.py
│   ├── validator.py
│   ├── kpi_engine.py
│   ├── trend_engine.py
│   └── report_writer.py
│
├── run_analysis.py
├── requirements.txt
└── README.md
```

---

# Design Principles

Each analytics module follows the same architecture.

* Accept DataFrame as input.
* Perform one responsibility.
* Return DataFrame or business output.
* No business logic duplication.
* No Excel writing inside analytics engines.
* No visualization inside analytics engines.

This separation keeps the project modular, testable, and reusable.

---

# Current Workflow

```
Load Dataset
      │
      ▼
Validate Dataset
      │
      ▼
Calculate KPIs
      │
      ▼
Calculate Trends
      │
      ▼
Generate Excel Report
```

---

# Technologies Used

* Python
* Pandas
* OpenPyXL
* Git
* GitHub

---

# Future Roadmap

## Phase 1 (Completed)

* Data Loader
* Data Validator
* KPI Engine
* Trend Engine
* Report Writer

---

## Phase 2

* Generic RCA Engine
* Country Analysis
* Global LOB Analysis
* Solution Type Analysis
* Detailed Category Analysis

---

## Phase 3

* Confidence Analysis
* Product Analysis
* OEM Analysis
* Recommendation Quality Analysis

---

## Phase 4

Interactive Dashboard

Possible technologies:

* Power BI
* Streamlit
* Plotly

---

## Phase 5

LLM-powered RCA

Capabilities:

* Natural language business summaries
* KPI explanation
* Root cause reasoning
* Recommendation generation
* Executive insights

---

# Development Workflow

The project follows a feature-branch workflow.

Example:

```
main
│
├── feature/trend-engine
├── feature/rca-engine
├── feature/dashboard
├── feature/llm-insights
```

Each feature is developed, tested, and merged into the main branch after completion.

---

# Author

Pratik Borse

---

# Project Status

Current Version: **v0.3**

Completed Modules:

* Data Loader
* Data Validator
* KPI Engine
* Trend Engine
* Report Writer

Next Module:

**Root Cause Analysis (RCA) Engine**
