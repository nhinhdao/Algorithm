

const validAnagram = (firstStr, secondStr) => {
    if (firstStr.length !== secondStr.length){
        return false;
    }

    const firstStrDictionary = {};
    const secondStrDictionary = {};

    for (let x = 0; x < firstStr.length; x++){
        firstStrDictionary[firstStr[x]] = 1 + (firstStrDictionary[firstStr[x]] || 0);
        secondStrDictionary[secondStr[x]] = 1 + (secondStrDictionary[secondStr[x]] || 0);
    }

    for (let x in firstStrDictionary){
        if (firstStrDictionary[x] !== secondStrDictionary[x]){
            return false;
        }
    }
    
    return true;
}