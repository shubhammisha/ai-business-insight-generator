import streamlit as st
import pandas as pd
import plotly.express as px
import tempfile
import os
import sys

# Add the parent directory to sys.path to import from flask_app.utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flask_app', 'utils')))
from insight_generator import generate_insights

def main():
    # Sidebar
    st.sidebar.title("🧠 AI Business Insight Generator")
    st.sidebar.markdown("Upload any business CSV to generate smart AI-style insights.")
    st.sidebar.markdown("---")

    # Main Heading
    st.markdown("<h1 style='text-align: center;'>📊 Business Insights Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload your CSV and get automated insights, charts & summaries.</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("")

    uploaded_file = st.file_uploader("📁 Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.markdown("---")

        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Load CSV as DataFrame
        df = pd.read_csv(tmp_path)
        df_clean = df.dropna()

        # Generate AI-style insights and suggested graphs
        insights, graphs = generate_insights(df_clean)

        # Show insights
        st.markdown("<h2 style='text-align: center;'>📝 Smart Insights</h2>", unsafe_allow_html=True)
        st.write("")
        for value in insights:
            st.markdown(f"- {value}")

        # Show table
        st.markdown("---")
        st.subheader("📄 Preview of Uploaded Data")
        st.dataframe(df_clean.head())

        # Auto-render suggested graphs
        if graphs:
            st.markdown("---")
            st.markdown("<h2 style='text-align: center;'>📈 Auto-Generated Visualizations</h2>", unsafe_allow_html=True)
            for graph in graphs:
                if graph['type'] == 'histogram':
                    if graph['column'] in df_clean.columns:
                        fig = px.histogram(df_clean, x=graph['x'], title=graph['title'])
                        st.plotly_chart(fig, use_container_width=True)
                elif graph['type'] == 'pie':
                    labels = graph.get('labels')
                    values = graph.get('values')
                    if labels and values:
                        fig = px.pie(names=labels, values=values, title=graph['title'])
                        st.plotly_chart(fig, use_container_width=True)
                elif graph['type'] == 'line':
                    x = graph.get('x')
                    y = graph.get('y')
                    if x and y:
                        fig = px.line(x=x, y=y, title=graph['title'], labels={'x': graph.get('xlabel', ''), 'y': graph.get('ylabel', '')})
                        st.plotly_chart(fig, use_container_width=True)

        # Clean up
        os.remove(tmp_path)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
