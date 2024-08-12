class Solution {
    public List<List<String>> res = new ArrayList<>();
    public int size;
    public HashSet<Integer> cols = new HashSet<>();
    public HashSet<Integer> diagonals  = new HashSet<>();
    public HashSet<Integer> antidiagonals = new HashSet<>();
    public List<String> board = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        size = n;
        String emptyRow = "";
        for (int i = 0; i < n; i++) {
            emptyRow += ".";
        }
        for (int i = 0; i < n; i++) {
            board.add(emptyRow);
        }
        
        rec(0);
        return res;
    }

    public void rec(int row) {
        if (row >= size) {
            res.add(new ArrayList<>(new ArrayList<>(board)));
            return;
        }

        for (int col  = 0; col < size; col++) {
            if (!(cols.contains(col) || diagonals.contains(row + col) || antidiagonals.contains(row - col))) {
                cols.add(col);
                diagonals.add(row + col);
                antidiagonals.add(row - col);
                String curRow = board.get(row);
                String newRow= curRow.substring(0, col) + "Q" + curRow.substring(col + 1, size);
                board.set(row, newRow);
                rec(row + 1);
                board.set(row, curRow);
                cols.remove(col);
                diagonals.remove(row + col);
                antidiagonals.remove(row - col);
            }
        }
    }
}