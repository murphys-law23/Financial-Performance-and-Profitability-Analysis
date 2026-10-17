"""Run from any directory: python python/run_analysis.py. Outputs are rebuilt locally."""
from pathlib import Path
import sqlite3
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
TABLE = 'financial_transactions'
frame = pd.read_csv(ROOT / 'data' / (TABLE + '.csv'))
assert not frame.isna().any().any(), 'Missing values'
assert not frame.duplicated(['month','department','expense_category']).any()
assert (frame[['revenue','expense','revenue_budget','expense_budget']] >= 0).all().all()
out = ROOT / 'reports' / 'query_results'
out.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(':memory:') as conn:
    frame.to_sql(TABLE, conn, index=False)
    script = (ROOT / 'sql' / 'analysis_sqlite.sql').read_text()
    statements = [s.strip() for s in script.split(';') if s.strip()]
    query = 0
    for statement in statements:
        cursor = conn.execute(statement)
        if cursor.description:
            query += 1
            result = pd.DataFrame(cursor.fetchall(), columns=[c[0] for c in cursor.description])
            result.to_csv(out / f'query_{query:02}.csv', index=False)
    sql_total = conn.execute('SELECT SUM(revenue)-SUM(expense) FROM financial_transactions').fetchone()[0]
    python_total = frame.revenue.sum()-frame.expense.sum()
    assert abs(sql_total - python_total) < 0.01, 'SQL / Python reconciliation failed'
print(f'Passed data checks and SQL/Python total reconciliation; wrote {query} query results.')
