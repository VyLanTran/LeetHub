class Solution {
public:

    string merge(string left, string right) {
        int i = 0;
        while (i < min(left.size(), right.size()) && left[i] == right[i]) {
            i += 1;
        }
        return left.substr(0, i);
    }

    string divide(int l, int r, vector<string>& strs) {
        if (l == r)
            return strs[l];
        int m = l + (r - l) / 2;
        string left_prefix = divide(l, m, strs);
        string right_prefix = divide(m + 1, r, strs);
        return merge(left_prefix, right_prefix);
    }

    string longestCommonPrefix(vector<string>& strs) {
        return divide(0, strs.size() - 1, strs);
    }
};