import { BrowserRouter, Route, Routes } from "react-router-dom";

import Holos from "../Holos.jsx";
import HolosLanding from "./pages/HolosLanding.jsx"
import HolosProjectInfo from "./pages/HolosProjectInfo.jsx"
import HolosNoMatch from "./pages/HolosNoMatch.jsx"
import HolosTeamInfo from "./pages/HolosTeamInfo.jsx"

export default function HolosRouter() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Holos />} >
                <Route index element={<HolosProjectInfo />} />
                {/*<Route path="project" element={<HolosProjectInfo />} />*/}
                <Route path="about-us" element={<HolosTeamInfo />} />
                <Route path="*" element={<HolosNoMatch />} />
            </Route>
        </Routes>
    </BrowserRouter>
}