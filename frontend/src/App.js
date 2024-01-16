import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import ControllerPage from './ControllerPage';
import SignUpPage from './SignUpPage';




const App = () => {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<HomePage/>} exact />
          <Route path="/controller" element={<ControllerPage/>} exact />
          <Route path="/sign_up" element={<SignUpPage/>} exact />
        </Routes>
      </Router>
    );
};

export default App;