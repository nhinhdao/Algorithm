class Storage {
    constructor(){
        this.list = {};
        this.values = [];
        this.length = 0;
    }

    getValue(val){
        return this.list.get(val);
    }

    insert(val){
        if (this.list[val]) return;
        this.values.push(val);
        this.length++;
        this.list[val] = this.length - 1
    }

    remove(val){
        if (!this.list[val]) return;
        const index = this.list[val];
        temp = this.values[index];
        this.values[index] = this.values[this.length -1];
        this.values[this.length -1] = temp;
        this.values.pop();
        this.length--;
    }

    getRandom(){
        return this.values[Math.floor(Math.random() * this.length)];
    }
}

const list = new Storage();
list.insert(2)
list.insert("nhinh")
list.insert(2)
list.insert("me")

console.log(list.getRandom())