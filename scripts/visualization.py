import pandas as pd
import matplotlib.pyplot as plt

def create_visualizations(input_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Plot Age vs TSH level
    plt.scatter(df['Age'], df['TSH'])
    plt.xlabel('Age')
    plt.ylabel('TSH Level')
    plt.title('Age vs TSH Level')
    plt.savefig('results/age_vs_tsh.png')
    plt.show()

if __name__ == "__main__":
    input_file = 'results/cleaned_data.csv'
    create_visualizations(input_file)
