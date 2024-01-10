import React from 'react';
import Banner from './Banner';
import Buttons from './Buttons';
import TimeUntilCanada from './TimeUntilCanada';

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
      <TimeUntilCanada></TimeUntilCanada>
    </div>
  );
};

export default App;