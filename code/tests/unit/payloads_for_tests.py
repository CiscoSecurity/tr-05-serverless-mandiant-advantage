EXPECTED_RESPONSE_OF_TEMPLATE = {
    "data": [
        {
            "agentDetectionInfo": {
                "accountId": "1469595929870590121",
                "accountName": "Cisco Systems",
                "agentDetectionState": "full_mode",
                "agentDomain": "CSTA",
                "agentIpV4": "10.180.10.103",
                "agentIpV6": "fe80::89f4:11e:1f2:2f60",
                "agentLastLoggedInUpn": None,
                "agentLastLoggedInUserMail": None,
                "agentLastLoggedInUserName": "dinsharm",
                "agentMitigationMode": "protect",
                "agentOsName": "Windows 10 Education",
                "agentOsRevision": "19044",
                "agentRegisteredAt": "2022-07-27T03:36:45.303172Z",
                "agentUuid": "a66b0c720aaf4a88ba4c034d347adbd5",
                "agentVersion": "22.1.2.217",
                "cloudProviders": {},
                "externalIp": "64.100.10.54",
                "groupId": "1469595930340352181",
                "groupName": "Default Group",
                "siteId": "1469595930331963572",
                "siteName": "Default site",
            },
            "agentRealtimeInfo": {
                "accountId": "1469595929870590121",
                "accountName": "Cisco Systems",
                "activeThreats": 0,
                "agentComputerName": "Hacker-1",
                "agentDecommissionedAt": None,
                "agentDomain": "CSTA",
                "agentId": "1473578157952136672",
                "agentInfected": False,
                "agentIsActive": True,
                "agentIsDecommissioned": False,
                "agentMachineType": "desktop",
                "agentMitigationMode": "protect",
                "agentNetworkStatus": "connected",
                "agentOsName": "Windows 10 Education",
                "agentOsRevision": "19044",
                "agentOsType": "windows",
                "agentUuid": "a66b0c720aaf4a88ba4c034d347adbd5",
                "agentVersion": "22.1.2.217",
                "groupId": "1469595930340352181",
                "groupName": "Default Group",
                "networkInterfaces": [
                    {
                        "id": "1473578157960525281",
                        "inet": ["10.180.10.103"],
                        "inet6": ["fe80::89f4:11e:1f2:2f60"],
                        "name": "Ethernet0",
                        "physical": "00:50:56:88:e0:52",
                    }
                ],
                "operationalState": "na",
                "rebootRequired": False,
                "scanAbortedAt": None,
                "scanFinishedAt": "2022-08-07T17:56:08.707242Z",
                "scanStartedAt": "2022-08-07T17:41:16.713594Z",
                "scanStatus": "finished",
                "siteId": "1469595930331963572",
                "siteName": "Default site",
                "storageName": None,
                "storageType": None,
                "userActionsNeeded": [],
            },
            "containerInfo": {"id": None, "image": None, "labels": None, "name": None},
            "id": "1473630109557835817",
            "indicators": [
                {
                    "category": "Evasion",
                    "description": "Detected attempt to hide tracks of a process",
                    "ids": [83],
                    "tactics": [
                        {
                            "name": "Defense Evasion",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/"
                                    "techniques/T1070/004/",
                                    "name": "T1070.004",
                                }
                            ],
                        }
                    ],
                }
            ],
            "kubernetesInfo": {
                "cluster": None,
                "controllerKind": None,
                "controllerLabels": None,
                "controllerName": None,
                "namespace": None,
                "namespaceLabels": None,
                "node": None,
                "pod": None,
                "podLabels": None,
            },
            "mitigationStatus": [
                {
                    "action": "quarantine",
                    "actionsCounters": {
                        "failed": 0,
                        "notFound": 0,
                        "pendingReboot": 0,
                        "success": 1,
                        "total": 1,
                    },
                    "agentSupportsReport": True,
                    "groupNotFound": False,
                    "lastUpdate": "2022-07-27T05:19:58.505123Z",
                    "latestReport": "/threats/mitigation-report/1473630110262478904",
                    "mitigationEndedAt": "2022-07-27T05:19:42.560000Z",
                    "mitigationStartedAt": "2022-07-27T05:19:42.560000Z",
                    "status": "success",
                },
                {
                    "action": "kill",
                    "actionsCounters": None,
                    "agentSupportsReport": True,
                    "groupNotFound": False,
                    "lastUpdate": "2022-07-27T05:19:58.464578Z",
                    "latestReport": None,
                    "mitigationEndedAt": "2022-07-27T05:19:58.458351Z",
                    "mitigationStartedAt": "2022-07-27T05:19:58.458350Z",
                    "status": "success",
                },
            ],
            "threatInfo": {
                "analystVerdict": "suspicious",
                "analystVerdictDescription": "Suspicious",
                "automaticallyResolved": False,
                "browserType": None,
                "certificateId": "",
                "classification": "Malware",
                "classificationSource": "Engine",
                "cloudFilesHashVerdict": "provider_unknown",
                "collectionId": "1473630109566224426",
                "confidenceLevel": "malicious",
                "createdAt": "2022-07-27T05:19:58.420530Z",
                "detectionEngines": [
                    {"key": "pre_execution", "title": "On-Write Static AI"}
                ],
                "detectionType": "static",
                "engines": ["On-Write DFI"],
                "externalTicketExists": False,
                "externalTicketId": None,
                "failedActions": False,
                "fileExtension": "",
                "fileExtensionType": "None",
                "filePath": "\\Device\\HarddiskVolume3\\Users\\dinsharm\\AppD"
                "ata\\Local\\Mozilla\\Firefox\\Profiles\\1r1gtoel"
                ".default-release\\cache2\\entries\\99A5AFC59CA2D"
                "59AB83B2E632DE96A8473DE113D",
                "fileSize": 9299,
                "fileVerificationType": "NotSigned",
                "identifiedAt": "2022-07-27T05:19:42.560000Z",
                "incidentStatus": "in_progress",
                "incidentStatusDescription": "In progress",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "initiatingUserId": None,
                "initiatingUsername": None,
                "isFileless": False,
                "isValidCertificate": False,
                "maliciousProcessArguments": None,
                "md5": None,
                "mitigatedPreemptively": False,
                "mitigationStatus": "mitigated",
                "mitigationStatusDescription": "Mitigated",
                "originatorProcess": "firefox.exe",
                "pendingActions": False,
                "processUser": "HACKER-1\\dinsharm",
                "publisherName": "",
                "reachedEventsLimit": False,
                "rebootRequired": False,
                "sha1": "654477f623a09fda1b04fcba854734fb20a30e11",
                "sha256": None,
                "storyline": "9F82037FFA3E2FDF",
                "threatId": "1473630109557835817",
                "threatName": "99A5AFC59CA2D59AB83B2E632DE96A8473DE113D",
                "updatedAt": "2022-07-27T15:22:10.519915Z",
            },
            "whiteningOptions": ["path", "hash"],
        }
    ],
    "pagination": {"nextCursor": None, "totalItems": 1},
}

