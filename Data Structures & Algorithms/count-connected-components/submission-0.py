class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # this guy wont do alien dictionary either
        # 2 nodes, 2 conected countComponents
        # we can try to make an adjacency list, do a dfs after
        # o(e+v) we have to go thru all edges & nodes,  
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            #while we have not found the root parent
            while res != par[res]:
                #path compression; set parent of result to grandparent --> make ll a lil shorter
                par[res] = par[par[res]]
                #update the current pointer to be the parent
                res = par[res]
            return res

    # lets do the union now
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 # no union performed
            
            if rank[p2] > rank[p1]: # union by rank
                par[p1] = p2 # add p1 as child of p1
                rank[p2] += rank[p1] # add p2 rank
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

    # lets go thru our edges now
    #? why do we need to go thru our edges?
        res = n
        for n1, n2 in edges:
            #attempt a union operation
            res -= union(n1,n2) # if it is successful, decrement the result by 1 ( return val of union) ow decremented by 0
        return res

         
        