import random
from datetime import datetime, timedelta

class Trasporte:
    def __init__(self, tipo: str, tarifa_base: float, capacidade: int):

        # Atributos padrão
        self.tipo = tipo
        self.tarifa_basica = tarifa_base
        self.capacidade = capacidade
        self.velocidade_media = 0
        
    # Métodos padrão (abstratos)
    def calcular_tarifa(self, distancia: float = 0, **kwargs) -> float: 
        return NotImplementedError("Deve ser implementado nas subclasses")

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        return NotImplementedError("Deve ser implementado nas subclasses")
    

class Onibus(Trasporte):
    def __init__(self,capacidade, velocidade_media, tarifa):
        tipo = "Onibûs"
        super().__init__(tipo, tarifa, capacidade)
        self.capacidade = capacidade
        self.velocidade_media = velocidade_media
        self.tarifa = 0
        

    def calcularTarifa(self, valor_transporte_padrao): 
        self.tarifa = valor_transporte_padrao
        print(f"Onibûs(tarifa padão): {self.tarifa}")

    def calcularTempoEspera(self, distancia):
        return NotImplementedError("Deve ser implementado nas subclasses")


class Metro(Trasporte):
    def __init__(self, tipo, tarifa_base, capacidade):
        super().__init__(tipo, tarifa_base, capacidade)



class Trem(Trasporte):
    def __init__(self, tipo, tarifa_base, capacidade):
        super().__init__(tipo, tarifa_base, capacidade)



class Barco(Trasporte):
    def __init__(self, tipo, tarifa_base, capacidade):
        super().__init__(tipo, tarifa_base, capacidade)

class Sistema_transporte:
    def __init__(self):
        self.veiculos = {
            'onibus': Onibus(),
            'metro': Metro(),
            'trem': Trem(),
            'barco': Barco()
        }

    def calcular_viagem(self, tipo_veiculo: str, distancia: float = 0, **kwargs):
        if(tipo_veiculo not in self.veiculos):
            raise ValueError(f"Tipo de veículo não suportado: {tipo_veiculo}")
        
        veiculo = self.veiculos[tipo_veiculo]
        hora_atual = datetime.now()

        tarifa = veiculo.calcular_tarifa(distancia, **kwargs)
        tempo_espera = veiculo.calcular_tempo_espera(hora_atual)

        if(distancia > 0 and veiculo.veloricade_media > 0):
            tempo_viagem = timedelta(hours=distancia / veiculo.velocidade_media)
        else:
            tempo_viagem = timedelta(minutes=15)

        return {
            'veiculo': veiculo.tipo,
            'tarifa': tarifa,
            'tempo_espera': tempo_espera,
            'tempo_viagem': tempo_viagem,
            'chegada_estimada': hora_atual + tempo_espera + tempo_viagem
        }

# T1 = Trasporte("Defaut", 0, 0)
# T1.calcularTempoEspera(200)

# O1 = Onibus("Onibûs", 45, 75, T1.get_tarifa_padrao())
# print(O1.tarifa)
# O1.calcularTarifa(T1.get_tarifa_padrao())