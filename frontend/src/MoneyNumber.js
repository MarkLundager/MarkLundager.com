import React, {useState, useEffect} from 'react';
import './MoneyNumber.css';

const MoneyNumber = () => {

    const [moneyNumber, setMoneyNumber] = useState(67);

    const fetchMoneyNumber = async () => {
      try{
        const response = await fetch(`/moneyNumber`, {method: 'GET'});
        const data = await response.json();
        setMoneyNumber(data.moneyNumber);
      } catch(error){
      console.error('Error fetching MoneyNumber', error);
      };
    } 
    useEffect(() =>{
        const intervalId = setInterval(fetchMoneyNumber, 1000);
        return () => clearInterval(intervalId);
    },[])

  return (
      <div id="MoneyNumber" class="MoneyNumber">
        <p> Number: {moneyNumber}</p>
      </div>

  );
};

export default MoneyNumber;