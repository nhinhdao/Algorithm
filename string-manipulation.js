const words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];

const group_anagram = words => {
    const map = new Map();

    for (const word of words) {
        const initial = new Array(26).fill(0);

        for (const i in word) {
            // get the unicode value of the character in word, set at index - 97 in initial array
            // a = 97 so a is at index 0, b = 98 - 97 at index 1
            initial[word.charCodeAt(i) - 97]++;
        }

        const key = initial.join('-');
        if (!map.has(key)) {
            map.set(key, []);
        }
        map.get(key).push(word);
    }
    console.log(map);

    return Array.from(map.values());
};

const isAnagram = (word1, word2) => {
    if (word1.length !== word2.length) return false;

    const obj = {};

    for (const char of word1) {
        obj[char] = (obj[char] || 0) + 1;
    }
    console.log(obj);

    for (const char of word2) {
        if (obj[char]) {
            obj[char] -= 1;
        } else {
            return false;
        }
    }
    console.log(obj);

    return true;
};

function get_pal_list(collection) {
    const obj = {};
    let orderedWord;

    for (const word of collection) {
        const sorted = word.split('').sort().join('');

        if (obj[sorted]) {
            obj[sorted].push(word);
        } else {
            obj[sorted] = [word];
        }
    }
    return Object.values(obj);
}

const str = "string manip interview question";

function reverse_str(str) {
    const arr = str.split(" ");
    const words = arr.reduceRight((acc, value) => {
        return `${acc} ${value}`;
    }, "");

    return words.trim();
}

function reverse_str2(str) {
    const arr = str.split(" ");
    const words = arr.reduceRight((acc, value) => {
        acc.push(value);
        return acc
    }, []);

    return words.join(" ");
}

// Log to console
console.log(group_anagram(words));
