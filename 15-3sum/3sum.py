class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []

        i = 0

        while i < len(nums):

            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

            i += 1

        return ans