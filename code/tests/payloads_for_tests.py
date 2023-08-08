EXPECTED_RESPONSE_OF_JWKS_ENDPOINT = {
    "keys": [
        {
            "kty": "RSA",
            "n": "tSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V"
            "mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H"
            "vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17"
            "_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB"
            "Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7"
            "33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke"
            "Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2"
            "Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8"
            "uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M"
            "loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU"
            "jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM"
            "-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35"
            "YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR"
            "k3jNdVM",
            "e": "AQAB",
            "alg": "RS256",
            "kid": "02B1174234C29F8EFB69911438F597FF3FFEE6B7",
            "use": "sig",
        }
    ]
}

RESPONSE_OF_JWKS_ENDPOINT_WITH_WRONG_KEY = {
    "keys": [
        {
            "kty": "RSA",
            "n": "pSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V"
            "mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H"
            "vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17"
            "_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB"
            "Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7"
            "33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke"
            "Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2"
            "Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8"
            "uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M"
            "loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU"
            "jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM"
            "-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35"
            "YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR"
            "k3jNdVM",
            "e": "AQAB",
            "alg": "RS256",
            "kid": "02B1174234C29F8EFB69911438F597FF3FFEE6B7",
            "use": "sig",
        }
    ]
}

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

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
