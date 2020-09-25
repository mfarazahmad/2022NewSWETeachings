import React from 'react';
import Coolart from './main'
import Header from './header'
import SampleForm from './form'

// This is called a functional component. | Only returns jsx
function App() {
  return (
    <div className="App">
      <Header name="Faraz"/>
      <SampleForm />
      <Coolart />
    </div>
  );
}

export default App;
