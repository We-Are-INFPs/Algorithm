const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString().split('\n');
  const essential = input.shift();
  const N = input.shift();
  const courseList = input
    .filter((t)=> t)
    .map((text)=>text.replace('\r', ''));
  return [essential.slice(0,-1), N, courseList];
}

for (let i = 1; i < 6; i += 1) {
  const [essential, N, courseList] = getParsedData(i);

  courseList.forEach((course,index)=>{
    const newCourse = course
      .split('')
      .filter((t)=>{
        if (essential.includes(t)) return true;
        return null
      })
      .join('');
    if (newCourse === essential) {
      console.log(`#${index+1} YES`);
    } else {
      console.log(`#${index+1} NO`);
    }
  })
}