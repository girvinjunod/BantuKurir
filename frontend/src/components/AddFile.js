import {useState} from 'react';


const AddFile = ({onAdd, onClear}) => {
    const [namafile, setNamaFile] = useState(null)
    const onSubmit = (e) => {
        e.preventDefault();
        if (!namafile){
            alert("Input kosong")
            return 
        }
        onClear()
        var formData = new FormData();
        console.log(namafile)
        for (var i = 0; i < namafile.length; i++) {
            console.log(namafile[i])
            formData.append('files[]', namafile[i]);
        }
        console.log(formData)
        onAdd(formData)
    }
    
    return (
        <form className="add-form" onSubmit = {onSubmit}>
            <h3>File</h3>
            <div className="form-control">
                <input type = "file" placeholder="filetes" name="filefield" accept=".txt" multiple="multiple" encType="multipart/form-data"
                 id="filefield"
                onChange ={(e) => setNamaFile(e.target.files)}
                />
            </div>
            <input type='submit' className='btn' value='Cari Jalur Terpendek'/>
        </form>
    )
}


export default AddFile