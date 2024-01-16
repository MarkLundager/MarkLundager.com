import React, { useState, useEffect } from 'react';
import './Button.css'

const Buttons = ({ onButtonClick }) => {
  const [divColor, setDivColor] = useState('red');
  const [dataLoaded, setDataLoaded] = useState(false);

  const handleButtonClick = (action) => {
    fetch(`/run_python_code/${action}`)
    .then((response) => response.json())
    .then(setDivColor(action === 'off' ? 'red' : 'green'))
    .catch((error) => {
      console.error('Error:', error);
    });
    

  };

  useEffect(() => {
    fetch('/lamp_status')
      .then(response => response.json())
      .then(data => {
        setDivColor(data.lightOn === false ? 'red' : 'green');
        setDataLoaded(true); 
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  //  if (!dataLoaded) {
  //    return null; // or a loading spinner, message, etc.
  //  }

  return (
    <div>
      <div>
        <p>Arduino Control Buttons</p>
        <button onClick={() => handleButtonClick('off')}>Turn Off</button>
        <button onClick={() => handleButtonClick('on')}>Turn On</button>
      </div>
      <div className={`buttonIndicator ${divColor}`}></div>
    </div>
  );
};

export default Buttons;