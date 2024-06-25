import React from "react";
import Layout from "../LayoutTemplate/Layout";
import './AboutMePage.css'  


const AboutMePage = () => {

    return (
        <Layout>
            <section className="AboutMePageContainer">
                <div className="aboutMeContainer">
                    <div className="aboutMeTitle">About Me</div>
                    <div className="profileFrame">
                    </div>
                    <div className="aboutMeText">I'm Mark ...</div>
                </div>
            </section>
        </Layout>

    );
};

export default AboutMePage;