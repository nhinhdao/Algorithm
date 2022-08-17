

//[10, 20, 35, 50, 75, 80] sum = 70
var pairSum = function(nums, sum) {
    let startIndex = 0;
    let endIndex = nums.length - 1;

    while (startIndex < endIndex){
        const numOne = nums[startIndex];
        const numTwo = nums[endIndex]
        const currentSum = numOne + numTwo;
        if(currentSum === sum){
            return true;
        }
        else if (currentSum > sum){
            endIndex--;
        }
        else {
            startIndex++;
        }
    }

    return false;
};


const result = pairSum([10, 20, 35, 50, 75, 80], 70);

console.log(result);