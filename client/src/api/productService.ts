import axios from 'axios';
import { Product } from '../types/product';

const API_URL = 'http://127.0.0.1:8000/product';

export const fetchProductList = async (): Promise<Product[]> => {
    try {
      const response = await axios.get<Product[]>(API_URL,{
        headers: {
            Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnZW5lcmljX3VzZXJuYW1lIn0.PGT_LfogrvXuu-_LUb0-xADPufwvZsgHd-GN5xnYPnU"
            }
        });
      return response.data;
    } catch (error) {
      console.error('Error fetching product list:', error);
      throw error;
    }
  };  

export const fetchProduct = async (id: String): Promise<Product> => {
  try {
    const response = await axios.get<Product>(`${API_URL}/${id}`,{
        headers: {
            Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnZW5lcmljX3VzZXJuYW1lIn0.PGT_LfogrvXuu-_LUb0-xADPufwvZsgHd-GN5xnYPnU"
        }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching product:', error);
    throw error;
  }
};
