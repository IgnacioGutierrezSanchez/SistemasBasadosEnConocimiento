def add(entrada, motor):
    partes = entrada.split()
    if len(partes) == 3:
        hecho = partes[1]
        grado_verdad = float(partes[2].strip('[]'))
        motor.add_hecho(hecho, grado_verdad)
    elif len(partes) == 2:
        hecho = partes[1]
        motor.add_hecho(hecho, 1.0)
    else:
        print("Error: formato incorrecto para agregar hecho.")


def pregunta(entrada, consulta, grado_verdad, reglas_aplicadas, configuracion):
    if grado_verdad is None:
        print("No")
    else:
        # Mostrar la explicación (reglas aplicadas)
        print(f"Reglas aplicadas para {consulta}:")
        for regla in reglas_aplicadas:
            print(f" - {regla}")

        # Mostrar la respuesta con el formato de rango configurado
        rangos = configuracion['rangos_respuesta']
        if grado_verdad == 1:
            print(f"Sí, completamente ({grado_verdad})")
        elif grado_verdad >= rangos['mucho']:
            print(f"Sí, mucho ({grado_verdad})")
        elif grado_verdad >= rangos['algo']:
            print(f"Sí, algo ({grado_verdad})")
        else:
            print(f"Sí, pero poco ({grado_verdad})")