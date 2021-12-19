import logo from './logo.svg';
import './components/css/main-positioning.css';
import './components/css/main.css';

import Form from './components/form/form.index';
import NavBar from './components/main-component/navbar';
import Table from './components/table/table.index';
import Login_Page from './components/login-page/login.index';
import WaitingCard from './components/Waiting_list/Waiting_Card';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div className="wrapper">
        <Routes>
          <Route path="/" element={<Login_Page />} />
          <Route path='/table' element={<><NavBar /><Table/></>} />
          <Route path="/form" element ={<><NavBar /><Form/></>} />
          <Route path="/waitingList" element ={<><NavBar /><WaitingCard/></>} />
        </Routes>
      </div>
    </BrowserRouter>
  ); 
}

export default App;