import { FaTimes } from 'react-icons/fa';

const Tanggal = ({ info, onDelete }) => {
    info = info[0]
    return (
        <>
        <h4>Tanggal Pengiriman</h4>
        <div className="syarat">
            <h3>YYYY:MM:DD  -  {info.tanggal} 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(info.id)}/> </h3>
        </div>
        <br/>
        </>
    )
}

export default Tanggal