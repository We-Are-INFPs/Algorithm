const fs = require("fs");

const getParsedData = (i) => {
  const input = fs.readFileSync(`./in${i}.txt`, "utf8").toString();
  return input;
}

function infixToPostfix(formula) {
  let operators = [];
  let output = "";

  // 연산자의 우선순위를 확인하는 함수
  function precedence(operator) {
    if (operator === "+" || operator === "-") {
      return 1;
    } else if (operator === "*" || operator === "/") {
      return 2;
    } else {
      return 0;
    }
  }

  // 토큰을 처리하는 함수
  function processToken(token) {
    if (/[0-9]/.test(token)) {
      // 피연산자인 경우
      output += token + " ";
    } else if (token === "(") {
      // 여는 괄호인 경우
      operators.push(token);
    } else if (token === ")") {
      // 닫는 괄호인 경우
      while (operators.length > 0 && operators[operators.length - 1] !== "(") {
        output += operators.pop() + " ";
      }
      operators.pop(); // 여는 괄호 제거
    } else {
      // 연산자인 경우
      while (
        operators.length > 0 &&
        precedence(token) <= precedence(operators[operators.length - 1])
      ) {
        output += operators.pop() + " ";
      }
      operators.push(token);
    }
  }

  // 표현식을 토큰 단위로 분리
  let tokens = formula.split("");

  // 토큰을 하나씩 처리
  for (let i = 0; i < tokens.length; i++) {
    let token = tokens[i];
    processToken(token);
  }

  // 남아 있는 연산자를 모두 출력
  while (operators.length > 0) {
    output += operators.pop() + " ";
  }

  // 후위표기식 반환
  return output.trim();
}

for (let i = 1; i < 6; i += 1) {
  const formula = getParsedData(i);
  console.log(infixToPostfix(formula));
}
