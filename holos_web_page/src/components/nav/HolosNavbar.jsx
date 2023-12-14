
import { Container, Nav, Navbar } from "react-bootstrap";
import { Link } from "react-router-dom";
import {
    AiOutlineHome,
    AiOutlineTeam,
} from "react-icons/ai";
import crest from '../../assets/uw-crest.svg'

export default function HolosNavbar(props) {
    return <Navbar bg="dark" variant="dark"
                   expanded={true}
                   // fixed="top"
                   expand="md"
                   className={"navbar"} >
        <Container>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Brand as={Link} to="/">
                <img
                    alt="Badger Logo"
                    src={crest}
                    width="30"
                    height="30"
                    className="d-inline-block align-top"
                />{' '}
                Holos
            </Navbar.Brand>
            <Navbar.Collapse id="responsive-navbar-nav" className="me-auto">
                <Nav>
                    <Nav.Link as={Link} to="/">
                        <AiOutlineHome style={{ marginBottom: "2px" }} /> Home</Nav.Link>
                    <Nav.Link as={Link} to="/about-us">
                        <AiOutlineTeam style={{ marginBottom: "2px" }} />About Us</Nav.Link>
                    {/*<Nav.Link as={Link} to="/project">Project</Nav.Link>*/}
                </Nav>
            </Navbar.Collapse>
        </Container>
    </Navbar>
}
