import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();

        int i;
        int current;
        int required;

        for (i = 0; i < nums.length; i++) {

            current = nums[i];
            required = target - current;

            if (map.containsKey(required)) {
                return new int[] { map.get(required), i };
            }

            map.put(current, i);
        }

        return new int[] {};
    }
}