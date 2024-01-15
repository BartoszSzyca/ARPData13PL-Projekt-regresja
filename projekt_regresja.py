import data_preprocessing as dp
import data_visualization as dv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime

df = dp.df
print(df)
df = dv.df

X = df[['Size']]
y = df.Price

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=1)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,
                                                  test_size=0.2,
                                                  random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

print(f'Wyraz wolny (theta_0): {model.intercept_}')

print(f' Współczynniki regresji (theta_1): {model.coef_}')

x_range = np.linspace(X['Size'].min(), X['Size'].max(), 50)
y_range = model.predict(x_range.reshape(-1, 1))

fig = px.scatter(x=X['Size'], y=y, opacity=0.7)
fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
fig.show()

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
print(f'Zmienna niezależna do potegi ^3: \n{X_poly[:5]}')
model.fit(X_poly, y)
print(f'Wyraz wolny do potęgi ^3 (theta_0): {model.intercept_}')
print(f' Współczynniki regresji potęgi ^3 (theta_1) "Teraz tablica": {model.coef_}')

y_test = y_test.values.reshape(-1, 1)
predict_data_poly = poly.transform(y_test)
print(f'Dane przewidywane/testowe: \n{predict_data_poly}')
model_predict = model.predict(predict_data_poly)
print(f'Dane przewidywane/testowe przetestowene: {model_predict}')

x_range=np.linspace(X['Size'].min(),X['Size'].max(),50)
y_range=model.predict(poly.fit_transform(x_range.reshape(-1,1)))

fig=px.scatter(x=X['Size'],y=y,opacity=0.7)
fig.add_traces(go.Scatter(x=x_range,y=y_range,name='Polynomial Regression Fit'))
fig.show()

def mse(y_pred, y):  # średni błąd kwadratowy
    return np.mean((y_pred - y) ** 2)


predict_train = (model.predict(X_train))
predict_test = (model.predict(X_test))

print(df[35:])

print(pd.DataFrame({"y_test": np.squeeze(y_test),
                    "Predykcja": np.round(np.squeeze(predict_test),
                                          decimals=2)}))

print(model.intercept_)
print(model.coef_)

fig, ax = plt.subplots()

ax.scatter(df.Size, df.Price)
plt.title('Ceny mieszkań')
plt.xlabel('Wielkość')
plt.ylabel('Cena')
plt.grid()
plt.legend(df)
plt.show()

sns.lmplot(data=df,
           x='Size',
           y='Price', )
plt.show()
