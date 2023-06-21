const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const [N, M] = input[0].split(' ').map((number)=> Number(number));
  const parsedNumberList = input[1].split(' ').map((number)=> Number(number)).filter(n => !isNaN(n))
  return [N, M, parsedNumberList];
}

for (let i = 1; i < 6; i += 1) {
  let [N, M, parsedNumberList] = getParsedData(i);
  const queue = Array(N).fill().map((_,i)=>i);
  let count = 0;

  while (queue.length) {
    const firstIndex = queue.shift();
    const firstNumber = parsedNumberList.shift();
    if (firstNumber < Math.max(...parsedNumberList)) {
      queue.push(firstIndex);
      parsedNumberList.push(firstNumber);
    } else {
      count += 1;
      if (firstIndex === M) {
        console.log(count);
        break;
      }
    }
  }
}
