import pandas as pd

def clean_data(input_file, output_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Drop rows with missing target values
    df = df.dropna(subset=['Diagnosis'])

    # Fill missing data in other columns with the median or mode
    df.fillna(df.median(), inplace=True)
    df.fillna(df.mode().iloc[0], inplace=True)

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_file = 'data/thyroid_data.csv'
    output_file = 'results/cleaned_data.csv'
    clean_data(input_file, output_file)
