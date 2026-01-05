# UiPath Remediation Bot - Workflow Specification

## Process Overview
**Bot ID:** BOT-404
**Trigger:** API Call from Microsoft Copilot Studio
**Goal:** Log defect incidents in SharePoint and alert the production supervisor.

## Logic Flow (Pseudo-Code)

1. **INITIALIZATION**
   - Get Credential "SharePoint_Auth" from Orchestrator Assets.
   - Read Input Arguments: `DefectRate` (Float), `IncidentID` (String).

2. **DECISION LOGIC**
   - IF `DefectRate` > 2.0%:
     - STATUS = "Critical"
     - PRIORITY = "High"
   - ELSE:
     - STATUS = "Warning"
     - PRIORITY = "Medium"

3. **ACTION: SHAREPOINT**
   - Use `Office365.SharePoint.ListItems.Add`:
     - List Name: "Quality_Incidents"
     - Title: "Incident {IncidentID}"
     - Description: "Defect rate spike detected: {DefectRate}%"
     - Priority: {PRIORITY}

4. **ACTION: NOTIFICATION**
   - Send SMTP Mail to `supervisor@factory.com`.
   - Subject: "URGENT: Quality Threshold Breached".

5. **TERMINATION**
   - Return Output Argument: `JobStatus` = "Success".