class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        temp = set()
        for i,j in connections:
            temp.add((i,j))
        graph = defaultdict(list)
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0 for i in range(len(connections)+1)]
        self.ans = 0
        def dfs(node):
            visited[node] = True
            for i in graph[node]:
                if visited[i] == 0:
                    if (node,i) in temp:
                        self.ans += 1
                    dfs(i)
        dfs(0)
        return self.ans
    