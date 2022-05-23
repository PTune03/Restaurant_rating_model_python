import openpyxl
import requests
from bs4 import BeautifulSoup
import json
import numpy
from sklearn.linear_model import LinearRegression

# Считывание данных data_lrn
f = open("Tables/dataset_modelv2.txt")
temp = []
data_lrn = []
result_lrn = []
for i in range(915):
    temp.append(f.readline().replace(',','.').replace('\n',"").split('\t'))
    for j in range(5):
        data_lrn.append(temp[i][j])

for i in range(5*915):
    data_lrn[i] = int(data_lrn[i])
# for i in range(4,915*5,5):

    # data_lrn[i] = 20*(data_lrn[i]**0.5)*(2.72**(1100/(data_lrn[i] + 1100)))

temp = []
data_test = []
for i in range(915,1015):
    temp.append(f.readline().replace(',', '.').replace('\n', "").split('\t'))
    for j in range(5):
        data_test.append(temp[i - 915][j])
for i in range(5*100):
    data_test[i] = int(data_test[i])

# for i in range(4,5*100,5):
#     data_test[i] = data_test[i]*(2.72**(-data_test[i]))



# Считывание данных result
f = open("Tables/dataset_resultv2.txt")

for i in range(915):
    result_lrn.append(float(f.readline().replace('\n','').replace(',','.')))

result_test = []

for i in range(915,1015):
    result_test.append(float(f.readline().replace('\n', '').replace(',', '.')))


x_lrn = numpy.array(data_lrn).reshape((-1,5))
model = LinearRegression().fit(x_lrn,result_lrn)

r_sq = model.score(x_lrn, result_lrn)
print(f"coefficient of determination: {r_sq}")

# print(f"intercept: {model.intercept_}")
# print(f"coefficients: {model.coef_}")

x_test = numpy.array(data_test).reshape((-1,5))
y_pred = model.predict(x_test)
print(f"Results:\n {y_pred}")
print(len(y_pred))
print("min is:",min(y_pred))
print("max is:",max(y_pred))
res = []
for i in range(100):
    res.append(y_pred[i])
for i in range(100):
    res[i] = round(res[i], 1)
    res[i] = round(res[i]- 0.239,1)




