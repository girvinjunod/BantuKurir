import { FaTimes } from 'react-icons/fa';

const Identitas = ({ info, onDelete }) => {
    info = info[0]
    return (
        <>
        <h4>Identitas Kurir</h4>
        <div className="syarat">
            <h3>Nama : {info.nama} 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(info.id)}/> </h3>
        </div>
        <br/>
        </>
    )
}

export default Identitas