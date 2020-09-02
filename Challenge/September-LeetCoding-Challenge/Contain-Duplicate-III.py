class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t) -> bool:
        if t < 0 or k < 0:
            return False
        buckets = {}
        w = t+1
        for idx, e in enumerate(nums):
            buck = e // w
            # If t = 3, then numbers 0, 1, 2, 3 will all be put into bucket[0]
            # if bucket already exist it means we have already a num which have diff <= t
            if buck in buckets:
                return True
            else:
                buckets[buck] = e
                # if t = 3, num = 4 it will be in bucket 1 and num = 2 will be in bucket 0, 4-2 <= t, so we have to consider neighbour buckets
                # see if element in left neighbour bucket have diff <= t
                if buck - 1 in buckets and e - buckets[buck-1] <= t:
                    return True
                # see if element in right neighbour bucket have diff <= t
                if buck + 1 in buckets and abs(e - buckets[buck+1]) <= t:
                    return True
                if idx >= k: #delete leftmost(idx-k) element from bucket
                    del buckets[ nums[idx - k] // w ] 
        return False




print(Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)) #true
print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3)) #false