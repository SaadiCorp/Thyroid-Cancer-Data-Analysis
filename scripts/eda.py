import pandas as pd
import matplotlib.pyplot as plt

def perform_eda(input_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Summary statistics
    print(df.describe())

    # Diagnosis distribution
    df['Diagnosis'].value_counts().plot(kind='bar')
    plt.title('Diagnosis Distribution')
    plt.savefig('results/diagnosis_distribution.png')
    plt.show()

if __name__ == "__main__":
    input_file = 'results/cleaned_data.csv'
    perform_eda(input_file)
