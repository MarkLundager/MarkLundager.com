import React from 'react';
import './Spinner.css';

const Spinner = ({children}) => {
  return (
    <div className="spinner-container">
        <div className='text'>{children}</div>
      <div className="spinner"></div>
    </div>
  );
};

export default Spinner;