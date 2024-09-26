import { postData } from "../services/fetch"
import { useState } from "react"
const FormAggProduct = ()=>{
    const [name, setName] = useState('')
    const [price, setPrice] = useState('')
    const [description, setDescription] = useState('')
    const [image, setImage] = useState('')

    const aggProduct=async(e)=>{
        e.preventDefault()
        const data = {
            name,
            price,
            description,
            image
        }
        await postData('products/', data)
    }
    return(
        <div>
            <h1>Formulario de Agregar Producto</h1>
            <form onSubmit={aggProduct}>
                <label>Nombre:</label>
                <input type="text" name="name" onChange={(e)=>setName(e.target.value)}/>
                <label>Precio:</label>
                <input type="text" name="price" onChange={(e)=>setPrice(e.target.value)}/>
                <label>Descripción:</label>
                <input type="text" name="description" onChange={(e)=>setDescription(e.target.value)}/>
                <label>Imagen:</label>
                <input type="text" name="image" onChange={(e)=>setImage(e.target.value)}/>
                <button type="submit">Agregar Producto</button>
            </form>
        </div>
    )
}
export default FormAggProduct