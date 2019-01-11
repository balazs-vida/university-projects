# -*- coding: utf-8 -*-

class Solution:
    def __init__(self, candidates, target, result):
        self.candidates = candidates
        self.target = target
        self.result = result
    
    def combinationSum2(self, candidates, target, tree_traversal):
        """
        https://leetcode.com/problems/combination-sum-ii/
        
        args:
            candidates (list): a bemeneti, pozitív egészekből álló halmaz
            target (int): amivel egyenlőnek kell lennie a részhalmazelemek összegének
            tree_traversal (str): dfs, bfs, preorder
            
        returns:
            self.result (2d list): a megoldások listája
        """
        
        # heurisztika1: rendezzük sorba a halmaz elemeit
        self.candidates.sort()
        
        self.result = []
        if tree_traversal == "bfs":
            self.bfs(0, candidates, target, [])
        elif tree_traversal == "dfs":
            self.dfs(0, candidates, target, [])
        elif tree_traversal == "preorder":
            self.preorder(0, candidates, target, [])   
            
        return self.result
        
    def dfs(self, start, candidates, target, path):
        print("jelenlegi útvonal: ", path)
        
        # ha a csökkentett target 0 lesz, akkor van megoldásunk
        if target == 0:
            self.result.append(path)
        
        elif target > 0:
            for i in range(start, len(candidates)):
                # ha több azonos eleme van a halmaznak, akkor mindegyiket
                # csak egyszer vizsgáljuk
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # heurisztika2: ha az i-edik szám túl nagy lenne, akkor ugorjunk
                if candidates[i] > target:
                    break
                       
                else:
                    self.dfs(i + 1, candidates, target - candidates[i], \
                             path + [candidates[i]])
                    
    def bfs(self, start, candidates, target, path):
        queue = [(start, 0, path)] # (start, current_sum, path)
        
        while len(queue) > 0:
            print("sor tartalma: ", [queue[key][2] for key in range(len(queue))])
            print("jelenlegi útvonal: ", path)
            print('-------\n')
            
            # vegyük ki a sor első elemét
            start, current_sum, path = queue.pop(0)
            
            # ha az aktuális összeg egyenlő a targettel, akkor van megoldásunk
            if current_sum == target:
                self.result.append(path)
            
            elif current_sum < target:
                for i in range(start, len(candidates)):
                    extended_sum = current_sum + candidates[i]
                    
                    # többször számolást elkerülendő
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    
                    # heurisztika2: ha a kiterjesztett összeg túl nagy lenne,
                    #               akkor ne adjuk a sorhoz
                    elif extended_sum > target:
                        break
                    
                    else:
                        queue.append((i + 1, extended_sum, path + [candidates[i]]))
                    
    def preorder(self, start, candidates, target, path):
        print("jelenlegi útvonal: ", path)
        
        if target == 0:
            self.result.append(path.copy())
    
        elif target > 0 and start < len(candidates) and candidates[start] <= target:
            
            # bevesszük a start indexű elemet és rekurzívan meghívjuk 
            # az 1-gyel nagyobb indexre és csökkentett targetre
            path.append(candidates[start])
            self.preorder(start + 1, candidates, target - candidates[start], path)
            path.pop()
        
            # többször számolást elkerülendő
            while (start + 1 < len(candidates) and \
                   candidates[start] == candidates[start + 1]):
                start += 1
                
            # megyünk egy indexszel tovább (a poppal együtt megfelel annak, hogy
            # visszalépünk a szülőcsúcsba, azaz nem vesszük be a start indexű elemet)
            self.preorder(start + 1, candidates, target, path)

                    
if __name__ == "__main__":
    # Pelda1
    candidates, target, result = [10,1,2,7,6,1,5], 8, []
    
    # Pelda2
#    candidates, target, result = [2,5,2,1,2], 5, []
    
    # Pelda3: a 2^n felső korlát éles
    # candidates, target, result = [1,2,3,4,5], 16, []
    
    solution = Solution(candidates, target, result)    

    result = solution.combinationSum2(candidates, target, tree_traversal="bfs")     
    print("megoldás: ", result)
