import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import HolosNavbar from "./nav/HolosNavbar.jsx";


export default function Holos() {

    return <div>
        <HolosNavbar />
        <div className={"App"} style={{ margin: "1rem" }}>
                <Outlet />
        </div>
    </div>
}