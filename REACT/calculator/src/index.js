import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Inject React into #root div inside the public folder
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);