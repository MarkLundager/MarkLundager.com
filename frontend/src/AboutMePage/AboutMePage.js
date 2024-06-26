import React from "react";
import Layout from "../LayoutTemplate/Layout";
import './AboutMePage.css'  


const AboutMePage = () => {
    const aboutMeTitle = "About Me"
    const aboutMeParagraph =`I'm Mark, a student in Computer Engineering at the faculty
     of engineering, Lund University in Sweden. I am currently specialising in software but
     I have great interest for AI (specifically reinforcement learning), robotics, 
     computer security (Mainly reverse engineering), compilers and computer graphics. As one might
     be able to conclude swiftly by looking at this website, front end is not my forte. 
     To further hone my skills, I created this website to act as a display of my skills
     within this areas and evidently because I have too much time on my hands.`

     const marklundagerTitle = "MarkLundager.com"
     const marklundagerParagraph = `This website is hosted on my Raspberry Pi 4. I use nginx
     as a reverse proxy to handle the TLS together with "Let's Encrypt". The nginx server then
     forwards the https requests to a python flask server which is hosted locally on the Pi 
     as well. The front end is built using ReactJS. For fun, I made an account system using
     SQlite (which I think suffices for a small website? but will change to a MySQL server
     later on as SQlite has limited functionality when it comes to concurrency). 
     I do not have great expertise in web security but it is my intention to make this website
     as safe as possible for learning purposes. Below is a list of vulnerabillities I wish to 
     combat. If you happen to find something please let me know! To find the details of
     the website, visit my github which you can find under "contact me".`

     const vulnerabillitiesList = `\n-SQL injections
     -Cross-Site Scripting (XSS)
     -Cross-Site Request Forgery (CSRF)
     -Sensitive Data Exposure
     -Insecure Direct Object References (IDOR)
     -Database flooding attacks`
     
    const projectIdeasTitle = "Project ideas"
    const projectIdeasText = "Here are a list of project Ideas so far:"

    return (
        <Layout>
            <section className="AboutMePageContainer">
                <div className="aboutMeContainer">
                    <div className="paragraphTitles">{aboutMeTitle}</div>
                    <div className="profileFrameAndTextContainer">
                        <div className="profileFrame"></div>
                        <p className="aboutMeText">{aboutMeParagraph}</p>
                    </div>
                    <div className="paragraphTitles">{marklundagerTitle}</div>
                    <p className="markLundagerText">{marklundagerParagraph}</p>
                    <p className="vulnlist">{vulnerabillitiesList}</p>
                </div>
            </section>
        </Layout>

    );
};

export default AboutMePage;