velocidade = 61 # velocidade atual do carro
local_carro = 90 # KM em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # distância onde o radar pega

veloc_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and veloc_carro_passou_radar_1

if veloc_carro_passou_radar_1:
    print('Velocidade do carro acima do radar 1')

if carro_passou_radar_1:
    print('Carro passou do radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
