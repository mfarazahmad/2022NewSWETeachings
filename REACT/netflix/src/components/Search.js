import React, {useState} from 'react';
import axios from 'axios';

function Search(props) {

    const [searchTerm, setSearch] = useState('')

    const handleInput = async (e) => {
        let inputVal = e.target.value;
        setSearch(inputVal)

        // Make api call to backend

        try {
            let resp = await axios.get(`http://127.0.0.1:5000/search?term=${inputVal}`)
            console.log(resp)
            if (resp.data.msg === 'success') {
                let filteredMovies = resp.data.data;
                props.handleMovie(filteredMovies)
                console.log(filteredMovies)
            } else {
                alert('Error! Plesae try again!')
            }
        } catch (error) {
            console.log(error)
        }
    }

    const handleSearch = () => {
        console.log('Test');
    }

    return ( 
    <div className="searchBar">
        <input onChange={handleInput} value={searchTerm} type="text" />
        <button onClick={handleSearch}>search</button>
    </div>
    )
}

export default Search;