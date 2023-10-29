
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _generate_hash(self, key):
        return hash(key) % self.size
    
    def insert(self, value):
        index = self._generate_hash(value)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append(value)
    
    def search(self, value):
        index = self._generate_hash(value)
        if self.table[index] is not None:
            pass
            checkValue = False
            for values in self.table[index]:
                if values == value:
                    checkValue = True
            
            print(f"{value} is found") if checkValue else print(f"{value} isn't found")
    
    def delete(self, value):
        index = self._generate_hash(value)
        if self.table[index] is not None:
            try:
                return self.table[index].remove(value)
            except:
                print(f"'{value}' isn't found")
    
    def display(self):
        arr = []
        for item in self.table:
            if item is not None:
                arr.append(item)
                
        for value in arr:
            for i in value:
                print(i)

hashTable = HashTable(10)
hashTable.insert("Afiq")
hashTable.insert("Sarah")
hashTable.insert("Dasha")
hashTable.insert("Alif")
# hashTable.delete("Afiq")
# hashTable.search("Afiq")
hashTable.display()
# print(hashTable.table)










