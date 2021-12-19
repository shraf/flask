import '../css/main.css';
import '../css/table.css';
import '../css/table-design2.css';

import Thead from "./thead.part";
import Tbody from "./tbody.part";
import axios from 'axios';
import React, { useState, useEffect } from 'react';

import { useJwt } from "react-jwt";


function Table() {


    const [token, settoken] = useState("")
    const [UserData, setUserData] = useState([])

    useEffect(() => {
        settoken(localStorage.getItem("token"));
    },[])

    const { decodedToken } = useJwt(token);

    useEffect(() => {
        if(token)
        axios.get("https://attendence123.herokuapp.com/employee", {headers:{authorization:token}})
        .then(res => {setUserData(res.data);})
        .catch(err => {console.log(err);})
    }, [token])

    if (decodedToken && decodedToken.type === "admin") {
        return (
            <div className="main_content">

                <div className="d1214">
                    <div className='info'>
                        <div>
                            <h2 className="table-header">Mangement Table</h2>
                            {/* Table Content */}
                            <table className='Emp-table'>
                                <Thead />

                                <Tbody Data={UserData}/>
                            </table>

                        </div>
                    </div>
                </div>
            </div>
        );
    }
    else {
        return (
            <div className="main_content">
                <div className='info'>
                    <h1>Not Allowed</h1>
                </div>
            </div>
        );
    }
}

export default Table;