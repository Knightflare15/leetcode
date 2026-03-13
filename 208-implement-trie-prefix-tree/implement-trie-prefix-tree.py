class Trie:

    def __init__(self):
        self.root = {"EoW":False, "children":{}}

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i in node["children"]:
                node = node["children"][i]
            else:
                node["children"][i] = {"EoW":False,"children":{}}
                node = node["children"][i]
        node["EoW"] = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node["children"]:
                return False
            else:
                node = node["children"][i]
        if node["EoW"] == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node["children"]:
                return False
            else:
                node = node["children"][i]
        return True
        




# Your Trie object will be instantiated and called as such:
# obj = Tre()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)