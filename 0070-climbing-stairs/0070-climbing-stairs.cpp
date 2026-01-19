class Solution {
public:
    unordered_map<int, int> dp;
    int climbStairs(int n) {
        if (n == 0 || n == 1)
            return 1;
        if (dp.contains(n))
            return dp[n];
        int res = climbStairs(n - 2) + climbStairs(n - 1);
        dp[n] = res;
        return res;
    }
};

/*
f(n):
    if n == 1:
        return 1
    if in cache:
        return that
    // take 1 step
    f(n - 1)
    // take 2 steps
    f(n - 2)
    res = sum of 2 results above
    put to cache
    return res
*/