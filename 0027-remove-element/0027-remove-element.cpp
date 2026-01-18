class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int left = 0, right = n - 1;

        while (left <= right) {
            while (left < n && nums[left] != val) {
                left += 1;
            }
            while (right >= 0 && nums[right] == val) {
                right -= 1;
            }
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        return left;
    }
};
