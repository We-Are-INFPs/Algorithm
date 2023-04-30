const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');

  const parsedList = input.map((arr, index) => {
    if (index !== 1 && index !== 3) return null;

    return arr.split(' ').map((number)=> Number(number)).filter(n => n);
  }).filter(l=>l)

  return parsedList;
}

for (let i = 1; i < 6; i += 1) {
  const [firstList, secondList] = getParsedData(i);
  console.log(`#${i}`, [...firstList,...secondList].sort((a,b) =>  a - b).join(' '));
}