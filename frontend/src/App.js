
import './App.css';
import {useState} from 'react';
import axios from 'axios';
import Header from './components/Header';
import AddKoordinat from './components/AddKoordinat';
import AddIdentitas from './components/AddIdentitas';


function App() {
  //koor titik asal
  const [titikasal, setTitikAsal] = useState([]);
  //koordinat per lokasi dan nama
  const [koordinat, setKoordinat] = useState([]);
  //identitas kurir
  const [indentitas, setIdentitas] = useState([]);
  //Waktu pengiriman
  const [waktu, setWaktu] = useState([]);
  //Kecepatan
  const [kecepatan, setKecepatan] = useState([]);

  // add input
  const addKoordinat = (s) =>{
    const id = Math.floor(Math.random() * 10000) + 1;
    const newKoordinat = { id, ...s };
    setKoordinat([...koordinat, newKoordinat])
  }

  const addIdentitas = (s) =>{
    setIdentitas([])
    const id = Math.floor(Math.random() * 10000) + 1;
    const newIdentitas = { id, ...s };
    setIdentitas([newIdentitas])
  }

  // delete syarat
  const deleteKoordinat = (id) => {
      setKoordinat(koordinat.filter((s) => s.id !== id));
  }

//Dibuat koor awal selalu ada di depan
const getGraph = async (namalokasi,koorlokasi) => {
  const obj = { namalokasi:namalokasi, koorlokasi:koorlokasi }
  await axios.post('/graph', obj)//.then(res => {
    //setJawaban([res.data]);
  //})
}
//header
//input sisa info
//input nama dan koordinat per lokasi
//get result
  return (
    <div className="container">
      <Header onSubmit = {getGraph}/>
      <AddKoordinat onAdd = {addKoordinat}/>
      <AddIdentitas onAdd = {addIdentitas} />
      <p>Hello</p>
    </div>
  );
}

export default App;
