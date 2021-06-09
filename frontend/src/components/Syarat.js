import { FaTimes } from 'react-icons/fa';
const Syarat = ({ syarat, onDelete }) => {
    return (
        <div className="syarat">
            <h3>x ≡ {syarat.sisa} (mod {syarat.pembagi}) 
            <FaTimes style = {{color: 'red', cursor: 'pointer'}} 
            onClick = {() => onDelete(syarat.id)}/> </h3>
        </div>
    )
}

export default Syarat
