class Solution {
    public static int removeDuplicates(int[] nums) {
//         HashSet<Integer> set = new HashSet<>();
//         for (int i = 0; i < nums.length; i++) {
//             set.add(nums[i]);
//         }

//         int k = set.size();
//         int j = 0;
//         for (int x: set) {
//             nums[j++] = x;
// //            System.out.println(x);
//         }
//         return k;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] != nums[j]){
                i++;
                nums[i] = nums[j];
                // System.out.println(nums[j]);
            }
        }
        return i+1;

    }
}