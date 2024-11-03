class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int c = moveTime.length;
        int d = moveTime[0].length;
        
        int[][] dist = new int[c][d];
        for (int i = 0; i < c; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        
        PriorityQueue<int[]> ab = new PriorityQueue<>((p, q) -> p[0] - q[0]);
        
        ab.offer(new int[]{0, 0, 0});
        dist[0][0] = 0;
        
        int[][] dirs = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        
        while (!ab.isEmpty()) {
            int[] curr = ab.poll();
            int time = curr[0];
            int row = curr[1];
            int col = curr[2];

            if (time > dist[row][col]) continue;
            
            for (int[] dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                
                if (newRow >= 0 && newRow < c && newCol >= 0 && newCol < d) {
                    int newTime = Math.max(time, moveTime[newRow][newCol]) + 1;
                    
                    if (newTime < dist[newRow][newCol]) {
                        dist[newRow][newCol] = newTime;
                        ab.offer(new int[]{newTime, newRow, newCol});
                    }
                }
            }
        }
        
        return dist[c-1][d-1];
    }
}