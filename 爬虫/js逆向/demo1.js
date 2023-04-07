console.log("hello word");

var bb = 10;

function xxx(){
    var dd = 3;
    console.log(dd);
}

xxx()

{
    let a = 2;
}

let a,b;
let e=123,f=" ";
// let a  // 从此处可见 let 不可以被重复声明

function xx(){  // 此处定义有名函数
    let i = 9
    console.log(i)
}
// console.log(i)
const xxxs = 123
// xxxs = 456  // const 是声明常量关键字  常量不可修改

function xssss(arg1,arg2,arg3){  // 定义有名函数 并此函数需要传参arg1,arg2,arg3
    return arg1 + arg2 + arg3 // return 其实是一个终止代码
}

// 自执行函数
!(function (){
    console.log("hello world");
})()

// 内部函数操作
var _x;
!(function (){
    function xl(){
        return "xxx";
    }
    _x = xl;  // 此处给声明的全局变量复赋值
})();

console.log(_x());
_a = "{'a':'hello','b':'world'}"
JSON.parse(_a)
