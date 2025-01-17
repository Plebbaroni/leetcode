class Solution {
    public int numberOfSpecialChars(String word) {
        int[][] idx = new int[26][2];
        for (int i = 0; i < idx.length; i++) {
            for (int j = 0; j < idx[i].length; j++) {
                idx[i][j] = -1;
            }
        }
        int res = 0;

        for (int i = 0; i < word.length(); i++) {
            Character c = word.charAt(i);
            if (c > 'Z') {
                idx[c-'a'][0] = i;
            } else {
                if (idx[c-'A'][1] == -1) {
                    idx[c-'A'][1] = i;
                }
            }
        }

        for (int i = 0; i < 26; i++) {
            if (idx[i][0] != -1 && idx[i][0] < idx[i][1]) {
                res++;
            }
        }

        return res;
    }
}