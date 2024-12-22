let objFun = function () {};
objFun.prototype = {
  name: "objFun",
  sayName: function () {
    console.log("你的名字", this.name);
    return this;
  },
  setName: function (name) {
    this.name = name;
    return this;
  },
  addFun: function (name, fun) {
    if (typeof this[name] == "function") {
      console.log(name+"该函数已经存在,请勿重复添加");
    } else {
      this[name] = fun;
      return this;
    }
  },
};

objFun.prototype.getAge = function () {
  console.log("你的年龄", this.age);
  return this;
};

let obj = new objFun();
obj.sayName().setName("张三").sayName().getAge().addFun("getAge", function () {
    console.log("你的年龄");
    
})
;
