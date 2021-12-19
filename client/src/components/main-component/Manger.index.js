

function Manger_Index() {
    return (
        <BrowserRouter>
            <div className="wrapper">
                <Routes>
                    <Route path="/" element={<Login_Page />} />
                    <Route path='/table' element={<><NavBar /><Table /></>} />
                    <Route path="/form" element={<><NavBar /><Form /></>} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default Manger_Index;