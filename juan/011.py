from datetime import datetime, timedelta
import math

def calcular_valor(tempo_total):
    # Regras:
    # - Diária: R$ 60,00
    # - Hora: R$ 12,00
    # - Fração de 15 min: R$ 3,00

    minutos = tempo_total.total_seconds() / 60
    horas = minutos / 60

    if horas >= 12:  
        dias = math.ceil(horas / 24)
        return dias * 60.00

    
    horas_completas = int(horas)
    minutos_restantes = minutos - (horas_completas * 60)
    fracoes = math.ceil(minutos_restantes / 15)

    valor = (horas_completas * 12.00) + (fracoes * 3.00)
    return valor

def main():
    print("=== SISTEMA DE ESTACIONAMENTO ===")
    
    placa = input("Digite a placa do veículo: ").upper()
    
    entrada_str = input("Digite a data e hora de ENTRADA (formato: dd/mm/aaaa hh:mm): ")
    saida_str = input("Digite a data e hora de SAÍDA (formato: dd/mm/aaaa hh:mm): ")

    
    entrada = datetime.strptime(entrada_str, "%d/%m/%Y %H:%M")
    saida = datetime.strptime(saida_str, "%d/%m/%Y %H:%M")

    
    tempo_total = saida - entrada

  
    valor_total = calcular_valor(tempo_total)

  
    print("\n===== TICKET DE ESTACIONAMENTO =====")
    print(f"Placa do veículo: {placa}")
    print(f"Data de entrada: {entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Data de saída:   {saida.strftime('%d/%m/%Y %H:%M')}")
    print(f"Tempo total:     {tempo_total}")
    print(f"Valor a pagar:   R$ {valor_total:.2f}")
    print("====================================")

if __name__ == "__main__":
    main()

