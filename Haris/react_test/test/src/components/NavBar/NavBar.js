import React from 'react';
import Home from '../Home/Home'

const NavBar = (props) => {
    return (
        <div>
            <div style={{'padding':'10px', 'background':'red'}}>{props.age}</div>
            <Home job="Marketer" />
        </div>
    );
}

export default NavBar;