import  pickle
import sys

from mapa import createMap
from trip import verificarElementos, estoEsunaPrueba



mi_Mapa = "miMapa.pkl" 
def serializacion_Esquinas_Ycalles(parametroRecibido):
    with open(parametroRecibido) as file:
        datoEsquinas = file.readline()
        datoAristasyPeso = file.readline()
        
    
    with open(mi_Mapa, "wb") as pickle_file:
        pickle.dump(datoEsquinas, pickle_file)

        pickle.dump(datoAristasyPeso, pickle_file)
    

    mapa_creado = createMap(mi_Mapa)
    return mapa_creado
        

if sys.argv[1] == "-create_map":
    try:
        map_resultado = serializacion_Esquinas_Ycalles(sys.argv[2])
        print("MAPA CREADO CORRECTAMENTE")
    except IndexError:
        print("Parametro no permitido")
       

#quiero creer que las cosas las va a cargar como: 
# fix_element : [H1, [e1,]]

if sys.argv[1] == "-create_trip":
    try:
        #aca debo de deserializar el mapa y los elementos me imagino
        #verificarElementos(sys.argv[2], sys.argv[3])
        estoEsunaPrueba(sys.argv[2], sys.argv[3])
    except:
        print("ERROR, mucha sensualidad")
        
