class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.con = []
        self.pos = {}
        self.size = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            if self.size == len(self.con):
                self.con.append(val)
            else:
                self.con[self.size] = val 
            self.size += 1
            # print 'be_in', self.pos
            self.pos[val] = self.size-1
            # print 'in', self.pos
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # print self.pos 
        if val in self.pos:
            rm_pos = self.pos[val]
            del self.pos[val]
            if rm_pos != self.size-1:            
                self.con[rm_pos] = self.con[self.size-1]            
                self.pos[self.con[self.size-1]] = rm_pos
            self.size -= 1
            return True 
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        # print self.size
        # print self.pos
        return random.choice(self.con[:self.size])


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# print obj.pos
# print 'in', obj.insert(0)
# print obj.pos
# print 'in', obj.insert(0)
# print obj.pos
# print 'rm', obj.remove(0)
# print obj.pos
# print 'in', obj.insert(-1)
# print obj.pos
# print 'rm', obj.remove(0)
# print obj.pos
# print obj.getRandom()