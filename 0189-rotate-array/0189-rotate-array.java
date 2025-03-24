class Solution {
    public static void rotate(int[] nums, int k){
        // right rotate by k - optimal solution
        k = k % nums.length;
        reverse(nums,0,nums.length-1);  // reverse the whole array
        reverse(nums,0,k-1);    // reverse first k elements
        reverse(nums,k,nums.length-1);  // reverse remaining elements
    }

    public static void reverse(int[] nums, int start, int end){
        while (start<end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    // Time = O(n)
    // Space = O(1)
}