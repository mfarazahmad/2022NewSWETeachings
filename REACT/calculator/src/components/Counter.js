import React, {useState} from 'react';

function Counter() {

    // State is a special variable that react keeps track off when changes are happening
    // State is immutable. You can't change items in state directly
    // You need a special function to change items in state

    // React Hook -> A way to inject special features into react

    const [count, setCount] = useState(0);

    function handleMinus() {
        let newCount = count - 1;
        setCount(newCount);
    }
    
    function handlePlus() {
        let newCount = count + 1;
        setCount(newCount);
    }

    return (
        <div>
            <p>Counter</p>
            <div className="counter row">
                <button onClick={handleMinus}>-</button>
                <p>{count}</p>
                <button onClick={handlePlus}>+</button>
            </div>
        </div>
    );
}

export default Counter;


/*
$('button').off().on('click', function() {
    alert('HEY!');
})
*/