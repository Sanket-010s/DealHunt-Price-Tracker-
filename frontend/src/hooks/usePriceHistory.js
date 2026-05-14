import { useState, useEffect } from 'react';
import { getProduct } from '../services/products';

export const usePriceHistory = (productId, days = 30) => {
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchProduct = async () => {
    if (!productId) return;
    
    try {
      setLoading(true);
      const data = await getProduct(productId, days);
      setProduct(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProduct();
  }, [productId, days]);

  return { product, loading, error, refetch: fetchProduct };
};
