from matplotlib.pyplot import plt
import seaborn as sns


class PlotHist():
    def __init__(self,df,column_name):
        self.column_name = column_name 
        self.df = df

    def plot_histogram(self,df,column_name):
        plt.figure(figsize=(8,5))
        sns.histplot(df[column_name],kde=True)
        plt.title(f"Distribution of {column_name}")

        col_mean = df[column_name].mean()
        col_median = df[column_name].median()

        plt.axvline(col_mean,color='red',linestyle='--',label='Mean')
        plt.axvline(col_median, color='green',linestyle='-',label="Median")

        plt.legend()
        plt.show()