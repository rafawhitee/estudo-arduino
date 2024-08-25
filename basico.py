import pyfirmata
import time

# Defina a porta serial correta para o seu Arduino
# Exemplo: 'COM3' no Windows ou '/dev/ttyACM0' no Linux
board = pyfirmata.Arduino('COM3')

# Defina a porta digital 2 como saída
digital_pin = board.get_pin('d:2:o')

# Acender a porta digital 2
digital_pin.write(1)

# Aguarde um tempo (5 segundos neste exemplo)
time.sleep(5)

# Desligar a porta digital 2
digital_pin.write(0)

# Finalizar a comunicação
board.exit()