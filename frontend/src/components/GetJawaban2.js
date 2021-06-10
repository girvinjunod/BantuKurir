import Button from "./Button";

const GetJawaban2 = ({identitas, tanggal, onSubmit}) => {
    const onClick = () =>{
        if (identitas.length === 0 || tanggal.length === 0){
            alert("Input Kosong");
            return;
        }
        let i = identitas[0]
        let t = tanggal[0]

        onSubmit(i,t);
    };
    return (
            <Button onClick = {onClick} text="Cari"/>
    )
}

export default GetJawaban2
