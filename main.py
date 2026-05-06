import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = 'crime_with_ses.csv'
OUTPUT_PLOT = 'poverty_correlation.png'

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find {file_path}")
    df = pd.read_csv(file_path, low_memory=False)
    df.columns = df.columns.str.strip() 
    return df

def generate_visuals(df):
    print(f"Columns found: {list(df.columns)}")
    print("Generating correlation plot...")
    
    plt.figure(figsize=(12, 7))
    plt.scatter(df['POV_2020-2024'], df['crime_count'], alpha=0.6, edgecolors='w')
    
    plt.title('Chicago: Crime Count vs. Poverty Rate (2020-2024)')
    plt.xlabel('Poverty Rate (%)')
    plt.ylabel('Total Crimes')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.savefig(OUTPUT_PLOT)
    print(f"Success! Plot saved as {OUTPUT_PLOT}")

def main():
    try:
        data = load_data(INPUT_FILE)
        generate_visuals(data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()