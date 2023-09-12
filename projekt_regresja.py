import data_preprocessing as dp
import data_visualization as dv
# import data_preprocessing as dp
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import plotly.express as px
# import plotly.graph_objects as go
# from sklearn.preprocessing import PolynomialFeatures
# from datetime import datetime

df = dp.df
print(df)
df = dv.df
#
# # Zmienna zależna 'Objaśniana': (y), zmienna niezależna 'Objaśniana': (X)
# X = df[['Size']]
# y = df.Price
# # Przygotowanie danych testowych i treningowych
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
#                                                     random_state=1)
# # Przygotowanie danych walidacyjnych i treningowych
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,
#                                                   test_size=0.2,
#                                                   random_state=1)
# # Wytrenowanie modelu
# model = LinearRegression()
# model.fit(X_train, y_train)
# # Sprawdz wartosc wyrazu wolnego i wspolczynnikow regresji
# print(f'Wyraz wolny (theta_0): {model.intercept_}')  # wyraz wolny theta_0
# # Współczynniki regresji
# print(f' Współczynniki regresji (theta_1): {model.coef_}')  # theta_1
# # Wykres zależności Size, Price i prosta Regresji
# x_range = np.linspace(X['Size'].min(), X['Size'].max(), 50)
# y_range = model.predict(x_range.reshape(-1, 1))
#
# fig = px.scatter(x=X['Size'], y=y, opacity=0.7)
# fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
# # fig.show()
# """ Alternatywny sposób:
# plt.scatter(X,y,color='red')
# plt.plot(X,model.predict(X),color='green')
# plt.title('Price vs Size')
# plt.xlabel('Size')
# plt.ylabel('Price')
# plt.show()
# """
# # Okerślenie lini wielomianowej 3 stopnia (potęgi)
# poly = PolynomialFeatures(degree=3)
# X_poly = poly.fit_transform(X)
# print(f'Zmienna niezależna do potegi ^3: \n{X_poly[:5]}')
# model.fit(X_poly, y)
# print(f'Wyraz wolny do potęgi ^3 (theta_0): {model.intercept_}')
# print(f' Współczynniki regresji potęgi ^3 (theta_1) "Teraz tablica": {model.coef_}')
# # Predict = przewidywane.  Przypisanie danych testowych i trenowanie
# y_test = y_test.values.reshape(-1, 1)
# predict_data_poly = poly.transform(y_test)
# print(f'Dane przewidywane/testowe: \n{predict_data_poly}')
# model_predict = model.predict(predict_data_poly)
# print(f'Dane przewidywane/testowe przetestowene: {model_predict}')
# # Wykres zależności Size, Price i linia wielomianowa (3)
# x_range=np.linspace(X['Size'].min(),X['Size'].max(),50)
# y_range=model.predict(poly.fit_transform(x_range.reshape(-1,1)))
#
# fig=px.scatter(x=X['Size'],y=y,opacity=0.7)
# fig.add_traces(go.Scatter(x=x_range,y=y_range,name='Polynomial Regression Fit'))
# fig.show()
#
# def mse(y_pred, y):  # średni błąd kwadratowy
#     return np.mean((y_pred - y) ** 2)
#
#
# predict_train = (model.predict(X_train))
# predict_test = (model.predict(X_test))
#
# print(df[35:])
#
# print(pd.DataFrame({"y_test": np.squeeze(y_test),
#                     "Predykcja": np.round(np.squeeze(predict_test),
#                                           decimals=2)}))
#
# print(model.intercept_)
# print(model.coef_)
#
# # fig, ax = plt.subplots()
# #
# # ax.scatter(df.Size, df.Price)
# # plt.title('Ceny mieszkań')
# # plt.xlabel('Wielkość')
# # plt.ylabel('Cena')
# # plt.grid()
# # plt.legend(df)
# # plt.show()
#
# sns.lmplot(data=df,
#            x='Size',
#            y='Price', )
# # plt.show()
