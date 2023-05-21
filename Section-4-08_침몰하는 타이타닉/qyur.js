const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N, M] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => n);
  return [N, M, parsedNumberList];
}

for (let i = 1; i < 6; i += 1) {
 const [N, M, parsedNumberList] = getParsedData(i);
 let people = parsedNumberList;
 people.sort((a,b) => a - b);

 let count = 0;
 while (people.length > 0) {
  if (people.length === 1) {
    count += 1;
    break;
  }
  if (people[0] + people[people.length - 1] > M) {
    people.splice(people.length - 1, 1);
    count += 1;
  } else {
    people.splice(0, 1);
    people.splice(people.length - 1, 1);
    count += 1;
  }
 }
 console.log(count);
}