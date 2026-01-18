class Solution {

private: 
    string s;
    int n;
    vector<int> expand(int l, int r) {
        while (l >= 0 && r < n && s[l] == s[r]) {
            l -= 1;
            r += 1;
        }
        return {l + 1, r - 1};
    }

public:
    string longestPalindrome(string s_input) {
        s = s_input;
        n = s.size();
        int min_l = 0, max_r = 0;

        for (int i = 0; i < n; i++) {
            vector<int> positions = expand(i, i);
            int l = positions[0], r = positions[1];
            if (r - l > max_r - min_l) {
                min_l = l, max_r = r;
            }
            if (i + 1 < n && s[i] == s[i + 1]) {
                vector<int> positions = expand(i, i + 1);
                int l = positions[0], r = positions[1];
                if (r - l > max_r - min_l) {
                    min_l = l, max_r = r;
                }
            }
        }

        return s.substr(min_l, max_r - min_l + 1);
    }
};