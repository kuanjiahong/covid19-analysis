import pandas as pd
import matplotlib.pyplot as plt

# Global variable
df = pd.read_csv('enhanced_sur_covid_19_eng.csv')
# Convert the Report date column to datetime64
df['Report date'] = pd.to_datetime(df['Report date'], dayfirst=True, format='%d/%m/%Y')
# Convert the HK/Non-HK resident column to category
df['HK/Non-HK resident'] = df['HK/Non-HK resident'].astype('category')


def n_by_resident():
    resident = df['HK/Non-HK resident'].value_counts()
    resident.plot(kind='bar', title='Number of cases by HK/Non-HK resident')
    plt.xlabel('X axis: HK/Non-HK resident')
    plt.xticks(rotation=0)
    plt.ylabel('Y axis: Number of cases')
    plt.tight_layout()
    plt.show()


def year_2020_vs_resident_case():
    df_2020 = df[df['Report date'].dt.year == 2020].copy()
    df_2020['Month'] = df_2020['Report date'].dt.month
    grouped = df_2020.groupby(['Month', 'HK/Non-HK resident']).size().reset_index(name='Count')
    pivot_data = grouped.pivot(index='Month', columns='HK/Non-HK resident', values='Count')
    pivot_data.plot(kind='bar', title='Number of cases by HK/Non-HK resident in 2020')
    plt.xlabel('X axis: Month')
    plt.xticks(rotation=0)
    plt.ylabel('Y axis: Number of cases')
    plt.tight_layout()
    plt.show()


def main():
    n_by_resident()
    year_2020_vs_resident_case()


if __name__ == '__main__':
    main()