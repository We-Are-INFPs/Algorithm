const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const parsedIndexList = input.map((firstAndEnd) => {
    const [f, e] = firstAndEnd.split(' ');
    return [Number(f), Number(e)];
  })
  return parsedIndexList;
}

for (let i = 1; i < 6; i += 1) {
  const parsedIndexList = getParsedData(i);

  const cardList = [...new Array(20)].map((_, i) => i + 1);

  parsedIndexList.forEach(([f,e])=>{
    const targetPart = cardList.slice(f-1,e);
    cardList.splice(f-1,e-f+1,...targetPart.reverse());
  })

  console.log(cardList.join(' '));
}