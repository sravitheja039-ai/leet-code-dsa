class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}

        for i in range(len(nums)):
            if nums[i] in h:
                p = i - h[nums[i]]

                if p <= k:
                    return True

            h[nums[i]] = i

        return False

        