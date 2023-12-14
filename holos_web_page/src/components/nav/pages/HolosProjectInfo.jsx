import React, {useContext, useState} from "react";
import {Button, Col, Row,Container} from "react-bootstrap";
import {useNavigate} from "react-router-dom";
import Particle from "../../Particle.jsx";
export default function HolosProjectInfo(props) {
    const navigate = useNavigate()
    return <div>
        <Container>
            <Particle/>
            <></>
        <h1><strong>Project Overview</strong> </h1>

        <Row>
        <Col xs={12} lg={4} xl={6}>
            <h4><strong>AI-Assisted Course Creation in VR</strong></h4>
        <p>Even with the world around us changing at breakneck speed, the way that we learn has barely changed at all. We are now entering a
            new era of learning that is accessible, personalized, and hands-on at a scale that has never before been possible,
            and Holos is on a mission to turn this new way of learning
            into a reality. The Holos platform enables anyone to quickly create
            and share immersive learning experiences in VR and is now working on utilizing AI to enable instructors to spin up new courses
            in 80% less time. You will be using Unity to test different
            methods for delivering learning content via a virtual agent and will build a demo that helps students learn something new.
            You will also be testing your method to validate that this method creates positive learning outcomes.
        </p>
        </Col><Col xs={12} lg={4} xl={6}>
            <img alt={"scene"} src={"../../../assets/Scene2.png"} className={"responsive-image"}/>
        </Col>
        </Row>

        <Button variant={"success"} onClick={()=>{
            console.log("click")
            window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D"
        }}>Download</Button>
        </Container>
    </div>
}