import {useState} from 'react';


const AddTanggal = ({onAdd}) => {
    const [tanggal, setTanggal] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!tanggal){
            alert("Input Kosong");
            return;
        }
        onAdd({tanggal});
        setTanggal('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>Tanggal Pengiriman</h3>
            <div className="form-control">
                <label>Tanggal</label>
                <input type = "date" placeholder="Tanggal Pengiriman" value={tanggal} 
                onChange ={(e) => setTanggal(e.target.value)}
                />
            </div>
            <input type='submit' className='btn btn-block' value='Tentukan Tanggal Pengiriman'/>
        </form>
    )
}


export default AddTanggal