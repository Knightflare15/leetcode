class WordDictionary:

    def __init__(self):
        self.root = {"EoW" : False, "children":{}}

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node["children"]:
                node["children"][i] = {"EoW":False,"children":{}}
                node = node["children"][i]
            else:
                node = node["children"][i]
        node["EoW"] = True

    def search(self, word: str) -> bool:
        node = self.root
        end = len(word)
        def dfs(node,i):
            if i == end:
                return node["EoW"]
            if word[i] == ".":
                for j in node["children"]:
                    flag = dfs(node["children"][j],i+1)
                    if flag:
                        return True
                return False
            else:
                if word[i] not in node["children"]:
                    return False
                return True and dfs(node["children"][word[i]],i+1)
        return dfs(node,0)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)