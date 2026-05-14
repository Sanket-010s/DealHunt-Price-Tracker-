export const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

export const ALERT_TYPES = {
  ABSOLUTE: 'absolute',
  PERCENTAGE: 'percentage',
  ANY_DROP: 'any_drop'
};

export const NOTIFICATION_CHANNELS = {
  EMAIL: 'email',
  DISCORD: 'discord'
};

export const CURRENCY_SYMBOLS = {
  USD: '$',
  EUR: '€',
  GBP: '£',
  INR: '₹'
};
