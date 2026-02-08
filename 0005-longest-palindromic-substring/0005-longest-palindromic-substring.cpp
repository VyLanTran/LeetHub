class Solution {
public:
    string longestPalindrome(string s) {
        int opt_left = 0, opt_right = 0;
        for (int i = 0; i < s.size(); i++) {
            vector<int> pair = expand(s, i, i);
            if (pair[1] - pair[0] > opt_right - opt_left) {
                opt_left = pair[0];
                opt_right = pair[1];
            }
            if (i + 1 < s.size() && s[i + 1] == s[i]) {
                vector<int> pair = expand(s, i, i + 1);
                if (pair[1] - pair[0] > opt_right - opt_left) {
                    opt_left = pair[0];
                    opt_right = pair[1];
                }
            }
        }
        return s.substr(opt_left, opt_right - opt_left + 1);
    }

private: 
    vector<int> expand(string s, int left, int right) {
        while (left - 1 >= 0 && right + 1 < s.size() && s[left - 1] == s[right + 1]) {
            left--;
            right++;
        }
        return {left, right};
    }   
};