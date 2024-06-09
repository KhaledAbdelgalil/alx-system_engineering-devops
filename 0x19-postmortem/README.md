# PharmaCheck Drug Checker App - Outage Postmortem


<p align="center">
  <img src="https://www.turntrading.com/wp-content/uploads/2017/05/fx-%E5%A4%B1%E6%95%97-6.jpg" width="350" title="hover text">
</p>
## Issue Summary
**Duration**: June 4, 2024, 13:00 - 15:30 UTC (2 hours 30 minutes)

**Impact**:
- PharmaCheck’s main service was unavailable, affecting 85% of users.
- Users encountered 503 Service Unavailable errors while trying to use the app.
- Around 50,000 users were impacted during the downtime.

**Root Cause**: A misconfigured load balancer after a routine maintenance update led to incorrect traffic routing.

## Timeline
- **13:00 UTC**: Automated monitoring detected the issue and alerted on-call engineers.
- **13:05 UTC**: On-call engineer verified the outage and started investigating.
- **13:15 UTC**: Suspected recent deployment as the cause; began rollback.
- **13:30 UTC**: Rollback finished, but the issue persisted; suspected database performance issues.
- **14:00 UTC**: Database team escalated; found no issues with database performance.
- **14:15 UTC**: Network team joined the investigation; started detailed network log analysis.
- **14:45 UTC**: Identified the root cause as a misconfigured load balancer from the recent update.
- **15:00 UTC**: Corrected and deployed the updated load balancer configuration.
- **15:30 UTC**: Service fully restored; monitoring confirmed normal operations.

## Root Cause and Resolution
**Root Cause**: A routine maintenance update introduced a misconfiguration in the load balancer, directing all traffic to a single, non-functional backend server, causing 503 errors for most users.

**Resolution**: Once the misconfiguration was identified, the network team corrected the load balancer settings to distribute traffic across all functional backend servers. Configuration tests ensured correctness, followed by a gradual return to normal traffic. Full traffic was restored once stability was confirmed.

## Corrective and Preventative Measures

**Improvements**:
- **Configuration Management**: Enhance procedures for updating and verifying changes to critical infrastructure components.
- **Monitoring and Alerts**: Improve monitoring to detect misconfigurations in load balancers and other critical services.
- **Documentation and Training**: Ensure thorough documentation and regular training on maintenance procedures and incident response.

**Tasks**:
1. **Patch Load Balancer Configuration**: Implement a patch to prevent similar misconfigurations in future updates.
2. **Add Monitoring on Load Balancer Traffic**: Deploy tools to monitor traffic patterns and alert on anomalies.
3. **Automated Configuration Validation**: Develop scripts to automatically validate load balancer configurations before deployment.
4. **Incident Response Review**: Review the incident response process to identify and address gaps.
5. **Training Session**: Schedule mandatory training for the operations team on new procedures and tools.
6. **Documentation Update**: Update all relevant documentation to reflect new procedures and configurations.
7. **Load Balancer Redundancy Check**: Ensure redundancy and failover mechanisms are correctly configured and regularly tested.

By implementing these measures, PharmaCheck aims to prevent similar incidents in the future and enhance overall system resilience and reliability.
