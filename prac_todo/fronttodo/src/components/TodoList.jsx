import { useEffect } from "react"
import { useState } from "react"
const TodoList =()=>{
    const [todos,setTodos] = useState([])
    const [newTodo,setNewTodo] = useState('')

    useEffect(()=>{
        const obtenerTodos = async()=>{
            const peticion = await fetch("http://127.0.0.1:8000/api/todos/")
            const data = await peticion.json()
            setTodos(data)
        }
        obtenerTodos()
    },[todos])
    

    const agregarTodo = async()=>{
        const peticion = await fetch("http://127.0.0.1:8000/api/todos/",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({title:newTodo,estado:false})
        })
        setTodos([...todos,peticion])
    }



    return(
        <>
        <h1>LISTA TAREAS</h1>

        <input type="text" value={newTodo} onChange={(e)=>setNewTodo(e.target.value)}/>
        <button onClick={agregarTodo}>Agregar</button>
        
        <ul>
            {todos.map((todo)=>(
                <li key={todo.id}>
                        <p>{todo.title}</p>
                </li>
            ))}
        </ul>
        </>
    )
}
export default TodoList