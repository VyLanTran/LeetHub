class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> cache;
        for (int i = 0; i < nums.size(); i++) {
            int comp = target - nums[i];
            if (cache.contains(comp))
                return {cache[comp], i};
            cache[nums[i]] = i;
        }
        return {};
    }
};