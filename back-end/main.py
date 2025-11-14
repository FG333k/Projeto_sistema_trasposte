import random

class VeiculoTrasporte:
    def __init__(self,tipo,tarifa_basica):
        self.tipo = tipo
        self.tarifa_basica = tarifa_basica

    def calcularTarifa(): 
        pass

    def calcularTempoEspera(self):
        pass

class Onibus(VeiculoTrasporte):
    def __init__(self,linha):      
        super().__init__(tipo= f'Ônibus (Linha: {linha})', tarifa_basica=4.50)
        self.linha = linha

    def calcularTarifa(self):
        return self.tarifa_basica

    def calcularTempoEspera(self):
        tempo = random.randint(5,20)
        return f'{tempo} min (trânsito muito cheio)'

class Metro(VeiculoTrasporte):
    def __init__(self,linha):      
        super().__init__(tipo= f'metrô (Linha: {linha})', tarifa_basica=5.00)
        self.linha = linha
        self.tarifaPor_km = 0.25