// Object.prototype.getName = function () {
//   return this.name;
// } // 这样做污染了原生对象，不推荐

// let obj = {
//     name: '张三',
//     age:15
// }

// console.log(obj.getName()); // 张三,看似没毛病

// for(a in obj){
//     console.log(a); // name, age, getName  原生对象被污染了就会得到getName这个不应该出现的方法
// }

// Object.keys(obj); // ["name", "age"]

const funObj = function () { };
funObj.name = '李四';
const abc = new funObj();
console.log(abc.name); // 李四
console.log(abc.prototype); // undefined
