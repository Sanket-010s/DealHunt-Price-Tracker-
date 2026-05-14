import { useState, useEffect } from 'react';
import { getAlerts, createAlert, deleteAlert } from '../services/alerts';
import { getProducts } from '../services/products';
import AlertBadge from '../components/AlertBadge';
import { Plus, Trash2 } from 'lucide-react';

const Alerts = () => {
  const [alerts, setAlerts] = useState([]);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    product_id: '',
    alert_type: 'absolute',
    target_price: '',
    percentage_drop: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [alertsData, productsData] = await Promise.all([
        getAlerts(),
        getProducts()
      ]);
      setAlerts(alertsData);
      setProducts(productsData);
    } catch (err) {
      alert('Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createAlert(formData);
      setShowForm(false);
      setFormData({ product_id: '', alert_type: 'absolute', target_price: '', percentage_drop: '' });
      fetchData();
    } catch (err) {
      alert('Failed to create alert');
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Delete this alert?')) {
      await deleteAlert(id);
      fetchData();
    }
  };

  if (loading) return <div className="min-h-screen bg-gray-100 dark:bg-gray-900 flex items-center justify-center"><p>Loading...</p></div>;

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Price Alerts</h1>
          <button
            onClick={() => setShowForm(!showForm)}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 flex items-center gap-2"
          >
            <Plus size={20} />
            New Alert
          </button>
        </div>

        {showForm && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-6">
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">Product</label>
                <select
                  value={formData.product_id}
                  onChange={(e) => setFormData({ ...formData, product_id: e.target.value })}
                  required
                  className="w-full px-3 py-2 border rounded dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                >
                  <option value="">Select a product</option>
                  {products.map(p => (
                    <option key={p.id} value={p.id}>{p.name}</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">Alert Type</label>
                <select
                  value={formData.alert_type}
                  onChange={(e) => setFormData({ ...formData, alert_type: e.target.value })}
                  className="w-full px-3 py-2 border rounded dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                >
                  <option value="absolute">Absolute Price</option>
                  <option value="percentage">Percentage Drop</option>
                  <option value="any_drop">Any Price Drop</option>
                </select>
              </div>
              {formData.alert_type === 'absolute' && (
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">Target Price</label>
                  <input
                    type="number"
                    step="0.01"
                    value={formData.target_price}
                    onChange={(e) => setFormData({ ...formData, target_price: e.target.value })}
                    required
                    className="w-full px-3 py-2 border rounded dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  />
                </div>
              )}
              {formData.alert_type === 'percentage' && (
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white">Percentage Drop (%)</label>
                  <input
                    type="number"
                    step="0.1"
                    value={formData.percentage_drop}
                    onChange={(e) => setFormData({ ...formData, percentage_drop: e.target.value })}
                    required
                    className="w-full px-3 py-2 border rounded dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  />
                </div>
              )}
              <div className="flex gap-2">
                <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
                  Create Alert
                </button>
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded hover:bg-gray-300"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        )}

        <div className="space-y-4">
          {alerts.map(alert => {
            const product = products.find(p => p.id === alert.product_id);
            return (
              <div key={alert.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-gray-900 dark:text-white mb-2">{product?.name || 'Unknown Product'}</h3>
                  <AlertBadge alert={alert} />
                </div>
                <button
                  onClick={() => handleDelete(alert.id)}
                  className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 flex items-center gap-2"
                >
                  <Trash2 size={16} />
                  Delete
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Alerts;
