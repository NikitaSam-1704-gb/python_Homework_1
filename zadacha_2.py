# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for i in range(0, 2):
    x=i
    for j in range(0,2):
        y=j
        for k in range(0,2):
            z=k
            b=not(x and y and z) == (not(x) or not(y) or not(z))
            print(f' для {x}{y}{z}->{b}')

