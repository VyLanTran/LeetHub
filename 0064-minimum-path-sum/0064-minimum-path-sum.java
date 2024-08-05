class Solution {
    // Better memory
    public int minPathSum(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        // first row
        for (int i = 1; i < cols; i++) {
            grid[0][i] += grid[0][i-1];
        }
        // first col
        for (int i = 1; i < rows; i++) {
            grid[i][0] += grid[i - 1][0];
        }
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[grid.length - 1][grid[0].length - 1];
    }


    // Worse memory
    // public int minPathSum(int[][] grid) {
    //     int rows = grid.length;
    //     int cols = grid[0].length;
        
    //     // keep track of current col to cal next col (but modify in place)
    //     int[] cur = new int[rows];
    //     cur[0] = grid[0][0];
    //     for (int i = 1; i < rows; i++) {
    //         cur[i] = cur[i-1] + grid[i][0];
    //     }

    //     for (int i = 1; i < cols; i++) {
    //         cur[0] += grid[0][i];
    //         for (int j = 1; j < rows; j++) {
    //             cur[j] = Math.min(cur[j], cur[j-1]) + grid[j][i];
    //         }
    //     }

    //     return cur[rows - 1];
    // }
}