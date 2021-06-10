import { FaTimes } from 'react-icons/fa';

const Lokasi = ({ titik, onDelete }) => {
    titik = titik[0]
    return (
        <>
        <h4>Koordinat Titik Awal </h4>
        <div className="syarat">
            <h3>Perusahaan : ({titik.x}, {titik.y}) 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(titik.id)}/> </h3>
        </div>
        <br/>
        </>
    )
}

export default Lokasi