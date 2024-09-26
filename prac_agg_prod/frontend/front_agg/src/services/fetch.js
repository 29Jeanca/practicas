const API_URL = 'http://127.0.0.1:8000/api/';

const getData = async(endpoint)=>{
    try {
        const response = await fetch(`${API_URL}${endpoint}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data', error);
    }
}
export { getData }
const postData = async(endpoint, data)=>{
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error('Error posting data', error);
    }
}
export { postData }