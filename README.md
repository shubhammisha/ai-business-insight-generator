# AI-Powered Business Insight Generator

## Overview
A professional, end-to-end solution for generating smart, AI-powered business insights and beautiful PDF reports from any CSV or Excel data. Combines a Flask backend for file upload and PDF generation with an interactive Streamlit dashboard for instant data exploration and visualization.

## Features
- 📈 Upload any CSV/Excel file (HR, sales, customer, etc.)
- 🤖 Automatic AI-style insight generation using pandas
- 📊 Interactive charts and summaries (Streamlit)
- 📝 Download polished PDF business reports (Flask/Streamlit)
- 🗂️ Clean, modular folder structure
- 🖥️ Modern, recruiter-friendly UI (Flask + Streamlit)

## Tech Stack
- Python 3
- Flask
- Streamlit
- pandas, numpy
- plotly, matplotlib
- fpdf (PDF generation)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-business-insight-generator.git
cd ai-business-insight-generator/ai_sales_insight
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App (for PDF upload/download)
```bash
cd flask_app
python3 app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

### 4. Run the Streamlit Dashboard (for interactive insights)
```bash
cd ../streamlit_dashboard
streamlit run app.py
```

## Sample Screenshot
> ![Dashboard Screenshot](screenshot.png)

## Future Improvements
- User authentication & history
- More advanced AI/NLP insights
- Cloud deployment (Heroku, AWS, etc.)
- Export charts to PDF
- Multi-language support

---
**Author:** Shubham Mishra 