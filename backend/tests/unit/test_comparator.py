import pytest
from app.core.comparator import should_trigger_alert
from app.db.models import Alert, AlertType

def test_absolute_alert_triggered():
    alert = Alert(alert_type=AlertType.ABSOLUTE, target_price=50.0, is_active=True)
    assert should_trigger_alert(alert, 60.0, 45.0) == True

def test_absolute_alert_not_triggered():
    alert = Alert(alert_type=AlertType.ABSOLUTE, target_price=50.0, is_active=True)
    assert should_trigger_alert(alert, 60.0, 55.0) == False

def test_percentage_alert_triggered():
    alert = Alert(alert_type=AlertType.PERCENTAGE, percentage_drop=10.0, is_active=True)
    assert should_trigger_alert(alert, 100.0, 85.0) == True

def test_percentage_alert_not_triggered():
    alert = Alert(alert_type=AlertType.PERCENTAGE, percentage_drop=10.0, is_active=True)
    assert should_trigger_alert(alert, 100.0, 95.0) == False

def test_any_drop_alert_triggered():
    alert = Alert(alert_type=AlertType.ANY_DROP, is_active=True)
    assert should_trigger_alert(alert, 100.0, 99.0) == True

def test_any_drop_alert_not_triggered():
    alert = Alert(alert_type=AlertType.ANY_DROP, is_active=True)
    assert should_trigger_alert(alert, 100.0, 100.0) == False
