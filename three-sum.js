
var threeSum = function (nums) {
    var sortedNums = nums.sort((a, b) => a - b);
    let i = 0;
    const answer = {};
    while (i <= sortedNums.length - 3) {
        let left = i + 1;
        let right = sortedNums.length - 1;
        while (left < right) {
            const numOne = sortedNums[i];
            const numTwo = sortedNums[left];
            const numThree = sortedNums[right];
            const currentSum = numOne + numTwo + numThree;
            if (currentSum === 0) {
                arr = [sortedNums[i], sortedNums[left], sortedNums[right]];
                if (!answer[arr.toString()]){ 
                    answer[arr.toString()] = arr;
                }
                left++;
                right--;
            }
            else if (currentSum > 0) {
                right--;
            }
            else {
                left++;
            }
        }
        i++;
    }

    return Object.values(answer);
};

// function to print triplets with 0 sum
function findTriplets(arr) {
    const uniqueNums = new Set(arr);
    const nums = Array.from(uniqueNums).sort((a, b) => a - b);
    const n = nums.length;
    const result = [];

    for (let l = 0; l < n - 1; l++) {
        // Find all pairs with sum equals to "-nums[i]"
        let s = new Set();
        for (let r = l + 1; r < n; r++) {
            const x = -(nums[l] + nums[r]);
            if (s.has(x)) {
                result.push([x, nums[l], nums[r]]);
            }
            else {
                s.add(nums[r]);
            }
        }
    }

    return result;
}

console.log(threeSum([-1,  0,  1,  2,  -1,  -4,  -2,  -3,  3,  0,  4]));
