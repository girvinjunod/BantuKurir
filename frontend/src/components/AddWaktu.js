import {useState} from 'react';


const AddWaktu = ({onAdd}) => {
    const [time, setTime] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!time){
            alert("Input Kosong");
            return;
        }
        onAdd({time});
        setTime('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>Waktu Pengiriman</h3>
            <div className="form-control">
                <label>Waktu Pengiriman Dalam Jam</label>
                <input type = "time" step="1" placeholder="Waktu Pengiriman" value={time} 
                onChange ={(e) => setTime(e.target.value)}
                />
            </div>
            <input type='submit' className='btn btn-block' value='Tentukan Waktu Pengiriman'/>
        </form>
    )
}


export default AddWaktu