class Solution(object):
    def getHint(self, secret, guess):
        a=len(secret)
        i=0
        bull=0
        cow=0
        while i<a:
            if guess[i]==secret[i]:
                bull+=1
            i+=1
        for j in set(guess):
            if j in set(secret):
                cow+=min(guess.count(j),secret.count(j))
        cow-=bull
        return str(bull)+"A"+str(cow)+"B"