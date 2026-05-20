def func(value, values):
    var = 1
    values[0] = 44
t = 3
v = [1, 2 , 3]
func(t , v)
print(t, v[0])

def f(i, values = []):
    values.append(i)
    print (values)
f(1)
f(2)
f(3)