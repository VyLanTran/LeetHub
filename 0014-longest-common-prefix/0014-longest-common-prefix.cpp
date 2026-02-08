class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        return divide(strs, 0, strs.size() - 1);
    }

    string divide(vector<string>& strs, int l, int r) {
        if (l == r)
            return strs[l];
        int m = l + (r - l) / 2;
        string left_prefix = divide(strs, l, m);
        string right_prefix = divide(strs, m + 1, r);
        return merge(left_prefix, right_prefix);
    }

    string merge(string l, string r) {
        int i = 0;
        while (i < min(l.size(), r.size()) && l[i] == r[i]) {
            i++;
        }
        return l.substr(0, i);
    }
};