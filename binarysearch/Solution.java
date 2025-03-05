public class Solution {

    public int[] searchRange(int[] nums, int target) {
        int[] retval = new int[2];
        retval[0] = binarySearch(nums, target, true);
        retval[1] = binarySearch(nums, target, false);
        return retval;
    }

    public int binarySearch(int[] nums, int target, boolean left) {
        int high = nums.length-1, low = 0;
        int bound = -1;
        while (low <= high) {
            int mid = (low+high)/2;
            if (nums[mid] == target) {
                bound = mid;
                if (left) {
                    high = mid-1;
                } else {
                    low = mid+1;
                }
            } else if (nums[mid] < target) {
                low = mid+1;
            } else {
                high = mid-1;
            }
        }

        return bound;
    }
} {
    
}
