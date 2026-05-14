import { useState, useEffect } from 'react';
import { getProducts } from '../services/products';

export const useProducts = (activeOnly = false) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const data = await getProducts(activeOnly);
      setProducts(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, [activeOnly]);

  return { products, loading, error, refetch: fetchProducts };
};
