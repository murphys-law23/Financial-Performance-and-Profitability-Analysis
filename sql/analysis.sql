-- PostgreSQL: import data/financial_transactions.csv into financial_transactions
CREATE TABLE IF NOT EXISTS financial_transactions (month DATE, department TEXT, expense_category TEXT, revenue NUMERIC(14,2), revenue_budget NUMERIC(14,2), expense NUMERIC(14,2), expense_budget NUMERIC(14,2));
-- 1. Monthly profitability
SELECT month, SUM(revenue) AS revenue, SUM(expense) AS expenses, SUM(revenue)-SUM(expense) AS operating_profit, ROUND(100*(SUM(revenue)-SUM(expense))/NULLIF(SUM(revenue),0),2) AS profit_margin_pct FROM financial_transactions GROUP BY month ORDER BY month;
-- 2. Department ranking
SELECT department, SUM(revenue) AS revenue, SUM(expense) AS expense, SUM(revenue)-SUM(expense) AS profit FROM financial_transactions GROUP BY department ORDER BY profit DESC;
-- 3. Budget vs actual
SELECT month, SUM(revenue)-SUM(revenue_budget) AS revenue_variance, SUM(expense_budget)-SUM(expense) AS favorable_expense_variance FROM financial_transactions GROUP BY month ORDER BY month;
-- 4. Expense mix
SELECT expense_category, SUM(expense) AS spend, ROUND(100*SUM(expense)/SUM(SUM(expense)) OVER (),2) AS spend_share_pct FROM financial_transactions GROUP BY expense_category ORDER BY spend DESC;
-- 5. MoM revenue movement
WITH m AS (SELECT month,SUM(revenue) AS revenue FROM financial_transactions GROUP BY month) SELECT month,revenue,ROUND(100*(revenue-LAG(revenue) OVER (ORDER BY month))/NULLIF(LAG(revenue) OVER (ORDER BY month),0),2) AS mom_growth_pct FROM m ORDER BY month;
