def constructorAstros(tam,color,nombre,distancia,x=0,y=0,angulo=0,v_angular=0):

    if v_angular == 0:
        tipo = "estrella"
    else:
        tipo = "planeta"


    objeto = { "tipo": tipo,
               "nombre": nombre,
               "tam": tam,
               "distancia": distancia,
               "v_angular": v_angular,
               "color": color,
               "x": x,
               "y": y,
               "angulo": angulo
            }

    return objeto
