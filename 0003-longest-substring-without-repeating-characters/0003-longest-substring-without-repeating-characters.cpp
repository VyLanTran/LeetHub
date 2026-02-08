class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0, left = 0;
        unordered_map<char, int> count;

        for (int right = 0; right < s.size(); right++) {
            char ch = s[right];
            count[ch]++;
            while (count[ch] > 1) {
                count[s[left]]--;
                left++;
            }
            res = max(res, right - left + 1);
        }

        return res;
    }
};