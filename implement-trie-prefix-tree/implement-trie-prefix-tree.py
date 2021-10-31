class Trie:

    def __init__(self):
       
        self.dict = {}
        self.end = '/'

    def insert(self, word: str) -> None:
        
        temp = self.dict
        for i in word:
            if i in temp:
                temp = temp[i]
            else:
                temp[i] = {}
                temp = temp[i]
        temp[self.end] = self.end
        
    def search(self, word: str) -> bool:
        
        temp = self.dict
        for i in word:
            if i in temp:
                temp = temp[i]
            else:
                return False

        return self.end in temp
        
    def startsWith(self, prefix: str) -> bool:
        
        temp = self.dict
        for i in prefix:
            if i in temp:
                temp = temp[i]
            else:
                return False

        return True
        