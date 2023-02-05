const fs = require("fs");

for (let i = 1; i < 6; i += 1) {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString();

  const regex = /[^0-9]/g;
  const result = input.replace(regex, "");
  const number = parseInt(result);
  console.log(number);

  let yaksuCount = 0;
  for (let i = 1; i < number + 1; i += 1) {
    if (number % i === 0) yaksuCount += 1;
  }
  console.log(yaksuCount);
}