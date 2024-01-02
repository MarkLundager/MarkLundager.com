import React from 'react';
import './Banner.css';

const Banner = () => {
  return (
    <section className="banner" id="banner">
      <div class="signIn" id="signIn" onclick="handleClick('firstDiv')">
        Sign in
      </div>
      <span id="firstName" class="firstName">Mark</span>
      <span id="lastName" class="lastName">Lundager</span>
      <ul class="menu">
        <li>About me</li>
        <li>Projects</li>
        <li id="Controller"><a id="signInLink" href="#">Controller</a></li>
      </ul>
    </section>
  );
};

export default Banner;