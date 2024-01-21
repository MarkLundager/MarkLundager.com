import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import Spinner from '../GeneralComponents/Spinner';

const VideoStreamComponent = () => {
  const [videoLoaded, setVideoLoaded] = useState(false);
  useEffect(() => {
    const socket = io.connect(
      "https://" + "www.marklundager.com" + ":" + "" + "/video_feed"
    );


    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });

    socket.on('video_frame', (data) => {
      console.log("receiving images");
      const img = document.getElementById('video_feed');

      if (data.frame instanceof ArrayBuffer) {
        const base64String = btoa(
          String.fromCharCode.apply(null, new Uint8Array(data.frame))
        );
        img.src = `data:image/jpeg;base64,${base64String}`;
      } else {
        console.error('Invalid frame data received');
      }
      if(!videoLoaded){
        setVideoLoaded(true);
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
    <div>
      {videoLoaded ?(<img id="video_feed" alt="Video Stream" style={{ width: '100%', height: 'auto' }} />):(<Spinner>Loading Video</Spinner>)}
    </div>

  );
};

export default VideoStreamComponent;