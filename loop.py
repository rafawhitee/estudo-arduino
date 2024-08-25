import pyfirmata

# Configura a conexão com o Arduino
board = pyfirmata.Arduino('COM3')

# Inicializa o iterador para evitar problemas com a comunicação serial
it = pyfirmata.util.Iterator(board)
it.start()

# Configura a porta digital 2 como saída
led = board.get_pin('d:2:o')

# Função para controlar o LED
def controlar_led(estado):
    led.write(estado)

# Loop para controlar o LED
try:
    while True:
        comando = input("Digite 1 para ligar o LED ou 0 para desligar: ")
        if comando == '1':
            controlar_led(1)
            print("LED ligado")
        elif comando == '0':
            controlar_led(0)
            print("LED desligado")
        else:
            print("Comando inválido, tente novamente.")
except KeyboardInterrupt:
    print("Programa finalizado.")
finally:
    board.exit()
