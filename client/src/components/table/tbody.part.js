import { useState, useEffect } from 'react';
import axios from 'axios';

function Tbody(props) {

    // const [expandclass, setexpandclass] = useState("Expand");

    // const onClickHandler = () => {
    //     if (expandclass === "Expand")
    //         setexpandclass("Expand_open")
    //     else
    //         setexpandclass("Expand")
    // }

    if (props.Data.length !== 0) {
        console.log(props.Data);
        return (
            <tbody>
                {props.Data.map((value) => {
                    return (
                        <tr className='Hello' key={value.id}>
                            {/* <td className='p-checkbox'> {/*className="p-checkbox" 
                <input type="checkbox" name="tdbox1" id="td1box" />
            </td> */}
                            <td className='p-id'>
                                {value.id}
                            </td>
                            <td>
                               {value.name}
                            </td>

                            <td>
                                {value.email}
                            </td>

                            <td>
                                {value.shift_duration}
                            </td>

                            <td>
                                <div className="expand-data">
                                    <h5 className="status-label inbox">Inbox</h5>
                                </div>
                            </td>

                        </tr>
                    );
                })}

            </tbody>
        );
    }
    else { return (<tbody></tbody>); }
}

export default Tbody;