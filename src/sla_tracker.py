"""SLA Tracker - calculates MTTD/MTTR/SLA breach metrics from Splunk.
Author: Praveenkumar S
"""
import logging, csv
from datetime import datetime
from pathlib import Path
from src.splunk_query import SplunkQuery
from src.report_builder import ReportBuilder
from src.sla_alerter import SLAAyerter
_log = logging.getLogger(__name__)
MTTR_Q = "index=incidents sourcetype=incident_log earliest=-30d status=resolved | eval mttr_minutes=round((strptime(resolved_at, '%Y-%m-%dT%H:%M:%S') - strptime(detected_at, '%Y-%m-%dT%H:%M:%S')) / 60, 1) | stats avg(mttr_minutes) as avg_mttr, count as total, count(eval(mttr_minutes>sla_limit)) as breaches by severity"
class SLATracker:
    def __init__(self, cfg_path="config/config.yaml"):
        import yaml
        with open(cfg_path) as f: self.cfg = yaml.safe_load(f)
        self.splunk = SplunkQuery(self.cfg["splunk"])
    def run_daily(self):
        data = self.splunk.search(MTTR_Q)
        _log.info(f"SLA data:   {data}")
if __name__ == "__main__": SLATracker().run_daily()
