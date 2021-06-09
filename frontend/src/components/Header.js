import Button from "./Button";

const Header = ({soal, onSubmit}) => {
    const onClick = () =>{
        console.log("tes")
        onSubmit([],[])
    };
    return (
        <header className = 'header'>
            <h1>TSP Solver</h1>
            <Button onClick = {onClick}/>
        </header>
    )
}

export default Header
