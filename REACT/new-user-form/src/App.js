import './styles/App.css';
import Form from './components/Form'
import DisplayUsers from './components/DisplayUsers'
import WeatherApp from './components/Weather';

function App() {
  return (
    <div className="App">
      <WeatherApp />
      <Form />
      <DisplayUsers />
    </div>
  );
}

export default App;
