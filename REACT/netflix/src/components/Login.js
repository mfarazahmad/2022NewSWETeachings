import React, {useState} from 'react'
import axios from 'axios'

function Login(props) {

    const [userName, setUserName] = useState("")
    const [password, setPass] = useState("")

    const handleInput = (e, inputType) => {
        let value = e.target.value;
        if (inputType === "username") {
            setUserName(value)
        } else {
            setPass(value)
        }
    }
    
    const handleLogin = async () => {

        let payload = {
            'username': userName,
            'password': password
        }

        if (userName === "" || password === "") {
            alert ('Please enter in required fields!')
            return false
        }

        try {
            let endpoint = "http://localhost:5000/user/login"
            let resp = await axios.post(endpoint, payload)
            console.log(resp['data'])
            if (resp['data']['msg'] === "success") {
                props.handleLogin()
            } else {
                alert('Failed to Login!')
            }
        } catch (error) {
            console.log(error)
            alert('Failed to Login!')
        }

    } 

    return (
        <div className="loginBox">
            <input  onChange={e => handleInput(e, "username")} 
                    value={userName} 
                    placeholder="username" />
            
            <input  onChange={e => handleInput(e, "password")}
                    value={password} 
                    placeholder="password" />
            <button onClick={handleLogin}>Sign In</button>
        </div>

    )
}

export default Login