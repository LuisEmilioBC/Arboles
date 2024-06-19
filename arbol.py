from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecho)

    def in_order_traversal(self):
        self._in_order_traversal_recursivo(self.raiz)

    def _in_order_traversal_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._in_order_traversal_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.valor)
            self._in_order_traversal_recursivo(nodo_actual.derecho)
            
    def pre_order(self):
        self._pre_order_recursivo(self.raiz)
    
    def _pre_order_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor)
            self._pre_order_recursivo(nodo_actual.izquierdo)
            self._pre_order_recursivo(nodo_actual.derecho)
        
    def post_order(self):
        self._post_order_recursivo(self.raiz)
    
    def _post_order_recursivo(self,nodo_actual):
        if nodo_actual is not None:
            self._post_order_recursivo(nodo_actual.izquierdo)
            self._post_order_recursivo(nodo_actual.derecho)
            print(nodo_actual.valor)

    def buscar_nodo(self, valor):
        if (nodo := self._buscar_recursivo(self.raiz, valor)):
            print(f'El valor {nodo.valor} se encuentra en el árbol')
        else:
            print('Valor no encontrado')
    
    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is not None:
            if nodo_actual.valor == valor:
                return nodo_actual
            elif nodo_actual.valor >= valor:
                return self._buscar_recursivo(nodo_actual.izquierdo, valor)
            else:
                return self._buscar_recursivo(nodo_actual.derecho,valor)
        return
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # no tiene hijos)
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # tiene un solo hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            # tiene dos hijos
            else:
                sucesor = self._encontrar_minimo(nodo.derecho)
                nodo.valor = sucesor.valor
                nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)

        return nodo

    def buscar_minimo(self):
        if (minimo := self._encontrar_minimo(self.raiz)):
            return minimo.valor
        else:
            return "La lista está vacía"
    
    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    def buscar_maximo(self):
        if (maximo := self._encontrar_maximo(self.raiz)):
            return maximo.valor
        else:
            return "La lista está vacía"
    
    def _encontrar_maximo(self, nodo):
        actual = nodo
        while actual.derecho is not None:
            actual = actual.derecho
        return actual
    
    def altura_arbol(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if nodo is not None:
            altura_izquierda = self._altura_recursiva(nodo.izquierdo)
            altura_derecha = self._altura_recursiva(nodo.derecho)
            if altura_izquierda > altura_derecha:
                return 1 + altura_izquierda
            else:
                return 1 + altura_derecha
        else:
            return 0
    
    def convertir_lista(self):
        return self._lista_recursiva(self.raiz)
    
    def _lista_recursiva(self, nodo_actual):
        lista = []
        if nodo_actual is not None:
            lista += self._lista_recursiva(nodo_actual.izquierdo)
            lista.append(nodo_actual.valor)
            lista += self._lista_recursiva(nodo_actual.derecho)
        return lista
    
    