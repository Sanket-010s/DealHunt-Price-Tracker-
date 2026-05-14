import { CURRENCY_SYMBOLS } from './constants';

export const formatPrice = (price, currency = 'USD') => {
  if (price === null || price === undefined) return 'N/A';
  const symbol = CURRENCY_SYMBOLS[currency] || currency;
  return `${symbol}${price.toFixed(2)}`;
};

export const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString();
};

export const formatDateTime = (dateString) => {
  return new Date(dateString).toLocaleString();
};

export const calculatePercentageChange = (oldPrice, newPrice) => {
  if (!oldPrice || oldPrice === 0) return 0;
  return (((newPrice - oldPrice) / oldPrice) * 100).toFixed(1);
};
