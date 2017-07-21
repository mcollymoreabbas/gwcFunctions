import random
console.log(how many numbers should the program go up to?)
user_input=input()
var x= user_input

print("here are the numbers")
for (loop=0;loop=x;loop++){
    if (loop%3 == 0 and loop%5 == 0){
        console.log("fizzbuzz")
    }
    else if (loop%5 == 0){
        console.log("buzz")
    }
    else if (loop%3 == 0){
        console.log("fizz")
    }
    else{
        console.log(loop)
    }
}
