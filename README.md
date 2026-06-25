# NBA_RCA_Analytics

## Project Overview

NBA_RCA_Analytics is a KPI monitoring, trend analysis, business breakdown, and future AI-driven Root Cause Analysis (RCA) platform for NBA recommendation feedback data.

The platform helps stakeholders:

* Monitor recommendation performance.
* Track KPI movement across fiscal weeks.
* Analyze business dimensions contributing to KPI changes.
* Perform root cause investigations.
* Generate AI-powered insights and executive summaries.

---

# Business Objective

The objective of the platform is to answer:

### What is happening?

Measured through:

* Coverage %
* Usage %
* Thumbs Up %
* Thumbs Down %

### What changed?

Measured through:

* Week-over-week KPI trends

### Why did it change?

Measured through:

* Model-wise analysis
* Recommendation Type analysis
* Solution Type analysis
* Call Driver analysis
* Country analysis
* Global LOB analysis

### What actions should be taken?

Future LLM-based RCA and insight generation.

---

# High-Level Architecture

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
├── Overall KPI
│
└── Weekly KPI
│
▼
Trend Engine
│
▼
Business Breakdown Analysis
│
├── Model-wise
├── Recommendation Type
├── Solution Type
├── Call Driver
├── Country
└── Global LOB
│
▼
RCA Engine (Future)
│
▼
LLM Insight Engine (Future)

---

# Project Structure

NBA_RCA_Analytics/

├── data/
│   └── raw/
│       └── Weekly_Data/
│
├── reports/
│   └── NBA_RCA_Report.xlsx
│
├── src/
│   ├── data_loader.py
│   ├── validator.py
│   ├── kpi_engine.py
│   ├── trend_engine.py
│   ├── rca_engine.py
│   └── report_writer.py
│
├── run_analysis.py
│
└── README.md

---

# Current Completed Components

## 1. Data Loader

### Purpose

Loads the latest weekly dataset automatically.

### Responsibilities

* Detect latest Excel file
* Read dataset
* Return DataFrame

### Output

Pandas DataFrame

---

## 2. Data Validator

### Purpose

Validate dataset before calculations.

### Validations

* Required columns check
* Missing value check
* Duplicate case analysis
* Coverage distribution
* Feedback distribution
* Confidence score summary

---

## 3. KPI Engine

### Purpose

Calculate overall and weekly recommendation KPIs.

---

### Overall KPI Output

* Total Cases
* Coverage Cases
* Feedback Cases
* Coverage %
* Usage %
* Thumbs Up %
* Thumbs Down %

---

### Weekly KPI Output

Grouped by:

cls_fisc_wk_val

Example:

| Fiscal Week | Coverage % | Usage % | Thumbs Up % | Thumbs Down % |
| ----------- | ---------- | ------- | ----------- | ------------- |

---

# KPI Definitions

## Coverage %

Coverage Cases / Total Cases

Where:

Coverage Cases =
Distinct case_id where nbacoverage_bala = COVERAGE

---

## Usage %

(Yes Cases + No Cases) / Coverage Cases

Where:

Yes Cases =
Distinct case_id where is_helpful = YES

No Cases =
Distinct case_id where is_helpful = NO

---

## Thumbs Up %

Yes Cases / (Yes Cases + No Cases)

---

## Thumbs Down %

100 - Thumbs Up %

---

# 4. Trend Engine

### Purpose

Track KPI movement across fiscal weeks.

### Output

Week-over-week KPI trends.

Example:

| Fiscal Week | Usage % | Previous Usage % | Delta |
| ----------- | ------- | ---------------- | ----- |

Provides:

* KPI movement
* Best week
* Worst week
* Trend direction

---

# 5. Report Writer

### Purpose

Export analytics output to Excel.

### Current Features

* Writes to existing workbook
* Replaces existing sheet data
* Avoids duplicate sheet conflicts
* Supports multiple report tabs

Current Sheets:

* Overall KPI
* Weekly KPI
* Trends

---

# Business Breakdown Analysis (Current Development)

## Purpose

Break KPI performance into business dimensions.

This layer answers:

"Which business segments contributed to KPI changes?"

---

## Breakdown Dimensions

### Model-wise

Column:

based_on_txt_mdf

---

### Recommendation Type

Business-defined recommendation categories.

---

### Solution Type

Column:

sltn_type_desc

---

### Call Driver

Column:

case_detailed_category

---

### Country

Column:

assoc_country_name

---

### Global LOB

Column:

global_lob

---

# Planned Output

Latest Week vs Previous Week comparison.

Example:

| Model | W19 Usage % | W20 Usage % | Δ Usage % | W19 TU % | W20 TU % | Δ TU % |
| ----- | ----------- | ----------- | --------- | -------- | -------- | ------ |

Purpose:

* Identify KPI movement
* Support RCA investigations
* Feed future AI reasoning

---

# RCA Engine (Future)

## Purpose

Identify the business drivers responsible for KPI changes.

Example:

Overall Usage % ↓ 4.1%

The RCA Engine determines:

* Model A Usage ↓ 8%
* Printer Call Driver Usage ↓ 6%
* Brazil Usage ↓ 5%

and ranks contributors by impact.

---

# LLM Insight Engine (Future)

## Purpose

Generate executive-level explanations.

Example:

"Usage decreased by 4.1% compared to the previous week.

The decline was primarily driven by:

1. Model A (-8%)
2. Printer Call Driver (-6%)
3. Brazil (-5%)

Thumbs Up % also decreased by 3.2%, indicating reduced recommendation quality."

---

# Development Roadmap

## Phase 1 – Foundation (Completed)

* Data Loader
* Data Validator
* KPI Engine
* Trend Engine
* Report Writer

---

## Phase 2 – Business Breakdown (In Progress)

* Model-wise comparison
* Recommendation Type comparison
* Solution Type comparison
* Call Driver comparison
* Country comparison
* Global LOB comparison

---

## Phase 3 – RCA

* Driver ranking
* KPI contribution scoring
* Impact analysis

---

## Phase 4 – Agentic AI

* RCA Agent
* Insight Agent
* Executive Summary Agent
* Recommendation Quality Agent

---

# Current Project Status

Status: Active Development

Completed:

* KPI Monitoring
* Weekly KPI Analysis
* Trend Analysis
* Excel Reporting

In Progress:

* Business Breakdown Analysis

Planned:

* RCA Engine
* LLM Insight Generation
* Agentic AI Architecture
