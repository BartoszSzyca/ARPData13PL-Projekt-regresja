import data_preprocessing as dp
import matplotlib.pyplot as plt
import seaborn as sns

df = dp.df
X = dp.X
y = dp.y
print(df)

# heatmapa korelacji i wykresy
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmapa korelacji')
plt.show()

sns.pairplot(df, hue='encode_season')
plt.show()

set_time = '2008-01-01 00:00:00'
dane_filtered = df[df['Formatted Date'] < set_time]

plt.figure(figsize=(10, 6))  # Ustalamy rozmiar wykresu (opcjonalne)
plt.plot(dane_filtered['Formatted Date'], dane_filtered['Temperature (C)'], marker='o', linestyle='-')
plt.title(f'Wykres Temperatury do {set_time}')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.show()

plt.figure(figsize=(10, 6))  # Ustalamy rozmiar wykresu (opcjonalne)
plt.plot(df['Formatted Date'], df['Temperature (C)'], marker='o', linestyle='-')
plt.title('Wykres Temperatury w Czasie')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(df['Humidity'], df['Temperature (C)'], alpha=0.5)
plt.xlabel('Wilgotność')
plt.ylabel('Temperatura (C)')
plt.title('Temperatura vs Wilgotność')

sns.lmplot(df, x="Visibility (km)", y="Temperature (C)",
           line_kws={"color": "red"})
sns.lmplot(df, x="Humidity", y="Temperature (C)", line_kws={"color": "red"})
sns.lmplot(df, x="encode_season", y="Temperature (C)",
           line_kws={"color": "red"})
plt.show()
