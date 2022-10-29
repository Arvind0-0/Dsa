class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def getLastChar(self, query):
        curr = self.root
        for ch in query:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr
    
    def getMatches(self, query):
        lastChar = self.getLastChar(query)
        res = []
        self.getWord(query, lastChar, res)
        return res
    
    def getWord(self, pref, lastChar, res):
        if not lastChar: return res.append("0")
        if lastChar.isEOW: res.append(pref)
        for nextChar, node in lastChar.children.items():
                self.getWord(pref+nextChar, node, res)
        
    def insertWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEOW = True

class Solution:
    def displayContacts(self, n, contacts, s):
        trie = Trie()
        for contact in contacts:
            trie.insertWord(contact)
        res = list()
        for i in range(1, len(s)+1):
            matches = trie.getMatches(s[:i])
            if not matches: return res + ["0"]*(len(s)-i)
            res.append(sorted(matches))
        return res
