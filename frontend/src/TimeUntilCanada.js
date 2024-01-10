import React, {useState, useEffect} from 'react';
import './TimeUntilCanada.css'

const TimeUnilCanada = () => {

  const [timeLeft, setTimeLeft] = useState({
    days: null,
    hours: null,
    minutes: null,
    seconds: null,
  });

    const fetchTimeRemaining = async () => {
      try {
        const response = await fetch('/timeUntilCanada', { method: 'GET' });
        const data = await response.json();
        setTimeLeft(data);
      } catch (error) {
        console.error('Error fetching time remaining', error);
      }
    };

    const updateLocalTime = () => {
      setTimeLeft((prevTime) => {
        const { days, hours, minutes, seconds } = prevTime;
    
        const newSeconds = seconds > 0 ? seconds - 1 : 59;
        const newMinutes = newSeconds === 59 ? minutes - 1 : minutes;
        const newHours = newMinutes === 59 ? hours - 1 : hours;
        const newDays = newHours === 59 ? days - 1 : days;
    
        return {
          days: newDays >= 0 ? newDays : 0,
          hours: newHours >= 0 ? newHours : 0,
          minutes: newMinutes >= 0 ? newMinutes : 0,
          seconds: newSeconds >= 0 ? newSeconds : 0,
        };
      });
    };
    useEffect(() =>{
        fetchTimeRemaining();
        const intervalId = setInterval(updateLocalTime, 1000);
        return () => clearInterval(intervalId);
    },[])

    return (
      <div id="TimeUntilCanada" className="TimeUntilCanada">
        {timeLeft.days !== null ? (
        <section class="wrapper">
          <div class="top">Time Until Canada</div>
          <div class="timeRemaning">Days: {timeLeft.days} Hours: {timeLeft.hours} Minutes: {timeLeft.minutes} Seconds: {timeLeft.seconds}</div>
        </section>
        ) : (
          <p>Loading...</p>
        )}

      </div>
    );
  };

export default TimeUnilCanada;