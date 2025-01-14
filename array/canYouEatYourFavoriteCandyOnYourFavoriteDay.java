//crashed out and copied this solution, less performant sol below.
class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        int n = queries.length, c = candiesCount.length;
        long[] prefix = new long[c+1];
        boolean[] answer = new boolean[n];
        prefix[0] = 0;

        for (int i = 1; i < c+1; i++) {
            prefix[i] = prefix[i-1] + candiesCount[i-1];
        }

        for (int i = 0; i < n; i++) {
            int type = queries[i][0], day = queries[i][1], cap = queries[i][2];
            long maxDay = prefix[type+1]-1;
            long minDay = prefix[type]/cap;
            answer[i] = (minDay <= day && day <= maxDay);
        }
        return answer;
    }
}

//actual sol I wrote here god of tle

class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        int n = queries.length;
        boolean[] answer = new boolean[n];
        for (int i = 0; i < n; i++) {
            int prefix = 0, latestcand = 0;
            int candies = queries[i][0], day = queries[i][1], cap = queries[i][2];
            for (int j = 0; j <= candies; j++) {
                prefix += candiesCount[j];
                latestcand = candiesCount[j];
            }
            int latestday = prefix-1;
            prefix -= latestcand;
            if (latestday < day) {
                continue;
            }
            if (prefix/cap <= day) {
                answer[i] = true;
            }
        }
        return answer;
    }
}