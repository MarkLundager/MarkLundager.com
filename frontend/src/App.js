import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage/HomePage';
import ControllerPage from './ControllerPage/ControllerPage';
import CreateAccountPage from './CreateAccountPage/CreateAccountPage';
import LoginPage from './LoginPage/LoginPage';
import LogoutPage from './LogoutPage/LogoutPage';
import AboutMePage from './AboutMePage/AboutMePage';
import ProjectPage from './ProjectPage/ProjectPage'



const App = () => {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<HomePage/>} exact />
          <Route path="/controller_page" element={<ControllerPage/>} exact />
          <Route path="/create_account_page" element={<CreateAccountPage/>} exact />
          <Route path="/login_page" element={<LoginPage/>} exact />
          <Route path="/logout_page" element={<LogoutPage/>} exact />
          <Route path="/about_me_page" element={<AboutMePage/>} exact />
          <Route path="/projects_page" element={<ProjectPage/>} exact />
        </Routes>
      </Router>
    );
};

export default App;