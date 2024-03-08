import sys

# Definir las ventas por mes
ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000,
    "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200,
    "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000
}

def nomina_ventas_mayores_a(monto):
    # Filtrar los meses cuyas ventas sean mayores al monto dado
    meses = [mes for mes, venta in ventas.items() if venta > monto]
    return meses

if __name__ == "__main__":
    # Obtener el monto de la terminal
    if len(sys.argv) != 2:
        print("!!! ERROR ... DEBE AGREGAR AL ARCHIVO UNA CIFRA...")
        sys.exit(1)
    
    monto = float(sys.argv[1])

    # Formatear el monto con separadores de miles y dos decimales
    monto_formateado = "{:,.2f}".format(monto)

    # Generar la nómina de ventas mayores al monto dado
    nominas = nomina_ventas_mayores_a(monto)

    if nominas:
        print(f"Meses con ventas mayores a {monto_formateado}:")
        for mes in nominas:
            print(mes)
    else:

        print(f"No hay meses con ventas mayores a {monto_formateado}.")
