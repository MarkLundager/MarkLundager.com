import React, {useState, useEffect} from "react";
import Layout from "../LayoutTemplate/Layout";
import Lamp from './Lamp.js'
import './Controller.css'
import Spinner from "../GeneralComponents/Spinner.js";

const Controller = () => {
    const [availableColors, setAvailableColors] = useState([]);
    const [colorsLoaded, setColorsLoaded] = useState(false);
    const [videoLoaded, setVideoLoaded] = useState(false);
    const videoFeedUrl = 'http://marklundager.com/video_feed';

    const fetchdata = async () => {
        try {
            const response = await fetch('/get_lamp_info', {
                method: 'GET',
            });
    
            if (response.ok) {
                const { colours } = await response.json();
                if (colours) {
                    setAvailableColors(colours.split(','));
                    setColorsLoaded(true);
                    setVideoLoaded(true);
                } else {
                    console.error('Data or data.colours is undefined');
                    setColorsLoaded(true);
                    setVideoLoaded(true);
                }
            } else {
                alert('Could not communicate with server');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };


    useEffect(() => {
        fetchdata();




    }, []);

    const lamps = availableColors.map((color, index) => (
        <Lamp key={index} color={color} />
    ));

    
    return(
        <Layout>
            <div className = "controller-video-container">
            {videoLoaded ? (
            <img src={videoFeedUrl} alt="Video Feed"></img>
            )
            :(<Spinner>Loading video</Spinner>)}
            </div>
            
            <div className="lamps-container-container">
            {
            colorsLoaded ? (
                availableColors.length > 0 ?(<div className="lamps-container">{lamps}</div>)
                :(<div>No buttons available with your authority level</div>)
            )
            :(<Spinner>Loading buttons</Spinner>)
            }
            
            </div>
            
        </Layout>
    )
}

export default Controller;