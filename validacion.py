
def validar_entero_positivo(x: int) -> bool:
    """
    Evalúa si un número entero es mayor a cero.
    
    Argumentos:
        x (int): El número a verificar.
    Retorna:
        bool: True si x > 0, False en caso contrario.
    """
    try:
        return x > 0
    except (ValueError, TypeError):
        return False

def validar_numero_no_negativo(x: float) -> bool:
    """
    Determina si un número (entero o flotante) es cero o positivo.
    
    Argumentos:
        x (float): El número a evaluar.
    Retorna:
        bool: True si x es mayor o igual a 0.
    """
    try:
        return x >= 0
    except (ValueError, TypeError):
        return False

def validar_string_no_vacio(s: str) -> bool:
    """
    Comprueba si una cadena de texto contiene caracteres visibles,
    ignorando los espacios en blanco adicionale
    
    Argumentos:
        s (str): La cadena a verificar.
    Retorna:
        bool: True si la cadena tiene contenido tras eliminar espacios.
    """
    try:
        return len(s.strip()) > 0
    except (ValueError, TypeError):
        return False

def normalizar_string(s: str) -> str:
    """
    Estandariza una cadena eliminando espacios en los extremos y 
    convirtiéndola totalmente a minúsculas.
    
    Argumentos:
        s (str): La cadena original.
    Retorna:
        str: La cadena limpia y en minúsculas.
    """
    try:
        return s.strip().lower()
    except (ValueError, TypeError):
        return False

def validar_opcion(valor: str, opciones_validas: list[str]) -> bool:
    """
    Verifica si un valor específico se encuentra dentro de una lista 
    de opciones permitidas.
    
    Argumentos:
        valor (str): El dato a buscar.
        opciones_validas (list): Lista de valores permitidos.
    Retorna:
        bool: True si el valor existe en la lista.
    """
    try:
        return valor in opciones_validas
    except (ValueError, TypeError):
        return False

def validar_booleano_str(valor: str) -> bool:
    """
    Valida si una cadena de texto puede interpretarse como un valor booleano,
    como 'true', 'false', 'si', 'no', '1' o '0'.
    
    Argumentos:
        valor (str): El texto a evaluar.
    Retorna:
        bool: True si el texto es una representación booleana válida.
    """
    try:
        opciones = ['true', 'false', 'si', 'no', '1', '0']
        return valor.lower() in opciones
    except (ValueError, TypeError):
        return False

def convertir_booleano_str(valor: str) -> bool:
    """
    Transforma una cadena de texto validada en su valor booleano real.
    
    Argumentos:
        valor (str): Texto como 'true', 'si' o '1'.
    Retorna:
        bool: True para afirmaciones, False para negaciones.
    """
    try:
        return valor.lower() in ['true', 'si', '1']
    except (ValueError, TypeError):
        return False

def validar_cantidad_campos(partes: list[str], cantidad_esperada: int) -> bool:
    """
    Verifica que una lista de datos (obtenida usualmente de un archivo) 
    tenga exactamente el número de elementos requeridos.
    
    Argumentos:
        partes (list): La lista de campos procesados.
        cantidad_esperada (int): El número correcto de campos.
    Retorna:
        bool: True si la longitud de la lista coincide con la esperada.
    """
    try:
        return len(partes) == cantidad_esperada
    except (ValueError, TypeError):
        return False

def validar_rango(x: float, minimo: float, maximo: float) -> bool:
    """
    Comprueba si un valor numérico se encuentra dentro de los límites
    mínimo y máximo definidos (inclusive).
    
    Argumentos:
        x (float): El valor a evaluar.
        minimo (float): El límite inferior.
        maximo (float): El límite superior.
    Retorna:
        bool: True si el valor está dentro del rango.
    """
    try:
        return minimo <= x <= maximo
    except (ValueError, TypeError):
        return False