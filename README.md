# 🚀 PulseForge

### Stellar & Soroban Infrastructure Monitoring Platform

PulseForge is an open-source monitoring and observability platform focused on
the **Stellar network and Soroban smart-contract ecosystem**.

It provides a centralized dashboard for monitoring the availability,
health, response time, operational status, and reliability of infrastructure
services used by Stellar applications.

PulseForge currently provides a general-purpose monitoring engine and is being
extended with **Stellar-specific infrastructure monitoring capabilities**.

The long-term goal is to provide Stellar developers, infrastructure
operators, application teams, and ecosystem builders with a simple way to
detect infrastructure failures, monitor network-facing services, and receive
actionable alerts.

---

# 🌟 Why PulseForge?

Modern Stellar applications depend on reliable infrastructure.

Applications may depend on services such as:

- Stellar RPC
- Horizon
- Soroban RPC infrastructure
- Stellar application APIs
- Payment services
- Wallet infrastructure
- Custom Stellar ecosystem services

When infrastructure becomes unavailable or unreliable, applications may be
unable to:

- Read network state
- Query accounts and balances
- Interact with Soroban smart contracts
- Simulate transactions
- Submit transactions
- Track ledger activity
- Process payments
- Provide reliable user experiences

PulseForge provides a monitoring layer for these services.

Instead of manually checking multiple endpoints, developers can register
services with PulseForge and continuously monitor their operational health.

---

# 🎯 Project Goals

PulseForge is being developed around four major goals:

1. **Monitor Stellar infrastructure**
2. **Detect failures quickly**
3. **Provide useful operational history**
4. **Alert developers when infrastructure problems occur**

The project starts with a reliable monitoring foundation and progressively
adds deeper Stellar and Soroban-specific capabilities.

---

# ✨ Current Features

## General Service Monitoring

PulseForge currently supports:

- Service registration
- Service listing
- Individual service lookup
- Service deletion
- Manual health checks
- Automated background health checks
- HTTP status monitoring
- Response-time measurement
- Healthy / unhealthy detection
- Health-check history
- Service history
- Failure detection
- Recovery detection

---

## 🚨 Alert System

PulseForge automatically generates alerts when monitored services change
health state.

Currently supported alert events include:

- Service DOWN
- Service RECOVERED

Alerts contain:

- Service
- Alert title
- Alert message
- Severity
- Sent status
- Creation timestamp

Example:

```text
PulseForge API is DOWN
Severity: critical