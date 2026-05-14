import { formatDateTime } from '../utils/formatters';
import { Mail, MessageSquare, CheckCircle, XCircle } from 'lucide-react';

const NotificationLog = ({ notifications }) => {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Recent Notifications</h3>
      <div className="space-y-3">
        {notifications.length === 0 ? (
          <p className="text-gray-500 dark:text-gray-400">No notifications yet</p>
        ) : (
          notifications.map(notif => (
            <div key={notif.id} className="flex items-start gap-3 p-3 bg-gray-50 dark:bg-gray-700 rounded">
              {notif.channel === 'email' ? <Mail size={20} /> : <MessageSquare size={20} />}
              <div className="flex-1">
                <p className="text-sm text-gray-900 dark:text-white">{notif.message}</p>
                <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                  {formatDateTime(notif.sent_at)}
                </p>
              </div>
              {notif.success ? (
                <CheckCircle size={20} className="text-green-600" />
              ) : (
                <XCircle size={20} className="text-red-600" />
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default NotificationLog;
