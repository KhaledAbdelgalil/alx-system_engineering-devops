# PharmaCheck Drug Checker App - Outage Postmortem

## Issue Summary
**Duration**: June 4, 2024, 13:00 - 15:30 UTC (2 hours 30 minutes)

**Impact**:
- PharmaCheck’s main service was down, affecting 85% of users.
- Users received 503 Service Unavailable errors when attempting to access the app.
- Approximately 50,000 users were impacted during the outage.

**Root Cause**: A misconfiguration in the load balancer following a routine maintenance update led to improper traffic routing.

## Timeline
- **13:00 UTC**: Automated monitoring system detected the issue and alerted on-call engineers.
- **13:05 UTC**: On-call engineer confirmed the outage and began investigating.
- **13:15 UTC**: Suspected the recent deployment caused the issue; initiated rollback.
- **13:30 UTC**: Rollback completed, but the issue persisted; suspected database performance issues.
- **14:00 UTC**: Database team escalated; found no anomalies in database performance.
- **14:15 UTC**: Network team joined the investigation; began detailed network log analysis.
- **14:45 UTC**: Identified the root cause as a misconfigured load balancer from the recent update.
- **15:00 UTC**: Corrected and deployed the load balancer configuration.
- **15:30 UTC**: Service fully restored; monitoring confirmed normal operation.

## Root Cause and Resolution
**Root Cause**: During routine maintenance, a misconfiguration was introduced into the load balancer, causing it to direct all traffic to a single, non-functional backend server, resulting in 503 errors for most users.

**Resolution**: Upon identifying the misconfiguration, the network team corrected the load balancer settings to distribute traffic across all functional backend servers. Configuration tests were conducted to ensure correctness, followed by a gradual traffic shift back to normal. Full traffic was restored once stability was confirmed.

## Corrective and Preventative Measures

**Improvements**:
- **Configuration Management**: Improve procedures for updating and verifying changes to critical infrastructure components.
- **Monitoring and Alerts**: Enhance monitoring to detect misconfigurations in load balancers and other critical services.
- **Documentation and Training**: Ensure comprehensive documentation and regular training on maintenance procedures and incident response.

**Tasks**:
1. **Patch Load Balancer Configuration**: Implement a patch to prevent similar misconfigurations in future updates.
2. **Add Monitoring on Load Balancer Traffic**: Deploy tools to monitor traffic patterns and alert on anomalies.
3. **Automated Configuration Validation**: Develop scripts to automatically validate load balancer configurations before deployment.
4. **Incident Response Review**: Review the incident response process to identify and address gaps.
5. **Training Session**: Schedule mandatory training for the operations team on new procedures and tools.
6. **Documentation Update**: Update all relevant documentation to reflect new procedures and configurations.
7. **Load Balancer Redundancy Check**: Ensure redundancy and failover mechanisms are correctly configured and tested regularly.

By implementing these measures, PharmaCheck aims to prevent similar incidents in the future and improve overall system resilience and reliability.

