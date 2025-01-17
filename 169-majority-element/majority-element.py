class Solution:
    def majorityElement(self, nums):
        # Dictionary to store the frequency of each number
        count = {}
        
        # Loop through each number in the list
        for num in nums:
            # Increment the count of the number in the dictionary
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Find the number with the highest frequency
        majority_element = None
        max_count = 0
        
        for num, freq in count.items():
            if freq > max_count:
                max_count = freq
                majority_element = num
        
        return majority_element
