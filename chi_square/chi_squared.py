def r3(x) :
    y = 38.47 - 48.65*x - 176.48*x**2
    return y

thetas = [-0.9,-0.7,-0.5,-0.3,-0.1,0.1,0.3,0.5,0.7,0.9]
observed = [82,50,35,27,26,60,108,188,319,519]
expected = []

for z in thetas :
    expected.append(r3(z))

chi_squared = []

for i in range(0,10) :
    a = ((observed[i] - expected[i])**2) / expected[i]
    chi_squared.append(a)

b = sum(chi_squared)
print(b)
