import React from 'react';
import { Link } from 'react-router-dom';
const Header = () => {

  return (
    <section className="header" id="header"  component={Link} to={'/'}>
       <div className="createAccount">
        <Link to="/sign_up">Create account</Link>
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