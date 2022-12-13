import React, {useState} from 'react';
import backupImg from '../img/goku.png';

function Movie(props) {

    const [display, setDisplay] = useState(false)

    const handleHover = () => { 
        setDisplay((display) => !display)
    }

    if (props.movie['img'] != '') {
        backupImg = props.movie['img']
    }

    return (
        <div className='movie' onMouseEnter={handleHover} onMouseLeave={handleHover} >
            <div className="movieShow" style={{backgroundImage: `url(${backupImg})`}}>
                <p className='title'>{props.movie['title']}</p>
                <div className='row'>
                    <p>Release: {props.movie['Year']}</p>
                    <p>Rating: {props.movie['UserRating']}</p>
                </div>
                <p className='feelings'>{props.movie['feelings']}</p>
            </div>
            
            {display && 
                <div className='movieExtention' >
                    <p className="genre">{props.movie['genre']}</p>
                    <p className='rating'>{props.movie['censoryRating']}</p>
                    <p>Seasons: {props.movie['seasons']}</p>
                </div>
            }
        </div>
    )
}

export default Movie;