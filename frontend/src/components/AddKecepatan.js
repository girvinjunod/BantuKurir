import {useState} from 'react';


const AddKecepatan= ({onAdd}) => {
    const [kecepatan, setKecepatan] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        if (!kecepatan){
            alert("Input Kosong");
            return;
        }
        if (kecepatan <= 0){
            alert("Kecepatan harus lebih besar dari 0")
            setKecepatan('');
            return;
        }
        onAdd({kecepatan});
        setKecepatan('');
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>Kecepatan Rata-rata Kurir</h3>
            <div className="form-control">
                <label>Kecepatan Rata-rata</label>
                <input type = "number" placeholder="Kecepatan Rata-rata" value={kecepatan} 
                onChange ={(e) => setKecepatan(e.target.value)}
                />
            </div>
            <input type='submit' className='btn btn-block' value='Tentukan Kecepatan Rata-rata Kurir'/>
        </form>
    )
}


export default AddKecepatan