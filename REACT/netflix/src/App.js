import React, {useState, useEffect} from 'react'
import axios from 'axios';

import './styles/index.scss';

import NavBar from './components/NavBar';
import MoviesDisplay from './components/MoviesDisplay';
import Form from './components/Form'
import NewUser from './components/NewUser'

function App() {

  const [movieData, setMovieData] = useState([]);
  const [display, setDisplay] = useState('none');
  const [isLoggedIn, setLoginStatus] = useState(false)

  const getMovies = async () => {
    try {
      let response = await axios.get('http://localhost:5000/movie');
      console.log(response)
      setMovieData(response.data.data)
    } catch (error) {
      console.log(error)
      alert(error)
    }

  }

  const checkLogin = async () => {
    try {
      let result = await axios.get('http://localhost:5000/user/check')
      if (result['data']['msg'] === 'success') {
        alert('YOU ARE LOGGED IN!')
        setLoginStatus(true)
      } 
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    if (isLoggedIn) {
      getMovies()
    }
  }, [isLoggedIn])
  useEffect(() => {checkLogin()}, [])

  const handleDisplay = () => {
    if (display === 'none') setDisplay('flex')
    else setDisplay('none')
  }

  const handleMovie = (movies) => setMovieData(movies)
  
  const handleLogin = () => {
    setLoginStatus(isLoggedIn => !isLoggedIn)
  }

  return (
    <div>
        <NavBar 
          handleMovie={handleMovie}
          isLoggedIn={isLoggedIn}
          handleLogin={handleLogin}
        />

        {!isLoggedIn && (
          <NewUser />
          )
        }

        {isLoggedIn && ( 
        
        <div className='outerContainer'>
          <Form 
            display={display} 
            handleDisplay={handleDisplay} 
          />

          <MoviesDisplay 
            movieData={movieData} 
            handleDisplay={handleDisplay}  
          />
          
        </div> )}
    </div>
  );
}
export default App;

// useState is a hook that is a dyanamic variable for your component
// useEffect is a hook that deals with page loading and rendering

/*  Why do we export? a: So we can use it elsewhere in the app as component
    Why do we use state? a: A global variable that persists throughout the component
    How is state different than other variables? 
      a. You dont have to define new variables
         You need a setter function to update state whereas with variables you can directly set
    Where do you update state?
      a. Inside an event
    What module do we use to do api calls externally?
      a. axios - A library to call other apis
    What is a easy way to loop in JSX w/ ES6 sytnax?
      a. map() - Loops through item and populates an argument as each item in the list
    For an event what is the first argument that automatically gets populated?
      a. e - event details like the target.value (aka what you typed in), time, etc.
    */
