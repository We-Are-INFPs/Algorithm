const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const N = input.shift();
  const sample = input.splice(0,Number(N));
  const getRealList = (list) => {
    return list.filter((t)=> t)
    .map((text)=>text.replace('\r', ''));
  }

  return [getRealList(sample), getRealList(input)];
}

for (let i = 1; i < 6; i += 1) {
  const [sample, poet] = getParsedData(i);
  sample.forEach(word=>{
    if (!poet.includes(word)) {
      console.log(word);
      return;
    }
  })
}