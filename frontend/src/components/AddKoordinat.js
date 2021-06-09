import {useState} from 'react';


const AddKoordinat = ({onAdd}) => {
    const [x, setX] = useState('');
    const [y, setY] = useState('');
    const [lokasi, setLokasi] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!x|| !y || !lokasi){
            alert("Input Kosong");
            return;
        }
        onAdd({x,y,lokasi});
        setX('');
        setY('');
        setLokasi('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <div className="form-control">
                <label>Lokasi</label>
                <input type = "text" placeholder="Nama Lokasi" value={lokasi} 
                onChange ={(e) => setLokasi(e.target.value)}
                />
            </div>
            <div className="form-control2" >
                <label>X</label>
                <input type = "number" placeholder="Koordinat X Lokasi" value={x} 
                onChange ={(e) => setX(e.target.value)}
                />
                </div>
            <div className="form-control2" >
                <label>Y</label>
                <input type = "number" placeholder="Koordinat Y Lokasi" value={y} 
                onChange ={(e) => setY(e.target.value)}
                />
            </div>

            <input type='submit' className='btn btn-block' value='Tambah Lokasi Pengiriman'/>
        </form>
    )
}


export default AddKoordinat
