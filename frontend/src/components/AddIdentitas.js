import {useState} from 'react';


const AddIdentitas= ({onAdd}) => {
    const [nama, setNama] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!nama){
            alert("Input Kosong");
            return;
        }
        onAdd({nama});
        setNama('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>Identitas Kurir</h3>
            <div className="form-control">
                <label>Nama Kurir</label>
                <input type = "text" placeholder="Nama Kurir" value={nama} 
                onChange ={(e) => setNama(e.target.value)}
                />
            </div>
            <input type='submit' className='btn btn-block' value='Tentukan Identitas Kurir'/>
        </form>
    )
}


export default AddIdentitas