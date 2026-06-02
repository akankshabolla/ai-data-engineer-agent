from ai_agent import (
    explain_dataset,
    suggest_cleaning,
    generate_sql,
    generate_insights
)

sample_summary = """
Rows: 5000
Columns: product, revenue, order_date, region

Missing Values:
revenue: 12%
region: 5%

Duplicates:
15 rows

Data Types:
product: string
revenue: float
order_date: string
region: string
"""

columns = ["product", "revenue", "order_date", "region"]

question = "Show top 5 products by revenue"


print("\n========== DATASET EXPLANATION ==========\n")
print(explain_dataset(sample_summary))

print("\n========== CLEANING SUGGESTIONS ==========\n")
print(suggest_cleaning(sample_summary))

print("\n========== GENERATED SQL ==========\n")
print(generate_sql(question, columns))

print("\n========== BUSINESS INSIGHTS ==========\n")
print(generate_insights(sample_summary))