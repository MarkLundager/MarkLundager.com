import React from 'react';
import Banner from './Banner';
import Buttons from './Buttons';
import MoneyNumber from './MoneyNumber';

const App = () => {
  const handleButtonClick = (action) => {
    fetch(`/run_python_code/${action}`)
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <Banner onButtonClick={handleButtonClick} />
      <Buttons onButtonClick={handleButtonClick} />
      <MoneyNumber></MoneyNumber>
    </div>
  );
};

export default App;