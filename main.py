import matplotlib.pyplot as plt
from scipy import stats

# veriler aylık ve 2021-09 ile 2022-09 arasında(ikisi de dahil) ve toplam 13 adet datadan oluşuyor

# ortalama USD/TL döviz alış fiyat
dolar = [8.51, 9.14, 10.52, 13.53, 13.52, 13.62, 14.57, 14.68, 15.62, 16.96, 17.39, 17.99, 18.28]
# türkiye ortalama konut birim fiyat(TL/m2)
konut = [5011.10, 5323.10, 5858.30, 6372.60, 7479.30, 8646.00, 9501.90, 10561.30, 11946.60, 13001.40, 13929.50, 15052.50, 15863.30]

slope, intercept, r, p, std_err = stats.linregress(dolar, konut)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, dolar))


def draw_scatter_plot():
    plt.scatter(dolar, konut)
    plt.show()


def draw_line_of_linear_regression():
    plt.scatter(dolar, konut)
    plt.plot(dolar, mymodel)
    plt.show()

# draw_scatter_plot()
# draw_line_of_linear_regression()


print(round(myfunc(25), 2))  # dolar 25 olursa ortalama konut birim fiyatını yazdır
print(round(myfunc(30), 2))  # dolar 30 olursa ortalama konut birim fiyatını yazdır
print(round(myfunc(35), 2))  # dolar 25 olursa ortalama konut birim fiyatını yazdır
