import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import Spinner from '../GeneralComponents/Spinner';
import './VideoStreamComponent.css'

const VideoStreamComponent = () => {
  const [videoLoaded, setVideoLoaded] = useState(false);
  const [imgSrc, setImgSrc] = useState('');
  useEffect(() => {
    const socket = io.connect(
      "wss://" + "www.marklundager.com" + ":" + "" + "/video_feed"
    );

    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });

    // window.addEventListener('beforeunload', () => {
    //   socket.disconnect();
    // });

    socket.on('video_frame', (data) => {
      const img = document.getElementById('video_feed');

      if (data.frame instanceof ArrayBuffer) {
        console.log("image received");
        const base64String = btoa(
          String.fromCharCode.apply(null, new Uint8Array(data.frame))
        );
        setImgSrc(`data:image/jpeg;base64,${base64String}`);
        setVideoLoaded(true);
      } else {
        console.error('Invalid frame data received');
      }

    });

    console.log("emitting request_frame");
    socket.emit('request_frame');

    // Cleanup when the component unmounts
    return () => {
      socket.disconnect();
    };
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div className = "videoContainer">
      {videoLoaded ?(<img id="video_feed" alt="Video Stream" src={imgSrc} style={{ width: '100%', height: '59vh' }} />):(<Spinner>Loading Video</Spinner>)}
    </div>

  );
};

export default VideoStreamComponent;