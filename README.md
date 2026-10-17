# Financial Performance and Profitability Analysis

An entry-to-intermediate portfolio case study examining revenue, operating expenses, profit margins and budget performance across three departments in 2025.

**Tools:** Python · pandas · Matplotlib · SQL · Power BI DAX · HTML/CSS/JavaScript

> This project uses synthetic educational data and illustrative USD amounts. It does not represent a real company's financial performance.

## Dashboard preview

![Financial performance dashboard with revenue, profit, expense mix and budget variance](reports/dashboard_preview.png)

*Static preview generated from the supplied CSV using Python. The [interactive HTML dashboard](dashboard/index.html) provides quarter and department filters. Download the repository and open that file in your browser; GitHub's file viewer displays its source.*

## Business problem

Finance teams need to understand whether revenue and spending are tracking to plan, which departments generate the most operating profit, and which expense categories deserve investigation.

This project answers four questions:

1. How do revenue, expenses and profit change during the year?
2. Which departments contribute the most operating profit?
3. How do actual revenue and expenses compare with budget?
4. Which categories account for the largest share of operating costs?

## Dataset

- **Input:** `data/financial_transactions.csv`
- **Coverage:** January–December 2025; 180 records; three departments; five expense categories.
- **Grain:** One month × department × expense-category combination per row.
- **Provenance:** Synthetic data supplied with this case study. The checked-in CSV is the reproducible input; the original generation script is not included.

Revenue and revenue budget appear on one category row per department-month to avoid double counting. An expense-category filter must therefore not be applied to revenue or profit-margin visuals.

## Workflow and skills demonstrated

| Stage | Work performed |
|---|---|
| Data validation | Check missing values, nonnegative amounts and unique month/department/category combinations |
| Python analysis | Aggregate monthly results, calculate profit and margins, and visualize trends |
| SQL analysis | Analyze profitability, department rankings, budget variances, expense shares and month-over-month revenue changes |
| Reconciliation | Compare the annual SQL operating-profit total with the pandas result |
| Dashboard | Present KPIs and trends with quarter and department filters |
| Power BI preparation | Supply DAX measures, a matching theme and a report build specification |

SQL examples demonstrate aggregation, CTEs, window functions and safe division with `NULLIF`.

## Key findings

| Metric | Result |
|---|---:|
| Revenue | $5,001,393.53 |
| Operating expenses | $2,700,356.33 |
| Operating profit | $2,301,037.20 |
| Operating margin | 46.0% |
| Revenue variance versus budget | -$28,865.27 |
| Favorable expense variance | $41,849.05 |

- **Online generated the highest operating profit:** $787,486.84.
- **Revenue finished approximately 0.6% below budget.** Review monthly demand and pricing assumptions before revising forecasts.
- **Payroll represented approximately 37.5% of operating expenses.** Review staffing costs alongside productivity and service levels, rather than assuming that lower spending is always better.
- **Expenses were below budget overall.** Investigate whether this reflects efficiency, delayed spending or reduced activity; this dataset cannot distinguish the causes.

## Metric definitions

- **Operating profit:** Revenue − operating expenses.
- **Operating margin:** Total operating profit ÷ total revenue, not an average of row-level margins.
- **Revenue variance:** Actual revenue − budgeted revenue; positive is favorable.
- **Favorable expense variance:** Budgeted expenses − actual expenses; positive is favorable.

## Repository structure

```text
finance-performance-analysis/
├── README.md
├── README.docx
├── data/          # Synthetic input CSV
├── python/        # Notebook, analysis runner and preview builder
├── sql/           # PostgreSQL and SQLite queries
├── powerbi/       # DAX, theme and Word build guide
├── dashboard/     # Interactive HTML dashboard
├── reports/       # Preview PNG, Word insights and SQL result tables
├── docs/          # Word data dictionary
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Run the project

Download or clone this repository, then open a terminal in its root folder.

```bash
python -m pip install -r requirements.txt
python python/run_analysis.py
python python/build_preview.py
```

The analysis runner uses SQLite from Python's standard library, checks the dataset, reconciles operating profit with pandas and writes five result tables to `reports/query_results/`. No separate database server is required for this route.

To explore the notebook, install JupyterLab separately if needed, start it from the `python/` folder, and open `finance_eda.ipynb`.

To use PostgreSQL, create the table from `sql/analysis.sql`, import the CSV with matching column order, and run the analysis queries. The PostgreSQL version is supplied separately; the automated validation here covers SQLite.

To refresh the dashboard after editing the CSV:

```bash
python python/refresh_dashboard.py
python python/build_preview.py
```

Open `dashboard/index.html` locally. The compact desktop layout targets a 1440 × 900 browser content area; smaller screens use a scrolling layout.

## Power BI deliverables

- [DAX measures](powerbi/measures.dax)
- [Navy and teal theme](powerbi/theme.json)
- [Report build guide — Word](powerbi/BUILD_GUIDE.docx)

**A native `.pbix` report is not included, and the DAX/theme have not been validated in Power BI Desktop.** The completed dashboard is HTML; the preview is generated by Python. Use the supplied guide to build and save the Power BI version.

## Detailed documentation

- [Data dictionary — Word](docs/data_dictionary.docx)
- [Findings and recommendations — Word](reports/insights.docx)
- [Dashboard instructions — Word](dashboard/README.docx)

## Limitations

The dataset is synthetic, covers one year and contains no cash-flow, balance-sheet, tax, interest or operational-driver data. Operating profit is not net income. Observed differences support further investigation, not causal conclusions or financial advice.

## License

See [LICENSE](LICENSE).
