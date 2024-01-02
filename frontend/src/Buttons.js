// Buttons.js
import React from 'react';

const Buttons = ({ onButtonClick }) => {
  const handleButtonClick = (action) => {
    onButtonClick(action);
  };

  return (
    <div>
      <p>Click the buttons below:</p>
      <button onClick={() => handleButtonClick('off')}>Turn Off</button>
      <button onClick={() => handleButtonClick('on')}>Turn On</button>
    </div>
  );
};

export default Buttons;