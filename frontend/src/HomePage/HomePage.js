import React from "react";
import Layout from "../LayoutTemplate/Layout";
import TimeUnilCanada from "./TimeUntilCanada";
import VideoStreamComponent from"../PiCamera/VideoStreamComponent";

const HomePage = () => {

    return(
        <Layout><TimeUnilCanada></TimeUnilCanada></Layout>
        
    );
};

export default HomePage;