import React, {useState, useEffect} from "react";
import Layout from "../LayoutTemplate/Layout";
import Lamp from './Lamp.js'
import './Controller.css'
import Spinner from "../GeneralComponents/Spinner.js";

const Controller = () => {
    const [availableColors, setAvailableColors] = useState([]);
    const [colorsLoaded, setColorsLoaded] = useState(false);
    //const [videoLoaded, setVideoLoaded] = useState(false);

    useEffect(() => {
        fetch('/get_lamp_info')
            .then(response => response.json())
            .then(data => {
                setAvailableColors(data.colours.split(','));
                setColorsLoaded(true);
            })
            .catch(error => console.error('Error fetching lamp info:', error));
    }, []);

    const lamps = availableColors.map((color, index) => (
        <Lamp key={index} color={color} />
    ));

    
    return(
        <Layout>
            
            {false /*change for videoloaded attribute*/? (
            <div className = "controller-video-container">
            <div className ="controller-video"></div>
            </div>)
            :(<div className="spinner-video-container"><Spinner>Loading video</Spinner></div>)}
            
            
            {colorsLoaded ? (
            <div className="lamps-container-container">
            <div className="lamps-container">{lamps}</div>
            </div>
            ):<div className="spinnnner-container"><Spinner>Loading Lamps</Spinner></div>}
            
            
        </Layout>
    )
}

export default Controller;