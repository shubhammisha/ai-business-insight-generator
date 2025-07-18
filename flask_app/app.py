from flask_app.utils.pdf_generator import generate_pdf
from flask_app.utils.insight_generator import generate_insights

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import pandas as pd
import streamlit as st

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        # Read the file into a DataFrame
        if filename.endswith('.csv'):
            df = pd.read_csv(save_path)
        else:
            df = pd.read_excel(save_path)

        # Generate insights and PDF
        insights, _ = generate_insights(df)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'AI_Report.pdf')
        generate_pdf(insights, pdf_path)

        return render_template('success.html', filename=filename)

    else:
        return 'Invalid file type. Only .csv and .xlsx files are allowed.'

@app.route('/download-pdf')
def download_pdf():
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'AI_Report.pdf')
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    else:
        return "No PDF report found. Upload a file first."

if __name__ == '__main__':
    app.run(debug=True)
