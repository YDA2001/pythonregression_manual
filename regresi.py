import mysql.connector
from tabulate import tabulate

x = []
y = []
x2 = []
y2 = []
xy = []
ape = []

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db = "datareg"
)

cur = mydb.cursor()
cur.execute("SELECT * FROM dataset")
res = cur.fetchall()

for k in res:
    x.append(k[0])
    y.append(k[1])

def sum_x():
    xs = 0
    
    for i in x:
       xs = xs + int(i)
    return (xs)
    
def sum_y():
    ys = 0
    
    for i in y:
       ys = ys + int(i)
    return (ys)
    
def sum_x2():
    x2s = 0
    
    for i in x2:
       x2s = x2s + int(i)
    return (x2s)    

def sum_y2():
    y2s = 0
    
    for i in y2:
       y2s = y2s + int(i)
    return (y2s)    
    
def sum_xy():
    xys = 0
    
    for i in xy:
       xys = xys + int(i)
    return (xys)            

def sum_const_a(y_sum, x2_sum, x_sum, xy_sum, x_data):
    a = y_sum * x2_sum
    b = x_sum * xy_sum
    c = x_data * x2_sum
    d = x_sum ** 2
    
    e = a - b
    f = c - d
    
    g = e / f
    return g
    
def sum_const_b(x_data, xy_sum, x_sum, y_sum, x2_sum):
    a = x_data * xy_sum
    b = x_sum * y_sum
    c = x_data * x2_sum
    d = x_sum ** 2
    
    e = a - b
    f = c - d
    
    g = e / f
    return g    
   
for q in range(20):
    m = int(x[q]) ** 2
    x2.append(m)
    
for w in range(20):
    m = int(y[w]) ** 2
    y2.append(m)    

for e in range(20):
    m = int(y[e]) * int(x[e])
    xy.append(m)    

for i in range(20):
    p = (int(x[i]) - int(y[i])) / int(x[i])
    p = abs(p)
    ape.append(p)
    
x_sum = sum_x()
y_sum = sum_y()
x2_sum = sum_x2()
y2_sum = sum_y2()
xy_sum = sum_xy()
x_data = len(x)
const_a = sum_const_a(y_sum, x2_sum, x_sum, xy_sum, x_data)
const_b = sum_const_b(x_data, xy_sum, x_sum, y_sum, x2_sum)
sub = input("input data yang diinginkan:")

q = const_b * int(sub)
w = const_a + q
e = w
mape = sum(ape) / len(ape)

print("x:", x)   
print("y:", y)
print("x2:", x2)
print("y2:", y2)
print("xy:", xy)
print("total x:", x_sum)
print("total y", y_sum)
print("total x2:", x2_sum)
print("total y2", y2_sum)
print("APE:", ape)
print("x:", x)   
print(const_a, "+" ,const_b, "(" ,sub, ")")
print(const_a, "+" ,q)
print(w)
print(f''' MAPE: { round(mape*100, 2) } % ''')





    