EXPECTED_RELAY_RESPONSE = {
    "data": {
        "sightings": {
            "count": 1,
            "docs": [
                {
                    "confidence": "High",
                    "count": 1,
                    "description": "Template Detection",
                    "external_ids": ["1478943957790855909"],
                    "id": "transient:sighting-40909883-cb4c-4473-b2ca-d87553de9198",
                    "internal": True,
                    "observables": [
                        {
                            "type": "sha1",
                            "value": "654477f623a09fda1b04fcba854734fb20a30e11",
                        }
                    ],
                    "observed_time": {"start_time": "2022-08-03T13:17:38.492566Z"},
                    "relations": [
                        {
                            "origin": "Template Threat",
                            "related": {
                                "type": "sha1",
                                "value": "654477f623a09fda1b04fcba854734fb" "20a30e11",
                            },
                            "relation": "File_Path_Of",
                            "source": {
                                "type": "file_path",
                                "value": "\\Device\\HarddiskVolume1\\Users"
                                "\\Public\\LockBit.exe",
                            },
                        },
                        {
                            "origin": "Template Threat",
                            "related": {
                                "type": "sha1",
                                "value": "654477f623a09fda1b04fcba854734fb" "20a30e11",
                            },
                            "relation": "File_Name_Of",
                            "source": {"type": "file_name", "value": "LockBit.exe"},
                        },
                    ],
                    "resolution": "detected",
                    "schema_version": "1.1.12",
                    "sensor": "Endpoint",
                    "source": "Template Threat",
                    "source_uri": "https://example.com/analyze/threats/147894395779085590"
                    "9/overview",
                    "targets": [
                        {
                            "observables": [
                                {"type": "hostname", "value": "Prod-Lckbit-477"},
                                {"type": "s1_agent_id", "value": "1478942211760818649"},
                                {"type": "mac_address", "value": "00:50:56:07:64:96"},
                                {"type": "ip", "value": "10.0.0.5"},
                                {"type": "ipv6", "value": "fe80::648b:1bb9:557:f5cd"},
                            ],
                            "observed_time": {
                                "start_time": "2022-08-03T13:17:38.492566Z"
                            },
                            "os": "Windows 10 Enterprise Evaluation",
                            "type": "endpoint",
                        }
                    ],
                    "type": "sighting",
                }
            ],
        }
    }
}
