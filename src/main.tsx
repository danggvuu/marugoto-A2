import React from 'react';
import ReactDOM from 'react-dom/client';
import { App } from './App';
import './styles/global.css';
import './styles/tokens.stylex';

const container = document.getElementById('root');
if (!container) throw new Error('Missing #root mount node');

ReactDOM.createRoot(container).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
