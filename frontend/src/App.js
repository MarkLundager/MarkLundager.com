import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ControllerPage from './ControllerPage/ControllerPage';
import CreateAccountPage from './CreateAccountPage/CreateAccountPage';
import LoginPage from './LoginPage/LoginPage';
import LogoutPage from './LogoutPage/LogoutPage';



const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ControllerPage />} exact />
        <Route path="/create_account_page" element={<CreateAccountPage />} exact />
        <Route path="/login_page" element={<LoginPage />} exact />
        <Route path="/logout_page" element={<LogoutPage />} exact />
      </Routes>
    </Router>
  );
};

export default App;