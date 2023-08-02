#!/usr/bin/node
// Task 7 - Write a function that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
    const matching = list.filter(value => value === searchElement);
    return matching.length;
  }
