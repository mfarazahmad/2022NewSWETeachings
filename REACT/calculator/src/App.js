import './static/css/App.css';
import Counter from './components/Counter';
import Calculator from './components/Calculator';

// Functional Component | Class Component
// Has to return JSX
// JSX - Javascript XML aka HTML with Javascript inside
function App() {

  let user = 'Faraz';
  // let is a way to define a variable to limit its scope
  // const is a way to define a variable so that the value stays constant

  return (
    <div className="App">
      <h1>Hello There <span style={{'color':'red'}}>{user}</span>!</h1>
      <Counter />
      <Calculator />
    </div>
  );
}

export default App;
