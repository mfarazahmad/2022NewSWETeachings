import React, { useRef } from 'react'
import users from '../models/user'
import creditcard from '../models/creditcard'
import address from '../models/address'

// .map(function) - Loops through and performs an operation of list of items
// .filter(function) - Loop through and makes the list smaller
// .reduce(function) - Loop through and only give you one value

function DisplayUsers() {

    return (
        <div className='Display'>
            {users['data'].map(function(user)  {
                return (
                    <div>
                        <br />
                        <li>{user["firstName"]}</li>
                        <li>{user["lastName"]}</li>
                        <li>{user["dob"]}</li>
                        <li>{user["gender"]}</li>
                    </div>
                )
            })}

            {creditcard['data'].map((cardInfo) => {
                return <li>{cardInfo.expDate}</li>
            })}
        </div>
    );
}

export default DisplayUsers;