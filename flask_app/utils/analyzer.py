import pandas as pd

def analyze_consulting_data():
    # Read the CSV file
    df = pd.read_csv('ai_sales_insight/sample_data/consulting_data.csv')
    # Remove rows with missing values
    df_clean = df.dropna()
    # Print first 5 rows
    print("First 5 rows:")
    print(df_clean.head())
    # Print list of column names
    print("\nColumn names:")
    print(list(df_clean.columns))
    # Print total number of rows after cleaning
    print(f"\nTotal number of rows after cleaning: {len(df_clean)}")

if __name__ == "__main__":
    analyze_consulting_data() 