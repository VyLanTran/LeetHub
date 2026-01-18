class Solution {
public:
    string intToRoman(int num) {
        vector<pair<int, char>> val_to_sym = {
            {1000, 'M'}, 
            {500, 'D'},
            {100, 'C'},
            {50, 'L'},
            {10, 'X'},
            {5, 'V'},
            {1, 'I'}
        };
        vector<pair<int, string>> val_to_combo = {
            {900, "CM"},
            {400, "CD"},
            {90, "XC"},
            {40, "XL"},
            {9, "IX"},
            {4, "IV"}
        };
        string res = "";

        while(num > 0) {
            if (to_string(num)[0] == '4' || to_string(num)[0] == '9') {
                for (auto c : val_to_combo) {
                    auto [special_val, combo] = c;
                    if (special_val > num) {
                        continue;
                    }
                   
                    res += combo;
                    num -= special_val;
                    break;
                }
                continue;
            }
            for (auto p : val_to_sym) {
                auto [val, sym] = p;
                if (val > num) {
                    continue;
                }
                int count = num / val;
              
                res += string(count, sym);
                num -= val * count;
                break;
            }
        }
        return res;
    }
};
