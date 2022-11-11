from Bus import *
from Empresa import *

empresa = Empresa("Cootracosta")


empresa.AgregarBus(Bus(2344, "abd123", "Juan Perez"))
empresa.AgregarBus(Bus(1243, "cde234", "Avendaño"))


print(empresa.buses[0].numeroIdentificacion)
print(empresa.buses[0].placa)
print(empresa.buses[0].conductor)
print(empresa.buses[0].sillas)

print(empresa.buses[1].numeroIdentificacion)
print(empresa.buses[1].placa)
print(empresa.buses[1].conductor)
print(empresa.buses[1].sillas)

empresa.buses[0].ModificarIdentificacion(2333)


print(empresa.buses[0].numeroIdentificacion)