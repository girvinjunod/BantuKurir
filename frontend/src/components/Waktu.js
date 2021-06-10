import { FaTimes } from 'react-icons/fa';

const Waktu = ({ info, onDelete }) => {
    info = info[0]
    return (
        <>
        <h4>Waktu Pengiriman</h4>
        <div className="syarat">
            <h3>Jam:Menit:Detik  -  {info.time} 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(info.id)}/> </h3>
        </div>
        <br/>
        </>
    )
}

export default Waktu