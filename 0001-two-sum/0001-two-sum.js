/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // optimal solution using Map()
    const map = new Map()
    for(let i=0; i<nums.length; i++){
        let diff = target - nums[i]
        if(map.has(diff)){
            return [map.get(diff), i]
        }
        map.set(nums[i], i)
    }
    return []

    // Time: O(n)
    // Space: O(1)  

    // using objects in this solution (better solution)

    // const map = {}

    // for(let i=0; i<nums.length; i++){
    //     let diff = target - nums[i]
    //     if(diff in map){
    //         return [map[diff], i]
    //     }
    //     map[nums[i]] = i
    // }
    // return []

    // Time: O(n)
    // Space: O(1)

    // brute force solution using two loops

    // for(let i=0; i<nums.length; i++){
    //     for(let j=i+1; j<nums.length; j++){
    //         let sum = nums[i] + nums[j]
    //         if(sum === target){
    //             return [i, j]
    //         }
    //     }
    // }
    // return []

    // Time: O(n^2)
    // Space: O(1)
};