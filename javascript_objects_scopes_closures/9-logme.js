#!/usr/bin/node
/*
Write a function that prints the number of arguments already printed and the
new argument value. (see example below)
Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument
value></current>
*/

let printed = 0;

exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
}
