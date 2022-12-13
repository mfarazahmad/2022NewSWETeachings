import React, {useState} from 'react'
import axios from 'axios'


function NewUser() {
    const [name, setName] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPass] = useState('')

    // When you change state the page reloads with the new change

    const handleName = (event) => {
        let value = event.target.value;
        setName(value)
    }

    const handleUserName = (event) => {
        let value = event.target.value;
        setUsername(value)
    }

    const handlePass = (event) => {
        let value = event.target.value;
        setPass(value)
    }

    const handleSave = async () => {
        let payload = {
            'name': name,
            'username': username,
            'password': password
        }

        if (name === "" || username === "" || password === "") {
            alert('Please enter in required fields!')
            return false;
        } 

        try {
            let endpoint = 'http://localhost:5000/user/new'
            let resp = await axios.post(endpoint, payload)
            if (resp['data']['msg'] === "success") {
                alert('YOU WERE SUCCESSFUL!')
            } else {
                alert('Failed to save to DB!')
            }
        } catch (error) {
            console.log(error);
            alert('Failed to save to DB!')
        }
    }

    return (
        <div className="newUserBox">
            <h2>Create New Account </h2>
            <input  
                    onChange={handleName}
                    value={name} 
                    placeholder="name" 
            />
            <input 
                    onChange={handleUserName}
                    value={username} 
                    placeholder="username"  
            />
            <input 
                    onChange={handlePass}
                    value ={password} 
                    placeholder="password" 
            />
            
            <button onClick={handleSave}>Save</button>
        </div>
    )
}

export default NewUser;