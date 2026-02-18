# Example: SQL Query Assistant (Safe)

## Context
User: "Top 10 products by revenue last month"

## Goal
Return parameterized SQL + assumptions.

## Constraints
- Ask for schema if missing
- If schema unknown, provide a generic template
- Mention safe parameterization
- Keep concise

## Example output (generic)
Assumptions:
- tables: orders(order_id, order_date), order_items(order_id, product_id, quantity, unit_price), products(product_id, name)

SQL (PostgreSQL):
SELECT
  p.product_id,
  p.name,
  SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.order_date >= date_trunc('month', current_date) - interval '1 month'
  AND o.order_date <  date_trunc('month', current_date)
GROUP BY p.product_id, p.name
ORDER BY revenue DESC
LIMIT 10;

Notes:
- Ensure indexes on orders(order_date) and order_items(order_id, product_id)
- Use prepared statements if injecting dates dynamically
