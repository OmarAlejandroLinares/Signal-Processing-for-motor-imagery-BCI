# Función de extracción de características
def statistics_feature_extraction(x):
    import math
    import numpy as np

    vector_caracteristicas = []
    xsize = x.size
    #F1: Promedio
    promedio=x.mean()
    vector_caracteristicas.append(promedio)
    #F2: Promedio absoluto
    vector_caracteristicas.append(abs(vector_caracteristicas[0]))
    #F3: Máximo
    vector_caracteristicas.append(max(x))
    #F4: Máximo absoluto
    vector_caracteristicas.append(abs(vector_caracteristicas[2]))
    # #F5: Mínimo
    vector_caracteristicas.append(min(x))
    #F6: Mínimo absoluto
    vector_caracteristicas.append(abs(vector_caracteristicas[4]))
    #F7: Máximo + Mínimo
    vector_caracteristicas.append(vector_caracteristicas[2]+vector_caracteristicas[4])
    #F8: Máximo - Mínimo
    vector_caracteristicas.append(vector_caracteristicas[2]-vector_caracteristicas[4])

    #F9: ELIMINADA

    #F10: Longitud de curva
    sumita=0
    for i in range(xsize-1):
        sumita=sumita+abs(x[i+1]-x[i])
    vector_caracteristicas.append(sumita)
    #F11: Energía
    sumita=0
    for i in range(xsize):
        sumita=sumita+(x[i]**2)
    vector_caracteristicas.append(sumita/xsize)
    #F12: Energía no lineal promedio (ANE)
    sumita=0
    for i in range(xsize-2):
        sumita=sumita+((x[i+1]**2)-(x[i]*x[i+2]))
    vector_caracteristicas.append(sumita/xsize-2)
    #F13: Entropía espectral (SE)
    sumita=0
    for i in range(xsize):
        pk=(abs(x[i]**2))/(xsize*1.5)
        sumita=sumita+(pk*math.log2(pk))
    vector_caracteristicas.append(sumita)

    #F14: ELIMINADA

    #F15: Integral
    sumita=0
    for i in range(xsize):
        sumita=sumita+abs(x[i])
    vector_caracteristicas.append(sumita)
    #F16: Desviación estándar
    desv=x.std()
    vector_caracteristicas.append(desv)
    #F17: Varianza
    vector_caracteristicas.append(x.var())
    #F18: Oblicuidad
    sumita=0
    for i in range(xsize):
        sumita=sumita+(((x[i]-promedio)/desv)**3)
    vector_caracteristicas.append(sumita/xsize)
    #F19: Curtosis
    sumita=0
    for i in range(xsize):
        sumita=sumita+(((x[i]-promedio)/desv)**4)
    vector_caracteristicas.append(sumita/xsize)
    #F20: Sumatoria
    sumita=0
    for i in range(xsize):
        sumita=sumita+x[i]
    vector_caracteristicas.append(sumita)
    #F21: Mediana
    vector_caracteristicas.append(np.median(x))
    return vector_caracteristicas