import React, { useState, useEffect } from 'react';
import './Button.css'

const Buttons = ({ onButtonClick }) => {
  const [divColor, setDivColor] = useState('red');
  const [dataLoaded, setDataLoaded] = useState(false);

  const handleButtonClick = (action) => {
    setDivColor(action === 'off' ? 'red' : 'green');
    onButtonClick(action);
  };

  useEffect(() => {
    fetch('/lamp_status')
      .then(response => response.json())
      .then(data => {
        console.log('Data type of lamp_on:', typeof data.lightOn);
        console.log('Actual value of lamp_on:', data.lightOn);
        console.log(data.lightOn === false ? 'red' : 'green')
        setDivColor(data.lightOn === false ? 'red' : 'green');
        setDataLoaded(true);  // Mark that the data has been loaded
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // Render nothing until the data is loaded
  if (!dataLoaded) {
    return null; // or a loading spinner, message, etc.
  }

  return (
    <div>
      <div>
        <p>Click the buttons below:</p>
        <button onClick={() => handleButtonClick('off')}>Turn Off</button>
        <button onClick={() => handleButtonClick('on')}>Turn On</button>
      </div>
      <div className={`buttonIndicator ${divColor}`}></div>
    </div>
  );
};

export default Buttons;