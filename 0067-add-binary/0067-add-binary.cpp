class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        string res = "";
        int carry = 0;
        int m = a.size(), n = b.size();

        for (int i = 0; i < max(m, n); i++) {
            int digit1 = (i < m) ? a[i] - '0' : 0;
            int digit2 = (i < n) ? b[i] - '0' : 0;
            res += (digit1 + digit2 + carry) % 2 + '0';
            carry = (digit1 + digit2 + carry) / 2;
        }
        if (carry > 0) {
            res += carry + '0';
        }

        reverse(res.begin(), res.end());
        return res;
    }
};