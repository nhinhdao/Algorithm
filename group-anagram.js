
const groupAnagram = (strArray) => {
    const sortedArray = strArray.map(i => i.split("").sort().join(""));

    const groupAnagrams = {};
    for (let x = 0; x < sortedArray.length; x++){
        if (groupAnagrams[sortedArray[x]] == null){
            groupAnagrams[sortedArray[x]] =  [strArray[x]]
        }
        else {
            groupAnagrams[sortedArray[x]].push(strArray[x])
        }
    }
    
    return Object.values(groupAnagrams);
}