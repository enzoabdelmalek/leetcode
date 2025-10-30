class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        for i in range(len(nums)) :
            if i == 0 :
                answer[0] = nums[0]
            else : 
                answer[i] = nums[i] + answer[i-1]
        return answer