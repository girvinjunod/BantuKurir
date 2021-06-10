
import './App.css';
import {useState} from 'react';
import axios from 'axios';
import Header from './components/Header';
import AddKoordinat from './components/AddKoordinat';
import AddIdentitas from './components/AddIdentitas';
import AddWaktu from './components/AddWaktu';
import AddKecepatan from './components/AddKecepatan';
import AddTitikAsal from './components/AddTitikAsal';
import Lokasi2 from './components/Lokasi2';
import TitikAwal from './components/TitikAwal';
import Identitas from './components/Identitas';
import Waktu from './components/Waktu';
import Kecepatan from './components/Kecepatan';
import AddTanggal from './components/AddTanggal';
import Tanggal from './components/Tanggal';
import GetJawaban2 from './components/GetJawaban2';
import GetJawaban from './components/GetJawaban';
import Jawaban from './components/Jawaban';
import Jawaban2 from './components/Jawaban2';
import AddFile from './components/AddFile';


function App() {
  //koor titik asal
  const [titikasal, setTitikAsal] = useState([]);
  //koordinat per lokasi dan nama
  const [koordinat, setKoordinat] = useState([]);
  //identitas kurir
  const [identitas, setIdentitas] = useState([]);
  //Waktu pengiriman (HH:MM:SS)
  const [waktu, setWaktu] = useState([]);
  //Kecepatan
  const [kecepatan, setKecepatan] = useState([]);



  // add input
  const addKoordinat = (s) =>{
    const id = Math.floor(Math.random() * 10000) + 1;
    const newKoordinat = { id, ...s };
    setKoordinat([...koordinat, newKoordinat])
  }

  const addTitikAsal = (s) =>{
    const id = Math.floor(Math.random() * 10000) + 1;
    const newTitikAsal = { id, ...s };
    setTitikAsal([newTitikAsal])
  }


  const addIdentitas = (s) =>{
    setIdentitas([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newIdentitas = { id, ...s };
    setIdentitas([newIdentitas])
  }

  const addWaktu = (s) =>{
    setWaktu([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newWaktu = { id, ...s };
    setWaktu([newWaktu])
  }

  const addKecepatan = (s) =>{
    setKecepatan([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newKecepatan = { id, ...s };
    setKecepatan([newKecepatan])
  }

  // delete syarat
  const deleteKoordinat = (id) => {
      setKoordinat(koordinat.filter((s) => s.id !== id));
  }

  
  // delete titik asal
  const deleteTitikAsal = () => {
    setTitikAsal([]);
}
  // delete identitas
  const deleteIdentitas = () => {
    setIdentitas([]);
}

  // delete waktu
  const deleteWaktu = () => {
    setWaktu([]);
}

  // delete kecepatan
  const deleteKecepatan = () => {
    setKecepatan([]);
}


  // delete all
  const deleteAll = () => {
    setTitikAsal([])
    setKoordinat([])
    setIdentitas([])
    setWaktu([])
    setKecepatan([])
    setJawaban([])
  }
  

  //Database
  //identitas kurir 2
  const [identitas2, setIdentitas2] = useState([]);
  //tanggal 
  const [tanggal, setTanggal] = useState([]);


  const addIdentitas2 = (s) =>{
    setIdentitas2([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newIdentitas = { id, ...s };
    setIdentitas2([newIdentitas])
  }

  const addTanggal = (s) =>{
    setTanggal([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newTanggal = { id, ...s };
    setTanggal([newTanggal])
  }

    // delete identitas
    const deleteIdentitas2 = () => {
      setIdentitas2([]);
  }

    // delete tanggal
      const deleteTanggal = () => {
        setTanggal([]);
    }

    // delete all 2
    const deleteAll2 = () => {
      setIdentitas2([])
      setTanggal([])
      setJawaban2([])
    }

  //jawaban
  //non bonus
  const [jawaban, setJawaban] = useState([]);
  //bonus
  const [jawaban2, setJawaban2] = useState([]);

//Dibuat koor awal selalu ada di depan
const getGraph = async (namalokasi, koorlokasi, identitas, waktu, kecepatan) => {
  let obj = {namalokasi:namalokasi, koorlokasi:koorlokasi, identitas:identitas, waktu:waktu, kecepatan:kecepatan}
  await axios.post('/graph', obj).then(res => {
    setJawaban([res.data]);
  })
}

const getData = async (i,t) => {
  let obj = { identitas:i, tanggal:t }
  await axios.post('/data', obj).then(res => {
    setJawaban2([res.data]);
  })
}

const getFromFile = async (obj) => {
  await axios.post('/file', obj).then(res => {
    console.log(res.data)
    setJawaban([res.data]);
  })
}


  return (
    <>
    <div className="container">
      <header className = 'title'>
            <h1>TSP Solver</h1>
      </header>
      <div>
      <header className = 'header'>
            <h1>Input Dari File</h1>
      </header>
      <AddFile onAdd = {getFromFile} onClear = {deleteAll}/>
      </div>
      <Header text = "Input Langsung" onClear = {deleteAll}/>
      <AddTitikAsal onAdd = {addTitikAsal} />
      {titikasal.length > 0 ? <TitikAwal titik = {titikasal} onDelete = {deleteTitikAsal}/> : ""}
      <AddKoordinat onAdd = {addKoordinat}/>
      {koordinat.length > 0 ? <Lokasi2 lokasi = {koordinat} onDelete = {deleteKoordinat}/> : ""}
      <AddIdentitas onAdd = {addIdentitas} />
      {identitas.length > 0 ? <Identitas info = {identitas} onDelete = {deleteIdentitas}/> : ""}
      <AddWaktu onAdd = {addWaktu} />
      {waktu.length > 0 ? <Waktu info = {waktu} onDelete = {deleteWaktu}/> : ""}
      <AddKecepatan onAdd = {addKecepatan} />
      {kecepatan.length > 0 ? <Kecepatan info = {kecepatan} onDelete = {deleteKecepatan}/> : ""}
      <GetJawaban titikasal = {titikasal} koordinat = {koordinat} identitas = {identitas} waktu = {waktu}
      kecepatan={kecepatan}  onSubmit={getGraph}/>
      { jawaban.length > 0 ? <Jawaban key={jawaban[0].id} jawaban = {jawaban[0]}/> : "" }
      
    </div>
    <div className="container2">
    <Header text = "Cari Info Pengiriman" onClear={deleteAll2}/>
    <AddIdentitas onAdd = {addIdentitas2} />
    {identitas2.length > 0 ? <Identitas info = {identitas2} onDelete = {deleteIdentitas2}/> : ""}
    <AddTanggal onAdd = {addTanggal} />
    {tanggal.length > 0 ? <Tanggal info = {tanggal} onDelete = {deleteTanggal}/> : ""}
    <GetJawaban2 identitas={identitas2} tanggal={tanggal} onSubmit={getData} />
    { jawaban2.length > 0 ? <Jawaban2 key={jawaban2[0].id} jawaban = {jawaban2[0]}/> : "" }
    </div>
    </>
  );
}

export default App;
