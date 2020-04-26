import models.LinearRegression as lr


df = lr.pd.read_csv('Datasets/house.csv')
df.columns=['size' , 'price']
x = df['size']
y = df['price']

thetas = lr.gradient(x,y)

y_fit = thetas[0] + thetas[1]*x
lr.plt.figure(figsize=(20,3))

lr.plt.scatter(x, y,s=20)
lr.plt.plot(x,y_fit,color="red")

lr.plt.show()