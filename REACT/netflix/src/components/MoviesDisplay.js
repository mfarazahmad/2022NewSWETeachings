import React from 'react';
import Movie from './Movie'

function MoviesDisplay(props) {


    return (
        <div className="movieBox">
            <div className="moviesList">
                {props.movieData.map(movie => <Movie movie={movie} /> )}
            </div>
            <button className="displayAdd" onClick={props.handleDisplay}>+</button>
        </div>
    )
}

export default MoviesDisplay;