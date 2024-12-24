let [a,b] = [1,2];
while (a<20){
    [a,b] = [b,a+b]
    console.log(a,b);
    
}