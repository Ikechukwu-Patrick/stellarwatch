cat > README.md <<'EOF'
# 🌟 StellarWatch

### Open-Source Stellar Network Health Monitoring & Observability Platform

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/Ikechukwu-Patrick/stellarwatch)
[![Python](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

StellarWatch is an open-source monitoring and observability platform focused on the **Stellar network and Soroban ecosystem**.

It continuously monitors Stellar network health, tracks ledger state, measures response time, stores historical health data, and exposes monitoring information through a REST API.

> **Mission:** Make Stellar infrastructure health visible, measurable, and easier to operate.

---

## 🚀 Why StellarWatch?

Stellar applications depend on reliable network infrastructure.

When infrastructure becomes slow, unavailable, or falls behind the network, applications can experience:

- Failed or delayed transactions
- Slow account and balance queries
- Stale network information
- Poor application performance
- Difficult-to-diagnose infrastructure failures
- Reduced reliability for payment applications

StellarWatch provides an observability layer for these problems.

Instead of manually checking network infrastructure, developers and infrastructure operators can continuously monitor Stellar health and review historical performance.

---

## 🎯 Project Goals

StellarWatch is being developed around four core goals:

1. **Monitor Stellar network health**
2. **Detect infrastructure problems quickly**
3. **Provide historical network-health data**
4. **Make Stellar infrastructure observability simple and accessible**

The current implementation establishes the core monitoring foundation. Future iterations will expand this foundation into broader Stellar and Soroban infrastructure observability.

---

# ✨ Current Features

## 🌐 Stellar Network Monitoring

StellarWatch currently provides:

- Stellar network health checks
- Latest ledger monitoring
- Oldest ledger monitoring
- Ledger retention monitoring
- Network response-time measurement
- Healthy/unhealthy status detection
- Periodic background monitoring
- Historical health records
- REST API endpoints

A live health check returns data such as:

```json
{
  "status": "healthy",
  "latest_ledger": 4118963,
  "oldest_ledger": 3998004,
  "ledger_retention_window": 120960,
  "response_time_ms": 889.08
}