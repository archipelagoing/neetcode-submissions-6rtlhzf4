
#1. Create a graph node for every unique character in all words.
#2. For each adjacent pair (w1, w2):
#   a.If w1 starts with w2 and len(w1) > len(w2), return "".
#   b.Find the first index j where they differ and add edge w1[j] -> w2[j] (only once).
#   c.Increase indegree[w2[j]] when you add a new edge.
# 3.  Push all characters with indegree = 0 into a queue.
# 4.  While the queue is not empty:
#   a.Pop a character, add it to the answer.
#   b.For each neighbor, decrement its indegree.
#   c.If a neighbor becomes 0, push it into the queue.
# 5.  If the answer contains fewer characters than total unique characters, a cycle exists - return "".
# 6.  Otherwise, join the answer list and return it.
#---------------------------------------------
class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w} 

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j]) # word 1 is the key at index j and then we'll add that next node
                    break
        visit = {} # false = visited, true = current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # if it was already visited, we saw a character that was already in the curent path
            visit[c] = True
            # we want to see all the neighbors of c, and do dfs on that neighbor
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)