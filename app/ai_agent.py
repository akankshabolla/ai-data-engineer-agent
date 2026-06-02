import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Add it to your .env file.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"


def explain_dataset(summary):
    prompt = f"""
You are an AI Data Engineer Agent.

Explain this dataset profile in simple terms:

{summary}

Include:
- What the dataset seems to contain
- Important columns
- Data quality issues
- Whether it is ready for analytics
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def suggest_cleaning(summary):
    prompt = f"""
You are an AI Data Engineering Assistant.

Based on the dataset summary below, suggest practical data cleaning steps:

{summary}

Include:
- Missing value handling
- Duplicate handling
- Data type fixes
- Outlier handling
- Final recommendation

Give the answer in clear bullet points.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def generate_sql(question, columns):
    prompt = f"""
You are an expert SQL engineer.

Table name:
uploaded_data

Available columns:
{columns}

User question:
{question}

Generate ONLY a DuckDB-compatible SQL query.
Do not include explanations.
Do not include markdown formatting.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    sql_query = response.text.strip()

    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    return sql_query


def generate_insights(summary):
    prompt = f"""
You are an AI Data Analyst and Data Engineering Assistant.

Analyze this dataset summary:

{summary}

Generate:
- Key business insights
- Data quality risks
- Possible trends
- Recommended next steps
- How this dataset can be used for analytics

Keep the response clear and professional.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text