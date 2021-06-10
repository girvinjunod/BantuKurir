import { FaTimes } from 'react-icons/fa';

const Lokasi = ({ lokasi, onDelete }) => {
    return (
        <div className="syarat">
            <h3>{lokasi.lokasi} : ({lokasi.x}, {lokasi.y}) 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(lokasi.id)}/> </h3>
        </div>
    )
}

export default Lokasi