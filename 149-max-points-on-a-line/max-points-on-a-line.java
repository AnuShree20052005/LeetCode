class Solution {
    public int maxPoints(int[][] points) {
        if (points.length <= 2) return points.length;
        int ans = 2;

        for (int i = 0; i < points.length; i++) {
            HashMap<String, Integer> map = new HashMap<>();

            for (int j = i + 1; j < points.length; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                int g = gcd(dx, dy);
                dx /= g;
                dy /= g;

                if (dx < 0) {
                    dx = -dx;
                    dy = -dy;
                } else if (dx == 0) {
                    dy = 1;
                } else if (dy == 0) {
                    dx = 1;
                }

                String key = dx + "," + dy;
                map.put(key, map.getOrDefault(key, 1) + 1);
                ans = Math.max(ans, map.get(key));
            }
        }
        return ans;
    }

    private int gcd(int a, int b) {
        if (b == 0) return Math.abs(a);
        return gcd(b, a % b);
    }
}