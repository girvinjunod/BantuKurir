import {useState} from 'react';


const AddTitikAsal = ({onAdd}) => {
    const [x, setX] = useState('');
    const [y, setY] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!x|| !y){
            alert("Input Kosong");
            return;
        }
        onAdd({x,y});
        setX('');
        setY('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>Koordinat Perusahaan (Titik Awal) </h3>
            <div className="form-control2" >
                <label>X</label>
                <input type = "number" placeholder="Koordinat X Perusahaan" value={x} 
                onChange ={(e) => setX(e.target.value)}
                />
                </div>
            <div className="form-control2" >
                <label>Y</label>
                <input type = "number" placeholder="Koordinat Y Perusahaan" value={y} 
                onChange ={(e) => setY(e.target.value)}
                />
            </div>
            <input type='submit' className='btn btn-block' value='Tentukan Koordinat Perusahaan'/>
        </form>
    )
}


export default AddTitikAsal