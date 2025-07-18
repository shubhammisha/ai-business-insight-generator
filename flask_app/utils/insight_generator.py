import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype, is_categorical_dtype

def generate_insights(df):
    insights = []
    suggested_graphs = []
    for col in df.columns:
        col_data = df[col].dropna()
        if col_data.empty:
            insights.append(f"⚠️ Column '{col}' has no valid data and was skipped.")
            continue
        # Numeric columns
        if is_numeric_dtype(col_data):
            mean = col_data.mean()
            min_val = col_data.min()
            max_val = col_data.max()
            insights.append(f"📊 Column '{col}' has average value: {mean:.2f}")
            insights.append(f"🔻 Minimum {col}: {min_val}, Maximum: {max_val}")
            low_vals = col_data[col_data < mean - col_data.std()]
            if not low_vals.empty:
                insights.append(f"⚠️ {len(low_vals)} unusually low values detected in '{col}'")
            # Suggest histogram if data is valid
            if col_data.nunique() > 1:
                suggested_graphs.append({
                    'column': col,
                    'type': 'histogram',
                    'title': f"Distribution of {col}",
                    'x': col
                })
        # Date columns
        elif is_datetime64_any_dtype(col_data) or pd.api.types.infer_dtype(col_data, skipna=True) in ['datetime', 'date']:
            dates = pd.to_datetime(col_data, errors='coerce').dropna()
            if not dates.empty:
                oldest = dates.min()
                most_recent = dates.max()
                insights.append(f"📅 {col.replace('_', ' ')}: from {oldest.date()} to {most_recent.date()}")
                # Monthly trend
                monthly = dates.dt.to_period('M').value_counts().sort_index()
                if not monthly.empty:
                    top_month = monthly.idxmax()
                    count = monthly.max()
                    insights.append(f"📈 Most records in {col.replace('_', ' ')}: {top_month} ({count} records)")
                    # Suggest line graph if data is valid
                    if len(monthly) > 1:
                        suggested_graphs.append({
                            'column': col,
                            'type': 'line',
                            'title': f"Monthly Trend for {col}",
                            'x': monthly.index.astype(str).tolist(),
                            'y': monthly.values.tolist(),
                            'xlabel': 'Month',
                            'ylabel': 'Count'
                        })
            else:
                insights.append(f"⚠️ Column '{col}' could not be parsed as dates or has no valid date data.")
        # Categorical columns
        elif is_categorical_dtype(col_data) or col_data.dtype == object:
            mode = col_data.mode().iloc[0] if not col_data.mode().empty else None
            freq = col_data.value_counts(normalize=True) * 100
            if mode is not None:
                percent = freq[mode] if mode in freq else 0
                insights.append(f"🧠 Most common value in '{col}' is '{mode}' ({percent:.1f}%)")
            if col_data.nunique() <= 20 and col_data.nunique() > 1:
                value_dist = col_data.value_counts().to_dict()
                insights.append(f"📌 Distribution in '{col}': {value_dist}")
                # Suggest pie chart if data is valid
                suggested_graphs.append({
                    'column': col,
                    'type': 'pie',
                    'title': f"Distribution of {col}",
                    'labels': list(value_dist.keys()),
                    'values': list(value_dist.values())
                })
    if not insights:
        insights.append("No significant insights found. Try uploading a richer dataset.")
    return insights, suggested_graphs
