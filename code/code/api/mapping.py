from uuid import uuid4

from flask import current_app

CONFIDENCE = "High"
SIGHTING = "sighting"
SOURCE = "Template Threat"
CTIM_DEFAUTLS = {"schema_version": "1.1.12"}

RESOLUTION = {
    "marked_as_benign": "allowed",
    "not_mitigated": "detected",
    "mitigated": "contained",
}

SIGHTING_DEFAULTS = {
    "count": 1,
    "internal": True,
    "confidence": CONFIDENCE,
    "type": SIGHTING,
    "source": SOURCE,
    "sensor": "Endpoint",
    "description": "Template Detection",
    **CTIM_DEFAUTLS,
}


class Sighting:
    def __init__(self, observable):
        self.observable = observable

    @staticmethod
    def _observed_time(threat):
        return {"start_time": threat["threatInfo"]["createdAt"]}

    def _relations(self, threat_info):
        return [
            {
                "origin": SOURCE,
                "related": self.observable,
                "relation": "File_Path_Of",
                "source": {
                    "type": "file_path",
                    "value": threat_info["filePath"],
                },
            },
            {
                "origin": SOURCE,
                "related": self.observable,
                "relation": "File_Name_Of",
                "source": {
                    "type": "file_name",
                    "value": threat_info["threatName"],
                },
            },
        ]

    @staticmethod
    def _target_observables(realtime_agent_info):
        observables = [
            {
                "type": "hostname",
                "value": realtime_agent_info.get("agentComputerName"),
            },
            {
                "type": "s1_agent_id",
                "value": realtime_agent_info.get("agentId"),
            },
        ]

        for interface in realtime_agent_info.get("networkInterfaces", []):
            observables.append(
                {"type": "mac_address", "value": interface.get("physical")}
            )
            observables.extend(
                {"value": ip, "type": "ip"} for ip in interface.get("inet", [])
            )
            observables.extend(
                {"value": ipv6, "type": "ipv6"}
                for ipv6 in interface.get("inet6", [])
            )
        return observables

    @staticmethod
    def _source_uri(threat):
        return (
            f'https://{current_app.config["HOST"]}/analyze'
            f'/threats/{threat["id"]}/overview'
        )

    def _targets(self, threat):
        return {
            "os": threat["agentRealtimeInfo"]["agentOsName"],
            "observed_time": self._observed_time(threat),
            "type": "endpoint",
            "observables": self._target_observables(
                threat["agentRealtimeInfo"]
            ),
        }

    def extract(self, threat):
        return {
            "id": f"transient:{SIGHTING}-{uuid4()}",
            "observed_time": self._observed_time(threat),
            "external_ids": [threat["id"]],
            "observables": [self.observable],
            "relations": self._relations(threat["threatInfo"]),
            "resolution": RESOLUTION[threat["threatInfo"]["mitigationStatus"]],
            "source_uri": self._source_uri(threat),
            "targets": [self._targets(threat)],
            **SIGHTING_DEFAULTS,
        }
