const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString();
  return input;
}

function evaluatePostfix(tokens) {
  let stack = [];

  // 토큰을 처리하는 함수
  function processToken(token) {
    if (/[0-9]/.test(token)) {
      // 피연산자인 경우
      stack.push(parseInt(token));
    } else {
      // 연산자인 경우
      let operand2 = stack.pop();
      let operand1 = stack.pop();

      switch (token) {
        case "+":
          stack.push(operand1 + operand2);
          break;
        case "-":
          stack.push(operand1 - operand2);
          break;
        case "*":
          stack.push(operand1 * operand2);
          break;
        case "/":
          stack.push(operand1 / operand2);
          break;
      }
    }
  }

  tokens.forEach((token)=>processToken(token));

  return stack[0];
}

for (let i = 1; i < 6; i += 1) {
  const formula = getParsedData(i);
  const tokens = formula.split("");
  console.log(evaluatePostfix(tokens));
}
