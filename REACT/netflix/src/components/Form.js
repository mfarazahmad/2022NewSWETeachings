import React, {useState} from "react";
import axios from "axios";

// Properties are to a class as a state is to a Component
function Form(props) {

    const [title, setTitle] = useState('')
    const [seasons, setSeasons] = useState('')
    const [censor, setCensor] = useState('')
    const [release, setRelease] = useState('')

    const handleInput = (e, name) => {
        if (name === 'title') {
            setTitle(e.target.value)
        } else if (name === 'seasons') {
            setSeasons(e.target.value)
        } else if (name === 'censor') {
            setCensor(e.target.value)
        } else if (name === 'release') {
            setRelease(e.target.value)
        } 
    }

    const handleSubmit = () => {
        let payload = {
            'title': title,
            'seasons': seasons,
            'censor': censor,
            'release': release
        }

        let endpoint = 'http://localhost:5000/movie/new'
       
        try {
            let resp = axios.post(endpoint , payload)
            console.log(resp.data)
            props.handleDisplay()
            alert('success!')
        } catch (error) {
            console.log(error)
        }
    }

    return (
        <div className="formBack" style={{display: `${props.display}`}}>
            <div className="form">
                <div className="closeBox"> 
                    <h2>NEW MOVIE</h2>
                    <button  onClick={props.handleDisplay}>x</button>
                </div>

                <input  onChange={e => handleInput(e, 'title')} 
                        value={title} 
                        className="title" 
                        type="text" 
                        placeholder="title" />
                
                <input  onChange={e => handleInput(e, 'seasons')} 
                        value={seasons} 
                        className="seasons" 
                        type="text" 
                        placeholder="seasons" />
                
                <input  onChange={e => handleInput(e, 'censor')} 
                        value={censor} 
                        className="censor" 
                        type="text" 
                        placeholder="censor rating" />
                
                <input  onChange={e => handleInput(e, 'release')} 
                        value={release} 
                        className="release" 
                        type="text" 
                        placeholder="release date" />

                <br />

                <button onClick={handleSubmit} className="addBtn">Add</button>
            </div>
        </div>
    )
}

export default Form;