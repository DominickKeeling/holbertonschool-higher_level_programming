#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with cmopleted task
You must use the module request
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) throw error;
    else {
      const info = JSON.parse(body);
      const taskDict = {};
      for (let i = 0; i < info.length; i++) {
        const userId = info[i].userId;
        if (info[i].completed === true) {
          if (userId in taskDict) {
            taskDict[userId]++;
          } else {
            taskDict[userId] = 1;
          }
        }
      }
      console.log(taskDict);
    }
  });
