class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Boyer-Moore voting - there can only be 1 element appearing more than
        #⌊n / 2⌋ times and therefore only 1 element that does not get canceled
        #Only the majority element survives because even after all cancellations, it still has enough     occurrences t#

        count = 0
        candidate = None

        for num in nums:

            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)
         
        return candidate    
