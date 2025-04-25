def exchange_money(budget, rate):
    return budget / rate

while True:
    try:
        budget = float(input("Ingrese el Monto = "))
        rate = float(input("Ingrese el Rate de la Moneda = "))
        print("Resultado: {:.2f} USD".format(exchange_money(budget, rate)))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue

    otra = input("¿Desea calcular otra conversión? (si/no): ").strip().lower()
    if otra != "si":
        print("Gracias por usar el conversor. ¡Hasta luego!")
        break