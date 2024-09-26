import CardProduct from "./CardProduct"
const ListProduct = ({ products }) => {
    return (
        <div>
           {products && products.length > 0 ? (
    products.map((product, index) => (
        <CardProduct 
            key={index}
            name={product.name}
            price={product.price}
            description={product.description}
            image={product.image}
        />
    ))
) : (
    <p>No products available</p>
)}

        </div>
    )
}
export default ListProduct