from typing import final

@final
class Base:
    pass

# Un linter (como MyPy) marcará esto como ERROR:
class Derivada(Base):
    pass

b = Base()
print("Clase Base instanciada correctamente")