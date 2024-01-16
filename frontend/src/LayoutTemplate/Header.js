import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';
const Header = () => {

  return (
    <section className="header" id="header"  component={Link} to={'/'}>
      <div className="accountManagement">
        <ul>
          <li><Link to="/create_account">Create account</Link></li>
          <li><Link to="/login_page">Log in</Link></li>
        </ul>
      </div>
      <span id="firstName" className="firstName">
        <Link
        to="/">Mark</Link>
      </span>
      <span id="lastName" className="lastName">
      <Link
        to="/">Lundager</Link>
      </span>
      <ul className="menu">
        <li>About me</li>
        <li id="Projects">Projects</li>
        <li id="Controller">
        <Link to="/controller">Controller</Link>
            
        </li>
      </ul>
    </section>

  );
};

export default Header;