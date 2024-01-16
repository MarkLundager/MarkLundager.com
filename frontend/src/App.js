import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage/HomePage';
import ControllerPage from './ControllerPage/ControllerPage';
import CreateAccountPage from './CreateAccountPage/CreateAccountPage';
import LoginPage from './LoginPage/LoginPage';



const App = () => {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<HomePage/>} exact />
          <Route path="/controller" element={<ControllerPage/>} exact />
          <Route path="/create_account" element={<CreateAccountPage/>} exact />
          <Route path="/login_page" element={<LoginPage/>} exact />
        </Routes>
      </Router>
    );
};

export default App;