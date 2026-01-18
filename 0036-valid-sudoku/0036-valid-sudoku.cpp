class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> row_set;
        unordered_map<int, unordered_set<char>> col_set;
        unordered_map<int, unordered_set<char>> box_set;
        int size = board[0].size();

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                char ch = board[i][j];
                if (ch == '.')
                    continue;
                if (row_set[i].contains(ch) || 
                    col_set[j].contains(ch) || 
                    box_set[(i / 3) * 3 + (j / 3)].contains(ch)
                )
                    return false;
                row_set[i].insert(ch);
                col_set[j].insert(ch);
                box_set[(i / 3) * 3 + (j / 3)].insert(ch);
            }
        }

        return true;
    }
};

/*
0 1 2 3 4 5 6 7 8 

(0, 1) -> 1

ri = row / 3
ci = col / 3
ri * 3 + ci

*/
