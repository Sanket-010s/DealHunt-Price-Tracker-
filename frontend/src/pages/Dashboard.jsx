import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Plus, RefreshCw } from 'lucide-react';
import { useProducts } from '../hooks/useProducts';
import ProductList from '../components/ProductList';
import AddProductModal from '../components/AddProductModal';
import { createProduct, deleteProduct } from '../services/products';

const Dashboard = () => {
  const navigate = useNavigate();
  const { products, loading, error, refetch } = useProducts();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleAddProduct = async (productData) => {
    await createProduct(productData);
    refetch();
  };

  const handleDeleteProduct = async (id) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
      await deleteProduct(id);
      refetch();
    }
  };

  const handleViewProduct = (id) => {
    navigate(`/product/${id}`);
  };

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Price Tracker Dashboard</h1>
          <div className="flex gap-2">
            <button
              onClick={refetch}
              className="px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded hover:bg-gray-300 dark:hover:bg-gray-600 flex items-center gap-2"
            >
              <RefreshCw size={20} />
              Refresh
            </button>
            <button
              onClick={() => setIsModalOpen(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 flex items-center gap-2"
            >
              <Plus size={20} />
              Add Product
            </button>
          </div>
        </div>

        {loading && <p className="text-center text-gray-500">Loading products...</p>}
        {error && <p className="text-center text-red-500">Error: {error}</p>}
        {!loading && !error && (
          <ProductList
            products={products}
            onView={handleViewProduct}
            onDelete={handleDeleteProduct}
          />
        )}

        <AddProductModal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
          onAdd={handleAddProduct}
        />
      </div>
    </div>
  );
};

export default Dashboard;
