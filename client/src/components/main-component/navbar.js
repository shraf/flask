import '../css/nav-style.css';

import 'https://kit.fontawesome.com/b99e675b6e.js';
import { Link } from 'react-router-dom';

function NavBar() {
    return (
        <div className="sidebar">
            <a href="/"><h2>Sidebar</h2></a>
            <ul>
                <li><Link to="/table"><i className="fas fa-home"></i>index</Link></li>
                <li><Link to="/form"><i className="fas fa-user"></i>data table</Link></li>
                <li><a href="/waitingList"><i className="fas fa-address-card"></i>suervy</a></li>

            </ul>
            <div className="social_media">
                <a href="https://www.facebook.com/ibrahim.elbana.10"><i className="fab fa-facebook-f"></i></a>
                <a href="https://www.youtube.com/channel/UCmbA_l0FXACyjbTOt7T_l-w"><i className="fab fa-youtube"></i></a>
                <a href="http://instagram.com/baheradelahmed?utm_source=qr"><i className="fab fa-instagram"></i></a>
            </div>
        </div>
    );
}

export default NavBar;