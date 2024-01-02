import React from 'react';

const Banner = ({ onButtonClick }) => {
  const handleClick = () => {
    onButtonClick('firstDiv');
  };

  return (
    <section className="banner" id="banner">
      <div className="signIn" id="signIn" onClick={handleClick}>
        Sign in
      </div>
      <span id="firstName" className="firstName">
        Mark
      </span>
      <span id="lastName" className="lastName">
        Lundager
      </span>
      <ul className="menu">
        <li>About me</li>
        <li>Projects</li>
        <li id="Controller">
            Controller
        </li>
      </ul>
    </section>
  );
};

export default Banner;