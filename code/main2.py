from cube import RubikCube
from genetic import genetic


coso = genetic(1,1,1,1,1)
print(coso)
cubo = coso[1]
print(cubo.getHistory())
print(cubo.ui())
print("MAX: ", RubikCube().getScore())

# TODO: pasarle un history inicial para que resuelva ESE cubo, es decir, siempre partiendo de esos x movimientos ya hechos, que intente resolver. Si no la solución que va a encontrar siempre es: hacer 2 movimientos.
# TODO: probar por separado que cada función del Genetic haga exactamente lo que se espera que haga.


cube2 = RubikCube()
cube2.logs = True
cube2.applyMovements([0, 1, 1, 2, 8, 6, 5, 9, 11, 11, 6, 8, 10, 7, 9, 0, 8, 8, 9, 6, 3, 2, 8, 11, 6, 0, 5, 9, 8, 11])
cube2.ui()
print(cube2.getHistory())
print(cube2.getScore())