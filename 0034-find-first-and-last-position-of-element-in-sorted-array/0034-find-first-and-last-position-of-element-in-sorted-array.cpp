class Solution {
private: 
    int find_index(vector<int>& nums, int target, bool is_first, int left, int right) {
        int res = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                res = mid;
                if (is_first) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return res;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = find_index(nums, target, true, 0, nums.size() - 1);
        if (start == -1) 
            return {-1, -1};
        int end = find_index(nums, target, false, start, nums.size() - 1);
        return {start, end};      
    }
};