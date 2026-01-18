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
                cout << "special case, num = " << num << endl;
                for (auto c : val_to_combo) {
                    auto [special_val, combo] = c;
                    if (special_val > num) {
                        continue;
                    }
                    cout << "special val = " << special_val << " combo = " << combo << endl;
                    cout << "num= " << num << " , subtract by = " << special_val << ", end=" << num - special_val << endl;
                    res += combo;
                    num -= special_val;
                    cout << "check that new num =" << num << endl;
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
                // if (count != 4 && count != 9) {
                //     res += string(count, sym);
                //     num -= val * count;
                // }
                res += string(count, sym);
                num -= val * count;
                break;
            }
        }
        return res;
    }
};

/*

while num > 0:
    compared with (big to small) values: 1000, 500, etc
    stop at the first val < num 
    count = num / val
    if count is not 4 or 9:
        append symbol * count to result
        num -= val * count
    else:
        go from 900, 400, etc
        stop at the first special_val < num
        append that special combo to result 
        num -= special_val

    


ex: 
num = 3749
val = 1000 --> M
count = 3

num = 49
i = 4, val = 10
count = 4
nex_val = 50
diff = 10 = 50 - 10 * 4

num = 9
val = 5
count = 9 / 5 = 1
next_val (of 5) = 10
diff = 
*/