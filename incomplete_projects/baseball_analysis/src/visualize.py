import seaborn as sns
import matplotlib.pyplot as plt

def plot_hr_distribution(df):
    sns.histplot(df["hr"], bins=20)
    plt.title("Home Runs Distribution")
    plt.show()

