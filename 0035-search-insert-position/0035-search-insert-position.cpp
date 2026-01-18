class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) 
                return mid;
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return left;
    }   
};

/*
0,1,2,3
1,3,5,6
l.m   r
lr
r l
return l

1,3,5,6
l m.  r
    lmr
      lmr
      r l
*/