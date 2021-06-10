import { FaTimes } from 'react-icons/fa';

const Kecepatan = ({ info, onDelete }) => {
    info = info[0]
    return (
        <>
        <h4>Kecepatan Rata-rata Kurir</h4>
        <div className="syarat">
            <h3>v = {info.kecepatan} km/jam
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(info.id)}/> </h3>
        </div>
        <br/>
        </>
    )
}

export default Kecepatan