class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        data = len(self._data)
        return data

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        data = self._data.append(value)
        return data

    def dequeue(self):
        """Aqui irá sua implementação"""
        data = self._data.pop(0)
        return data

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < len(self._data):
            data = self._data[index]
            return data

        raise IndexError
