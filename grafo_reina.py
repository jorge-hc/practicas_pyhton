from __future__ import annotations

def primera_busqueda(posible_tablero: list[list[int]], col_dig_dch: list[int],  col_dig_izq: list[int], tableros:list[list[str]], n:int) -> None:
    
    f = len(posible_tablero)
    
    if f == n:
        tableros.append(["."* i + "Q" + "."*(n - 1 - i) for i in posible_tablero])
        return
    
    for c in range(n):
        
        if (
            c in posible_tablero
            or f - c in col_dig_dch
            or f + c in col_dig_izq
        ):
            continue
        
        primera_busqueda(posible_tablero+[c], col_dig_dch + [f -c], col_dig_izq + [f + c], tableros, n)

def solucion(n: int) -> None:
    tableros : list[list[str]] = []
    primera_busqueda([],[],[], tableros,n)
    
    for tablero in tableros:
        for c in tablero:
            print(c)
        print(" ")
    print("la cantidad de soluciones encontradas son:", len(tableros))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    solucion(12)