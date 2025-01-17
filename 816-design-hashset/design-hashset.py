class MyHashSet:
    def __init__(self):
        # Initialize the hash set with a fixed size
        self.size = 1000
        self.table = [[] for _ in range(self.size)]  # List of lists for separate chaining
    
    def _hash(self, key: int) -> int:
        # Hash function to map the key to an index in the table
        return key % self.size
    
    def add(self, key: int) -> None:
        # Find the correct bucket using the hash function
        index = self._hash(key)
        
        # Only add the key if it is not already in the bucket (avoid duplicates)
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def remove(self, key: int) -> None:
        # Find the correct bucket using the hash function
        index = self._hash(key)
        
        # Remove the key from the bucket if it exists
        if key in self.table[index]:
            self.table[index].remove(key)
    
    def contains(self, key: int) -> bool:
        # Find the correct bucket using the hash function
        index = self._hash(key)
        
        # Check if the key is in the bucket
        return key in self.table[index]

# Example usage:
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# print(obj.contains(1))  # True
# print(obj.contains(3))  # False
# obj.add(2)
# print(obj.contains(2))  # True
# obj.remove(2)
# print(obj.contains(2))  # False
