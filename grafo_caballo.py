from __future__ import annotations

def posicion_valida(posicion: tuple[int,int], n:int)-> list[tuple[int,int]]:
    
    A , B = posicion 
    posiciones = [
        (A+1, B +2),
        (A-1, B +2),
        (A+1, B -2),
        (A-1, B -2),
        (A+2, B +1),
        (A+2, B -1),
        (A-2, B +1),
        (A-2, B -1),
    ]
    
    Posibles_posiciones = []
    
    for posicion in posiciones:
        A_text, B_test = posicion
        if 0 <= A_text < n and 0 <= B_test < n:
            Posibles_posiciones.append(posicion)
    return Posibles_posiciones

def completo(tablero: list[list[int]]) -> bool:
    return not any(elemento == 0 for f in tablero for elemento in f)

def apertura_caballo_ayuda(tablero:list[list[int]], pos: tuple[int, int], curr: int) -> bool:
    if completo(tablero):
        return True
    
    for posicion in posicion_valida(pos, len(tablero)):
        A, B = posicion
        
        if tablero[A][B] == 0:
            tablero[A][B] = curr +1
            if apertura_caballo_ayuda(tablero, posicion, curr +1):
                return True
            tablero[A][B] = 0
    return False

def apertura_caballo(n:int)-> list[list[int]]: 
    tablero = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range (n):
            tablero[i][j] = 1
            if apertura_caballo_ayuda(tablero, (i,j),1):
                print(tablero)
            tablero[i][j] = 0
        
    raise ValueError(f"No se puede realizar la apertura con el caballa en el tablero de tamaño {n}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()