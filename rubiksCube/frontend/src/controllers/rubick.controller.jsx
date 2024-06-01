import axios from 'axios';
const getSolverByPattern=async (pattern)=>{
    const url=' http://127.0.0.1:5000'
    try {
        const response=await axios.post(url,pattern);
        return response.data;
    }catch (e) {
        console.log(e)
    }
}

export  {getSolverByPattern}
