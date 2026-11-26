import numpy as np

def calculate(list):
    longitud = len (list)
    if longitud != 9:
        raise ValueError('List must contain nine numbers.')

    list = np.array(list)
    arreglo3x3 = list.reshape(3,3)

    #Calculamos promedio
    promedioColumnas = np.mean(arreglo3x3, axis=0)
    promedioFilas = np.mean(arreglo3x3, axis=1)
    promedioTotal = np.mean(arreglo3x3)
    resultadoPromedio = [promedioColumnas.tolist(), promedioFilas.tolist(), promedioTotal.tolist()]

    #Calculamos varianza
    varianzaColumnas = np.var(arreglo3x3, axis=0)
    varianzaFilas = np.var(arreglo3x3, axis=1)
    varianzaTotal = np.var(arreglo3x3)
    resultadoVarianza = [varianzaColumnas.tolist(), varianzaFilas.tolist(), varianzaTotal.tolist()]

    #Calculamos desviacion
    desviacionColumnas = np.std(arreglo3x3, axis=0)
    desviacionFilas = np.std(arreglo3x3, axis=1)
    desviacionTotal = np.std(arreglo3x3)
    resultadoDesviacion = [ desviacionColumnas.tolist(), desviacionFilas.tolist(), desviacionTotal.tolist()]

    #Calculamos máximos
    maximoColumnas = np.max(arreglo3x3, axis=0)
    maximoFilas = np.max(arreglo3x3, axis=1)
    maximoTotal = np.max(arreglo3x3)
    resultadoMaximo = [maximoColumnas.tolist(), maximoFilas.tolist(), maximoTotal.tolist()]

    #Calculamos mínimos
    minimoColumnas = np.min(arreglo3x3, axis=0)
    minimoFilas = np.min(arreglo3x3, axis=1)
    minimoTotal = np.min(arreglo3x3)
    resultadoMinimo = [minimoColumnas.tolist(), minimoFilas.tolist(), minimoTotal.tolist()]

    #Calculamos sumas
    sumaColumnas = np.sum(arreglo3x3, axis=0)
    sumaFilas = np.sum(arreglo3x3, axis=1)
    sumaTotal = np.sum(arreglo3x3)
    resultadoSuma = [sumaColumnas.tolist(), sumaFilas.tolist(), sumaTotal.tolist()]

    
    return {
        'mean':resultadoPromedio, 
        'variance': resultadoVarianza,
        'standard deviation': resultadoDesviacion,
        'max': resultadoMaximo,
        'min': resultadoMinimo,
        'sum': resultadoSuma
        }
