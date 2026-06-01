# AI Data Engineer Agent

An AI-powered data engineering assistant that automates dataset profiling, cleaning, analysis, SQL generation, and dashboard creation. Users can upload datasets and receive intelligent recommendations, insights, and visualizations without writing code.

---

## Features

### Data Upload & Profiling
- Upload CSV and Excel datasets
- Dataset preview and schema analysis
- Row and column statistics
- Missing value detection
- Duplicate row detection
- Data type analysis
- Unique value analysis

### Data Quality Monitoring
- Missing value identification
- Duplicate record detection
- Invalid data type detection
- Outlier detection
- Data quality summary report

### AI-Powered Recommendations
- Automatic dataset explanation
- AI-generated cleaning suggestions
- Data quality improvement recommendations
- Business insights generation using Gemini AI

### Data Cleaning
- Remove duplicate records
- Handle missing values automatically
- Data type standardization
- Download cleaned dataset

### SQL Analytics
- Natural language to SQL conversion
- AI-generated SQL queries
- SQL execution on uploaded datasets using DuckDB
- Query result visualization

### Interactive Dashboard
- Revenue trends and analytics
- Data quality metrics
- Missing value visualizations
- Category distributions
- Interactive charts and reports

---

## Tech Stack

### Frontend
- React.js
- Vite
- Tailwind CSS
- Axios
- Recharts
- React Router

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### Data Engineering
- Pandas
- NumPy
- OpenPyXL
- PyArrow

### SQL Engine
- DuckDB

### Artificial Intelligence
- Google Gemini API

### Deployment
- Vercel (Frontend)
- Render (Backend)
- GitHub

---

## Project Workflow

1. Upload a CSV or Excel dataset
2. Automatically profile and analyze the dataset
3. Detect data quality issues
4. Generate AI-powered recommendations
5. Clean and transform data
6. Generate SQL queries from natural language
7. Execute analytics using DuckDB
8. Visualize insights through interactive dashboards
9. Export cleaned data for downstream analytics

---

## Architecture

```text
React Frontend
       │
       ▼
FastAPI Backend
       │
 ┌─────┼─────┐
 ▼     ▼     ▼

Pandas DuckDB Gemini

 ▼
Data Profiling

 ▼
Data Cleaning

 ▼
SQL Analytics

 ▼
Dashboard & Insights
```

---

## Future Enhancements

- PostgreSQL integration
- Automated ETL pipeline generation
- Multi-dataset analysis
- AI-powered data catalog
- Role-based authentication
- Cloud storage integration
- Advanced data lineage tracking

---

## Team

Built by a team of 3 developers as an AI-powered Data Engineering platform focused on automating data profiling, cleaning, analytics, and insight generation.
