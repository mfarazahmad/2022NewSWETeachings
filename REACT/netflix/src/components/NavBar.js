import React from 'react';
import icon from '../img/icon.png'
import Search from './Search'
import Login from './Login'

function NavBar(props) {
    return (
        <div className='navBar'>
            <img className="icon" src={icon} />
            <Search 
                handleMovie={props.handleMovie}
            />
            <p>TEST</p>
            {props.isLoggedIn && (
                <button onClick={props.handleLogin}>Logout</button>
            )}
            {!props.isLoggedIn && (
                <Login  
                    handleLogin={props.handleLogin}
                />
            )}

        </div>
    )
}

export default NavBar;