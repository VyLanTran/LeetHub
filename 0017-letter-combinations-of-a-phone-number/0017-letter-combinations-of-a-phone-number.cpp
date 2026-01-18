class Solution {
public:
    vector<string> result;
    vector<char> combo;
    unordered_map<char, string> digit_to_letters = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };

    void rec(int i, string digits) {
        if (i >= digits.size()) {
            vector<char> copy = combo;
            result.push_back(string(combo.begin(), combo .end()));
            return;
        }
        for (auto letter : digit_to_letters[digits[i]]) {
            combo.push_back(letter);
            rec(i + 1, digits);
            combo.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        rec(0, digits);
        return result;
    }
};
