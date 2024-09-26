import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ListProduct from './components/ListProduct'
import { getData } from './services/fetch'
import FormAggProduct from './components/FormAggProduct'
function App() {
  const [products, setProducts] = useState([])

  useEffect(()=>{
    const fetchData = async () => {
      const data = await getData('products/')
      setProducts(data)
    }
    fetchData()
  },[])
  return (
    <>  
      <ListProduct products={products}/>

      <FormAggProduct/>
    </>
  )
}

export default App
