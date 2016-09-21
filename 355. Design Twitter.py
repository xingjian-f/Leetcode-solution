class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.post = defaultdict(list)
        self.user_follows = defaultdict(set)
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.post[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feed_users = set([userId])
        for i in self.user_follows[userId]:
            feed_users.add(i)
        feed_con = []
        for i in feed_users:
            feed_con.extend(self.post[i][-10:])
        feed_con = sorted(feed_con, reverse=True)
        # print feed_con
        return [i[1] for i in feed_con[:10]]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # print self.follow[followerId]
        # if followerId not in self.follow:
        #     self.follow[followerId] = set()
        self.user_follows[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # if followerId in self.follow:
        self.user_follows[followerId].discard(followeeId) 


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,2)
obj.postTweet(1,3)
print obj.getNewsFeed(1)
obj.follow(1,3)
obj.unfollow(1,3)