let numOne = ''; 
let operator = '+'; 
let numTwo = '';


const onClickOperator = (op) => () => { 
    if (numOne) {
      operator = op;
      $operator.value = op;
      console.log('operator:', operator);
    } else {
      alert('숫자를 먼저 입력하세요.');
    }
  };