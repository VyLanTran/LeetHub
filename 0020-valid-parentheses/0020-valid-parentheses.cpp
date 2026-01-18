class Solution {
private: 
    stack<char> st;
    unordered_map<char, char> close_to_open = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

public:
    bool isValid(string s) {
        if (s.size() % 2 == 1)
            return false;
        
        for (auto ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            }
            else if (st.size() == 0 || st.top() != close_to_open[ch]) {
                return false;
            }
            else {
                st.pop();
            }
        }

        return st.size() == 0;
    }
};