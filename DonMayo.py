class CafeDonMayo:
    def __init__(self, nombreProyecto:str, desarolladores: list ):
        self.nombreProyecto = nombreProyecto
        self.desarolladores = desarolladores

    


class Desarrollador:
    def __init__(self, nombre:str, apellido:str, apellido2:str, carnet:str, grado:str, horasLaboradas:int):
        self.nombre = nombre
        self.apellido = appellido
        self.apellido2 = apellido2
        self.carnet = carnet
        self.grado = grado
        self.horasLaboradas  = horasLaboradas
    
    def creditosEstudiantiles(self):
        grado = 0
        if self.grado == "tecnico":
            grado = 0.25
        if self.grado == "diplomado":
            grado = 0.35        
        if self.grado == "bachillerato":
            grado = 0.45
        return grado

    def creditosAColones (self):
        descuento = 0
        if self.horasLaboradas >= 10:
                descuento = self.horasLaboradas * 1000
            if self.grado == "diplomado":
                descuento = self.horasLaboradas * 1250        
            if self.grado == "bachillerato":
                descuento = self.horasLaboradas * 2500
        return descuento

    def creditosObtenidos(self):
        self.horasLaboradas * self.creditosEstudiantiles
        

desarollador1 = Desarrollador("milton", "baltodano", "medina", 701860575, "tecnico", 5)
desarollador2 = Desarrollador("Paquito", "DelBarrio", "Guzman", 500526075, "bachillerato", 20)
desarollador3 = Desarrollador("Elsa", "Pito", "Brinco", 30050075, "diplomado", 60)

list_desarrolladores = [desarollador1, desarollador2, desarollador3]

print(desarollador1.creditosAColones())
print(desarollador1.creditosObtenidos())
