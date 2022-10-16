class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = jobDifficulty
        numDays = d
        
        @cache
        def minDifficultyHelper(currentJobDif, currentDay, jobIndex):
            jobsLeft = len(jobDifficulty) - jobIndex
            daysLeft = numDays - currentDay
            if(jobsLeft < daysLeft or currentDay > numDays):
                return float('inf')
            
            if(jobIndex == len(jobDifficulty)):
                if(currentDay == numDays):
                    return currentJobDif
                return float('inf')
            
            nextJobDif = jobs[jobIndex]
            ###do job today
            minCostToday = minDifficultyHelper(max(currentJobDif,nextJobDif), currentDay, jobIndex+1)
            ###do job tomorrow            
            minCostTomorrow = currentJobDif + minDifficultyHelper(nextJobDif, currentDay+1, jobIndex+1)
            
            return min(minCostToday, minCostTomorrow)
        
        
        currentDayDif = jobDifficulty[0]
        currentDay = 1
        jobIndex = 1
        
        minDifficulty = minDifficultyHelper(currentDayDif, currentDay, jobIndex)
        
        return -1 if minDifficulty == float('inf') else minDifficulty