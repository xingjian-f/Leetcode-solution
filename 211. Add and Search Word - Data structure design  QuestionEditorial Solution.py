class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sons = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        a = self.sons
        for i in word:
            if i not in a:
                a[i] = {}
            a = a[i]
        a['#'] = 1


    def dfs(self, node, word):
        if node is None:
            return False
        if len(word) == 0:
            if '#' in node:
                return True
            else:
                return False
        if word[0] == '.':
            ret = False
            for i in node:
                if i == '#':
                    continue
                ret = ret or self.dfs(node[i], word[1:])
            return ret
        else:
            if word[0] in node:
                return self.dfs(node[word[0]], word[1:])
            else:
                return False


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.sons, word)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("wo")
print wordDictionary.search("...w")