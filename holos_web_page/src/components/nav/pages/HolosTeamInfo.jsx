import React, {useContext, useState} from "react";
import {Card, CardBody, Col, Container, Row} from "react-bootstrap";
import Type from "./Type.jsx";
import Particle from "../../Particle.jsx";
import badger from "../../../assets/BuckyBadger.png"

export default function HolosTeamInfo(props) {
    const members = ["Yibo Kong", "Jianbang Sun", "Yuhan Zhang", "Boyan Li", "DongJie Duan"]

    return <>
    <Container fluid className="home-section" id="home">
        <Particle/>
            <Container className="home-content">
                <Col><h2>We are</h2></Col>
                <h2><Type/></h2>
            </Container>
        <br/>
        <Container fluid className="home-about-section home-about-description" id="about">
            <Container>
                <h4>Members</h4>
                <Row>
                    {members.map((member)=>{
                        return <Col key={member} sm={4} md={3} xl={2}>
                            <Card >
                                <img src={badger} alt={"Personal Photo"}/>
                                <Card.Title>{member}</Card.Title>
                                <Card.Body>Badger</Card.Body>
                            </Card>
                        </Col>
                    })}
                </Row>
            </Container>
        </Container>
    </Container>
    </>

}