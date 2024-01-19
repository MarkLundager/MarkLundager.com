import React, {useState, useEffect} from "react";
import io from 'socket.io-client';
import Layout from "../LayoutTemplate/Layout";
import Lamp from './Lamp.js'
import './Controller.css'
import Spinner from "../GeneralComponents/Spinner.js";

const Controller = () => {
    const [availableColors, setAvailableColors] = useState([]);
    const [colorsLoaded, setColorsLoaded] = useState(false);
    const [videoLoaded, setVideoLoaded] = useState(false);
    const [videoUrl, setVideoUrl] = useState('');

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
    const startStream = async () => {
        try {
            const response = await fetch('/start_video_stream', {
                method: 'GET',
            });
            if (response.ok) {
                console.log("video start ok");
                setVideoLoaded(true);
            } else {
                setVideoLoaded(true);
            }   console.log("video start bad");
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const stopStream = async () => {
        try {
            const response = await fetch('/stop_video_stream', {
                method: 'GET',
            });
            if (response.ok) {
                console.log("video stop ok");
                setVideoLoaded(false);
            } else {
                setVideoLoaded(false);
            }   console.log("video stop bad");
        } catch (error) {
            console.error('Error:', error);
        }
    };

    useEffect(() => {
        const socket = io.connect('http://marklundager.com/get_video');
    
        socket.on('videoData', (data) => {
          const uint8Array = new Uint8Array(data);
          const blob = new Blob([uint8Array], { type: 'video/mp2t' });
          const url = URL.createObjectURL(blob);
            
          setVideoUrl(url);
          startStream();
          
        });
        return () => {
            socket.disconnect();
          };
        }, []);

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
              <div>
              {videoUrl && <video src={videoUrl} controls />}
            </div>
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