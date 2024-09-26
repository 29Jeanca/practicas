const CardProduct = ({name,price,description,image})=>{
    return(
        <div className="card">
            <img src={image} alt={name}/>
            <h2>{name}</h2>
            <p>{description}</p>
            <p>{price}</p>
        </div>
    )   
}
export default CardProduct