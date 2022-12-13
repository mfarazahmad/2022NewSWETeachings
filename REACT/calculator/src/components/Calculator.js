import React, {useState}  from "react";

function Calculator() {

    const [num1, setNum1] = useState(0);
    const [num2, setNum2] = useState(0);
    const [operation, setOperation] = useState('+');
    const [sum, setSum] = useState(0);

    const handleNumbers = (calcButton) => {
        // How do I know what variable to assign: Is it num1 or num2?
        if (num1 === 0) {
            // setNum1
            setNum1(calcButton)
        } else if (num1 !== 0) {
            // setNum2
            setNum2(calcButton)
        }
    }

    const handleOperation = (modifyButton) => {
        setOperation(modifyButton)
    }

    
    const handleTotal = () => {
        let total = 0;

        if (operation === '+') {
            total = add(num1, num2)
        } else if (operation === '-') {
            total = subtract(num1, num2)
        } else if (operation === '*') {
            total = multiply(num1, num2)
        } else if (operation === '/') {
            total = divide(num1, num2)
        }

        setSum(total)
    }


    const add = (x, y) => {
        let total = x + y
        return total
    }

    const subtract = (x, y) => {
        let total = x - y
        return total  
    }

    const multiply = (x, y) => {
        let total = x * y
        return total
    }

    const divide = (x, y) => {
        let total = x / y
        return total
    }
    // ES6 Syntax for a function
    //() => 

    return (
    <div className="calculator">

        <p>Calculator</p>

        <div className="display">
            <div>{num1}</div>
            <div>{operation}</div>
            <div>{num2}</div>
            <div>={sum}</div>
        </div>

        <div className="modify">
            <button onClick={() => handleOperation('+')}>+</button>
            <button onClick={() => handleOperation('-')}>-</button>
            <button onClick={() => handleOperation('*')}>*</button>
            <button onClick={() => handleOperation('/')}>/</button>
        </div>

        <div className="numbers">
            <div className="row">
                <button onClick={() => {handleNumbers(1)} }>1</button>
                <button onClick={() => {handleNumbers(2)} }>2</button>
                <button onClick={() => {handleNumbers(3)} }>3</button>
            </div>
            <div className="row">
                <button onClick={() => {handleNumbers(4)} }>4</button>
                <button onClick={() => {handleNumbers(5)} }>5</button>
                <button onClick={() => {handleNumbers(6)} }>6</button>
            </div>
            <div className="row">
                <button onClick={() => {handleNumbers(7)} }>7</button>
                <button onClick={() => {handleNumbers(8)} }>8</button>
                <button onClick={() => {handleNumbers(9)} }>9</button>
            </div>
        </div>

        <button className="totalBtn" onClick={handleTotal}>=</button>

    </div>
    );
}


export default Calculator;