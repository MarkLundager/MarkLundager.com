import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Header.css';
const Header = () => {

  const [is_authenticated, setAuthentication] = useState(false);

  const isAuthenticated = async () => {
    try {
      const data = await fetch('/is_authenticated').then(response => response.json());
      setAuthentication(data.is_authenticated);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {
    isAuthenticated();

  }, [is_authenticated]);


  return (
    <section className="header" id="header" component={Link} to={'/'}>
      <div className="accountManagement">
        <ul>
          {!is_authenticated && (
            <>
              <li>
                <Link to="/create_account_page">Create account</Link>
              </li>
              <li>
                <Link to="/login_page">Log in</Link>
              </li>
            </>
          )}
          {is_authenticated && (
            <li>
              <Link to="/logout_page">Logout</Link>
            </li>
          )}
        </ul>
      </div>
      <span id="firstName" className="firstName">
        <Link
          to="/">Mark </Link>
      </span>
      <span id="lastName" className="lastName">
        <Link
          to="/">Lundager</Link>
      </span>
      <div className="menu">
        <ul>
        </ul>
      </div>
    </section>

  );
};

export default Header;