import React, {useState} from 'react';
import axios from 'axios';

// Every time a REACT state changes it reloads
// Pure variables that describe the state of the component
function Form() {

    // State - A dynamic variable that is a property of the component. When this changes the component re-renders

    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [dob, setDob] = useState('')
    const [userName, setUserName] = useState('')
    const [password, setPass] = useState('')
    const [email, setEmail] = useState('')
    const [phone, setPhone] = useState('')

    const handleInput = (e, inputType) => {
        console.log(e.target.value)

        if (inputType === 'firstName') {
            setFirstName(e.target.value)
        } else if (inputType === 'lastName') {
            setLastName(e.target.value)
        } else if (inputType === 'dob') {
            setDob(e.target.value)
        } else if (inputType === 'userName') {
            setUserName(e.target.value)
        } else if (inputType === 'password') {
            setPass(e.target.value)
        } else if (inputType === 'email') {
            setEmail(e.target.value)
        } else if (inputType === 'phone') {
            setPhone(e.target.value)
        }
    }

    // e is a variable that represent the element and gets populated by the event handler

    /* What is the difference between asynchronous code and synchronous code?
        Synchronous - Code Blocking. One line of code executes at a time in order.
        Asynchronous - Non-Code Block. Multiple lines of code can execute independently.
        Give me an example
    */ 

    // What is a promise -> Its a promise in code that it will work one day

    const handleSubmit = async() => {

        let payload = {
            'firstName': firstName,
            'lastName': lastName,
            'dob': dob,
            'userName': userName,
            'password': password,
            'email': email,
            'phone': phone
        }

        // Validate Data

        // Save to Backend
        try {
            let endpoint = 'http://localhost:5000/saveUser'
        
            let resp =  await axios.post(endpoint, payload)
            let data = resp['data']
            
            if (data['msg'] === 'fail') {
                alert('Backend did not work')
            } else {
                console.log(data['data'])
            }

        } catch (err)  {
            console.log(err)
            alert('Frontend did not work')
        }
    }

    return (
        <div className="Form">
            <input  
                onChange={(e) => handleInput(e, 'firstName')} 
                value={firstName}
                type="text" 
                placeholder='First Name' />

            <input 
                value={lastName}
                onChange={(e) => handleInput(e, 'lastName')}   
                type="text"  
                placeholder='Last Name' />

            <input  
                value={dob}       
                onChange={(e) => handleInput(e, 'dob')}    
                type="text"  
                placeholder='Birth Date' />

            <input  value={userName}     
                    onChange={(e) => handleInput(e, 'userName')} 
                    type="text"  
                    placeholder='User Name' />

            <input  value={password}  
                    onChange={(e) => handleInput(e, 'password')}    
                    type="text"  
                    placeholder='Password' />

            <input  value={email}        
                    onChange={(e) => handleInput(e, 'email')} 
                    type="text"  
                    placeholder='Email' />

            <input  value={phone}       
                    onChange={(e) => handleInput(e, 'phone')}  
                    type="text"  
                    placeholder='Phone' />

            <br />
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}

export default Form;
