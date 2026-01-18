class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        combo = nums;
        backtrack(0);
        return result;
    }

private:
    vector<vector<int>> result;
    vector<int> combo;

    void swap(int i, int j) {
        int temp = combo[i];
        combo[i] = combo[j];
        combo[j] = temp;
    }
    
    void backtrack(int start) {
        if (start >= combo.size()) {
            vector<int> copy = combo;
            result.push_back(copy);
            return;
        }

        for (int i = start; i < combo.size(); i++) {
            swap(start, i);
            backtrack(start + 1);
            swap(start, i);
        }
    }
};

/*
0, 1, 2
1, 2, 3

f(start = 0)
    i = 0: 
        swap (0, 0) -> [1, 2, 3]
        f(start = 1)
            i = 1: 
                swap (1, 1) -> [1, 2, 3]
                f(start = 2)
                    i = 2: 
                        swap (2, 2) -> [1, 2, 3]
                        f(start = 3) -> **[1, 2, 3]
                        back (2, 2) -> [1, 2, 3]
                back (1, 1)
            i = 2:
                swap (1, 2) -> [1, 3, 2]
                f(start = 3) -> **[1, 3, 3]
                back (2, 1) -> [1, 2, 3]
        back (0, 0)
    i = 1:
        swap (0, 1) -> [2, 1, 3]
        f(start + 1 = 1)
            i = 1:
                swap (1, 1) -> [2, 1, 3]
                f(start = 2)
                    swap (2, 2) -> [2, 1, 3]
                    f(start = 3) -> **[2, 1, 3]
                    back (2, 2)
                back (1, 1)
            i = 2:
                swap (1, 2) -> [2, 3, 1]

*/