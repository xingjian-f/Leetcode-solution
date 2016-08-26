class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sons = {}
        self.vis = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        a = self.root.sons
        last = self.root
        for i in word:
            if i not in a:
                a[i] = TrieNode()
            last = a[i]
            a = a[i].sons
        last.vis = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        a = self.root.sons
        vis = self.root.vis
        for i in word:
            if i not in a:
                return False
            vis = a[i].vis
            a = a[i].sons
        return vis


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        a = self.root.sons
        for i in prefix:
            if i not in a:
                return False
            a = a[i].sons
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("ab")
print trie.search("ab")
print trie.startsWith('s')
# insert("ab"),search("a"),search("ab"),startsWith("a"),startsWith("ab")