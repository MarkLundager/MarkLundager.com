import React, {useState, useEffect} from 'react';

const MoneyNumber = () => {

    const [moneyNumber, setMoneyNumber] = useState(67);
    const updateNumber = () => {
        setMoneyNumber((prevMoneynumber) => prevMoneynumber + 67);
    };


    useEffect(() =>{
        const now = new Date();
        const timeUntilNext1AM = new Date(
            now.getFullYear(),
            now.getMonth(),
            now.getDate() + 1,
            1,
            0,
            0,
            0
          ) - now;


        const intervalId = setInterval(updateNumber, timeUntilNext1AM);
        return () => clearInterval(intervalId);
    },[])

  return (
      <div id="MoneyNumber">
        <p> Money Number: {moneyNumber}</p>
      </div>

  );
};

export default MoneyNumber;