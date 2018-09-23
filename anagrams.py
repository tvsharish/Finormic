class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        result = []
        
        from collections import Counter
        visited = [False for _ in range(len(A))]
        counter = [Counter(A[i]) for i in range(len(A))]
        
        i = 0
        while i < len(A):
            if not visited[i]:
                tmp = []
                tmp.append(i+1)
                visited[i] = True
                for j in range(len(A)):
                    if not visited[j] and counter[i] == counter[j]:
                        tmp.append(j+1)
                        visited[j] = True
                result.append(tmp)
            i += 1
        return result
 

