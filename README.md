# DataAuditAI

DataAuditAI is your AI data auditor. Upload any CSV dataset and get a clear data quality report.

## Features
- Profiling: nulls, dups, outliers
- AI-explained audit report
- PDF export (optional)

## Setup
1. Add `.env` with your OpenAI API key
2. Install: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`
