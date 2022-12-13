import React, {useState} from "react";
import axios from "axios";

function WeatherApp() {

    const [currentTemp, setTemp] = useState('')

    const handleClick = async () => {
        console.log('Test');
        let resp = await axios.get('http://api.weatherapi.com/v1/forecast.json?key=b79b5b79dda7411182c130448222706&q=dubai&days=10')
        console.log(resp.data)
        setTemp(resp['data']['current']['temp_f'])
    }
 
    return (
        <div>
            <button onClick={handleClick}>Click ME</button>
            <div>{currentTemp}</div>
        </div>
    )
}

export default WeatherApp;


// python - requests module is used to do api calls to elsewhere
// jquery - ajax is used to do api calls to backend
// react - axios is used to do api calls to backend 