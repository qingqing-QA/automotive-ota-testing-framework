# Automotive OTA Update Testing Framework

## Overview
This project simulates an automotive Over-the-Air (OTA) software update workflow and validates system behavior using Python and PyTest.

## Features
- Version checking before update
- Update download simulation (with network failure handling)
- Installation validation
- Post-update verification
- Rollback mechanism

## Tech Stack
- Python
- PyTest

## Test Scenarios
- Successful OTA update
- No update needed (same version)
- Network failure during download
- Installation without download
- Rollback after update

## How to Run
```bash
python -m pytest