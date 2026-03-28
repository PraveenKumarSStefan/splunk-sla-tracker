import requests, logging
log = logging.getLogger(__name__)
class SLAAlerter:
    def __init__(self, cfg): self.webhook = cfg.get("slack_webhook")
    def send_breach_warning(self, inc):
        if not self.webhook: return
        try: requests.post(self.webhook,json={"text":f"⚣SLA Warning: {inc}"},timeout=10)
        except Exception as e: log.error(f"Alert failed: {e}")
