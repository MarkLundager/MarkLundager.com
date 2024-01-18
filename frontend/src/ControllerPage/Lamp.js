import React from 'react';
import './Lamp.css'

const Lamp = ({color}) => {

  const handleButtonClick = () => {
    fetch(`/send_lamp_command_to_arduino/${color}`)
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
  };



  return (
  <div class="container" style={{'--color': color}}>
  <a class="button" onClick={handleButtonClick()}>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    {color}
  </a>
  </div>
  );
};

export default Lamp;