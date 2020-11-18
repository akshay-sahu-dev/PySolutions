## https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(1,len(cost)-1):
            
            cost[i+1]=cost[i+1]+min(cost[i],cost[i-1])
            
        return min(cost[-1],cost[-2])
            
                    
                    
                    
            