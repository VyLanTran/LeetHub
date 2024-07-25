class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> dueTime = new PriorityQueue<>();
        int rooms = 0;
        for (int i = 0; i < intervals.length; i++) {
            if (dueTime.size() == 0 || dueTime.peek() > intervals[i][0]) {
                rooms++;
            }
            else {
                dueTime.poll();
            }
            dueTime.add(intervals[i][1]);
        }

        return rooms;
    }
}