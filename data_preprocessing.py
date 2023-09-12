import pandas as pd

df = pd.read_csv('weatherHistory.csv')

if __name__ == '__main__':
    print(df.head())
    print(df.columns)
    print('\n', df.dtypes)
    print('\n', df.Summary.unique())

    nan_rows = df[df['Precip Type'].isna()]
    unique_daily_summaries = nan_rows['Daily Summary'].unique()

    print('\n', unique_daily_summaries)
    print('\n', df['Formatted Date'].str[24:].unique())

    are_duplicates = df.duplicated()
    duplicate_count = are_duplicates.sum()

    print("Liczba duplikatów:", duplicate_count)
    duplicate_rows = df[df.duplicated()]
    print(duplicate_rows)

df = df.drop_duplicates()

df.reset_index(drop=True, inplace=True)
## Przygotowanie danych
# Usuń offset czasowy
df['Timezone'] = df['Formatted Date'].str[24:]
df['encode_date'] = df['Formatted Date'].str[:-6]

# Przekształcenie kolumny "Formatted Date" na obiekt daty i czasu
df['Formatted Date'] = pd.to_datetime(df['encode_date'],
                                      format='%Y-%m-%d %H:%M:%S.%f')

df['encode_month'] = df['Formatted Date'].dt.month
df['encode_day'] = df['Formatted Date'].dt.month + df[
    'Formatted Date'].dt.day / 100
df['encode_season'] = df['Formatted Date'].dt.month + df[
    'Formatted Date'].dt.day / 100
df['encode_season_1'] = df['encode_season'].apply(lambda x: (
    1 if 1 <= x <= 3.19 else
    2 if 3.20 <= x <= 6.20 else
    3 if 6.21 <= x <= 9.21 else
    4 if 9.22 <= x <= 12.20 else
    1  # Grudzień (12)
))
df['encode_season_2'] = df['encode_season'].apply(lambda x: (
    1 if 1 <= x <= 2 else
    2 if 3 <= x <= 5 else
    3 if 6 <= x <= 8 else
    4 if 9 <= x <= 11 else
    1  # Grudzień (12)
))
df['encode_season_3'] = df['encode_season'].apply(lambda x: (
    1 if 1 <= x <= 3 else
    2 if 4 <= x <= 6 else
    3 if 7 <= x <= 9 else
    4 if 10 <= x <= 12 else
    1  # Grudzień (12)
))


# Usuń zbędne kolumny
df = df.drop(columns=['Loud Cover', 'Daily Summary', 'Apparent Temperature (C)',
                      'Summary', 'Precip Type'])
df = df.drop(columns=['encode_season_1', 'encode_season_2'])

y = df['Temperature (C)']
X = df.drop('Temperature (C)', axis=1)


