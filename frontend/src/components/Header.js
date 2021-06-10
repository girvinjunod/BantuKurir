import Button from "./Button";

const Header = ({onClear, text}) => {
    const onClick = () =>{
        console.log("tes")
        onClear()
    };
    return (
        <header className = 'header'>
            <h1>{text}</h1>
            <Button onClick = {onClick} text="Clear"/>
        </header>
    )
}

export default Header
