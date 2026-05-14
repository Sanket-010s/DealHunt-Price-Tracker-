import ProductCard from './ProductCard';

const ProductList = ({ products, onView, onDelete }) => {
  if (products.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 dark:text-gray-400">No products found. Add your first product to start tracking!</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map(product => (
        <ProductCard
          key={product.id}
          product={product}
          onView={onView}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default ProductList;
