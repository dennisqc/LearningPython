archivo_log = 'sample_data/delosi/logs.txt'



def contar_errores_log(archivo_log):
    conteo_errores_log={"error":0, "warning":0, "info":0}
    
    try:
        with open(archivo_log, 'r') as file:
            for linea in file:
                if 'ERROR' in linea:
                    conteo_errores_log["error"] += 1
                if 'WARNING' in linea:  
                    conteo_errores_log["warning"] += 1
                if 'INFO' in linea:
                    conteo_errores_log["info"] += 1
    except FileNotFoundError:
        print(f"El archivo {archivo_log} no fue encontrado.")
        return None
    return conteo_errores_log
    
resultado = contar_errores_log(archivo_log)
if resultado:
    print("Conteo de errores en el log:")
    print(f"Errores: {resultado['error']}")
    print(f"Advertencias: {resultado['warning']}")
    print(f"Información: {resultado['info']}")  