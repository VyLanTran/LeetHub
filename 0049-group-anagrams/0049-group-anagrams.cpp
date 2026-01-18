class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> res;

        for (auto str: strs) {
            string key = hash_str(str);
            map[key].push_back(str);
        }
        for (auto p: map) {
            res.push_back(p.second);
        }
        return res;  
    };

private:
    string hash_str(string str) {
        array<int, 26> count = {};
        string res = "";

        for (auto letter : str) {
            count[letter - 'a'] += 1;
        }
        for (int i = 0; i < count.size(); i++) {
            res += "#" + to_string(count[i]);
        }
        return res;
    }
};

/*
(0, 0, ..., 0): 26 entries
*/