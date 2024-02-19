import React, {useState, useEffect} from 'react';
import './HomePage.css'
import Spinner from '../GeneralComponents/Spinner'

const TimeUnilCanada = () => {

  const [timeLeft, setTimeLeft] = useState({
    days: null,
    hours: null,
    minutes: null,
    seconds: null,
    totalSeconds: null
  });

  const [dataLoaded, setDataLoaded] = useState(false);

    const fetchTimeRemaining = async () => {
      try {
        const response = await fetch('/timeUntilCanada', { method: 'GET' });
        const data = await response.json();
        setTimeLeft(data);
        setDataLoaded(true);
      } catch (error) {
        console.error('Error fetching time remaining', error);
      }
    };

    const updateLocalTime = () => {
      setTimeLeft((prevTime) => {
        const {totalSeconds } = prevTime;
        const newTotalSeconds = Math.floor(totalSeconds -1);
        const newSeconds = Math.floor(newTotalSeconds%60);

        const newMinutes = Math.floor((newTotalSeconds/60)%60);
        const newHours = Math.floor((newTotalSeconds/60/60)%24);
        const newDays = Math.floor(newTotalSeconds/60/60/24);

        return {
          days: newDays >= 0 ? newDays : 0,
          hours: newHours >= 0 ? newHours : 0,
          minutes: newMinutes >= 0 ? newMinutes : 0,
          seconds: newSeconds >= 0 ? newSeconds : 0,
          totalSeconds: newTotalSeconds
        };
      });
    };
    useEffect(() =>{
        fetchTimeRemaining();
        const intervalId = setInterval(updateLocalTime, 1000);
        return () => clearInterval(intervalId);
    },[])
    if (!dataLoaded) {
      return(<Spinner>Fetching time remaining to Canada</Spinner>);  
    };
    return (
      <div id="TimeUntilCanada" className="TimeUntilCanada">
        <section className="wrapper">
          <div className="top"></div>
          <div className="timeRemaning">Days: {timeLeft.days} Hours: {timeLeft.hours} Minutes: {timeLeft.minutes} Seconds: {timeLeft.seconds}</div>
        </section>
      </div>
    );
  };

export default TimeUnilCanada;