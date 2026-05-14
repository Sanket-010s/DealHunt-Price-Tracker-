import { Bell } from 'lucide-react';

const AlertBadge = ({ alert }) => {
  const getAlertText = () => {
    if (alert.alert_type === 'absolute') {
      return `Target: ${alert.target_price}`;
    } else if (alert.alert_type === 'percentage') {
      return `Drop: ${alert.percentage_drop}%`;
    } else {
      return 'Any Drop';
    }
  };

  return (
    <div className="inline-flex items-center gap-1 px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm">
      <Bell size={14} />
      <span>{getAlertText()}</span>
    </div>
  );
};

export default AlertBadge;
