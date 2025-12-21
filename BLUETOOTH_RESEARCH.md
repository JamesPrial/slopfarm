# Aggressive Bluetooth Defensive Research Framework

**WARNING**: This framework is for authorized defensive security research only. Only test devices you own or have explicit authorization to test.

## Overview

This repository contains an aggressive Bluetooth device detection and audio stress testing framework designed for defensive security research. The system uses parallel "wave" deployment of specialized agents to comprehensively test Bluetooth security.

## Architecture

### Agent-Based Design

The framework uses the **parallel wave pattern** with specialized agents:

1. **bluetooth-scanner** - Continuous BLE/Classic Bluetooth device detection
2. **bluetooth-audio-hammer** - Audio stress testing for speaker resilience
3. **bluetooth-orchestrator** - Coordinates parallel agent deployment

### Wave Deployment Pattern

```
Wave 1: RECONNAISSANCE (Parallel)
├─ Scanner Wave 1: High-frequency BLE scan (0.5s interval)
├─ Scanner Wave 2: Medium-frequency scan (0.8s interval)
└─ Scanner Wave 3: Standard frequency scan (1.0s interval)

Wave 2: AUDIO TESTING (Parallel)
├─ Audio Hammer 1: Continuous tone generation
├─ Audio Hammer 2: Frequency sweep attacks
├─ Audio Hammer 3: Connection cycling stress
└─ Audio Hammer 4: Stream flooding

Wave 3: SUSTAINED ASSAULT
└─ All agents continue for configured duration (24h-365d)
```

## Components

### 1. BLE Scanner (`bt_scanner.py`)

Aggressively scans for Bluetooth Low Energy devices:

**Features:**
- Continuous scanning with configurable intervals
- Logs MAC addresses, device names, RSSI values
- Tracks unique device discoveries
- JSON output format for analysis
- Supports extended duration (days/weeks/months)

**Usage:**
```bash
# Single scanner (1 day, 1 second intervals)
python3 bt_scanner.py -o scan.json -d 1 -i 1.0

# Aggressive high-frequency scan (365 days, 0.5s intervals)
python3 bt_scanner.py -o aggressive_scan.json -d 365 -i 0.5

# Run in background
python3 bt_scanner.py -o scan.json -d 1 &
```

### 2. Audio Stress Tester (`bt_audio_hammer.py`)

Tests Bluetooth speaker resilience with aggressive audio patterns:

**Test Patterns:**
1. Continuous 440Hz tone (default)
2. Frequency sweeps (20Hz - 20kHz)
3. White noise barrage
4. Connection cycling
5. Stream flooding

**Usage:**
```bash
# Simulation mode (no real device)
python3 bt_audio_hammer.py -t 24

# Target specific device (24 hours)
python3 bt_audio_hammer.py -d XX:XX:XX:XX:XX:XX -t 24

# Custom frequency and duration
python3 bt_audio_hammer.py -d XX:XX:XX:XX:XX:XX -t 168 --frequency 1000
```

### 3. Agent Monitor (`monitor_agents.py`)

Real-time dashboard for monitoring all running agents:

**Features:**
- Shows active agent processes (PID, CPU, memory)
- Displays scan statistics (unique devices, total scans)
- Auto-refreshing dashboard (5s intervals)
- Log file analysis

**Usage:**
```bash
python3 monitor_agents.py
```

## Aggressive Deployment Examples

### Example 1: Full Reconnaissance Wave

Deploy 3 parallel scanners with different scan rates:

```bash
# High-frequency scanner
python3 bt_scanner.py -o wave1.json -d 1 -i 0.5 &

# Medium-frequency scanner
python3 bt_scanner.py -o wave2.json -d 1 -i 0.8 &

# Standard scanner
python3 bt_scanner.py -o wave3.json -d 1 -i 1.0 &
```

### Example 2: Audio Stress Testing

Deploy multiple audio hammers targeting different devices:

```bash
# Device 1: Continuous tone
python3 bt_audio_hammer.py -d AA:BB:CC:DD:EE:01 -t 24 &

# Device 2: Frequency sweeps
python3 bt_audio_hammer.py -d AA:BB:CC:DD:EE:02 -t 24 --frequency 2000 &

# Monitor all tests
python3 monitor_agents.py
```

### Example 3: Extended Duration Research

Run scanners for extended periods:

```bash
# 7 days of continuous scanning
python3 bt_scanner.py -o week_scan.json -d 7 -i 1.0 &

# 30 days of aggressive scanning
python3 bt_scanner.py -o month_scan.json -d 30 -i 0.5 &

# 365 days of monitoring
python3 bt_scanner.py -o year_scan.json -d 365 -i 2.0 &
```

## Installation

### System Requirements

- Python 3.8+
- Linux (for full Bluetooth access)
- Bluetooth adapter (for real hardware testing)

### Python Dependencies

```bash
# Install dependencies
pip install -r requirements.txt

# For Classic Bluetooth (Linux only):
sudo apt-get install bluetooth libbluetooth-dev
pip install pybluez

# For audio support:
sudo apt-get install ffmpeg
```

### Quick Start

```bash
# 1. Clone and setup
git clone <repo_url>
cd slopfarm

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test scanner (simulation mode)
python3 bt_scanner.py -d 0.001 -i 1.0  # Run for ~90 seconds

# 4. Deploy aggressive wave
./deploy_wave.sh  # (create this script for your needs)

# 5. Monitor
python3 monitor_agents.py
```

## Defensive Research Use Cases

### 1. Device Enumeration Detection
Test how devices respond to continuous scanning:
- Monitor RSSI signal strength variations
- Detect when devices become discoverable/hidden
- Analyze manufacturer data leakage

### 2. Connection Resilience Testing
Stress test device connection handling:
- Rapid connect/disconnect cycles
- Connection flooding from multiple sources
- Protocol state exhaustion

### 3. Audio Stream Security
Test speaker firmware robustness:
- Malformed audio streams
- Buffer overflow attempts
- Extended duration streaming (memory leaks?)

### 4. Privacy Research
Analyze tracking and fingerprinting risks:
- MAC address randomization effectiveness
- Device name information leakage
- Service UUID exposure

## Output Analysis

### Scan Log Format

Each scan produces JSON logs:

```json
{
  "timestamp": "2025-12-21T04:16:30.123456",
  "mac_address": "AA:BB:CC:DD:EE:FF",
  "name": "Device Name",
  "rssi": -65,
  "device_type": "BLE",
  "metadata": {},
  "scan_number": 1234
}
```

### Analysis Scripts

```bash
# Count unique devices
cat scan.json | jq -r '.mac_address' | sort -u | wc -l

# Find devices by name
cat scan.json | jq -r 'select(.name | contains("Speaker"))'

# RSSI analysis
cat scan.json | jq -r '.rssi' | sort -n | uniq -c
```

## Safety and Ethics

### Authorization Requirements

✅ **Authorized Use:**
- Your own devices
- Devices you own for testing
- Authorized penetration testing engagements
- CTF competitions
- Educational/defensive security research

❌ **Prohibited Use:**
- Unauthorized device attacks
- DoS attacks on public infrastructure
- Mass targeting without authorization
- Malicious interference

### Safety Controls

- All scripts support graceful shutdown (Ctrl+C)
- Simulation modes available (no real device needed)
- Clear logging of all operations
- Duration limits configurable

## Agent Definitions

Agent definition files are located in `.claude/agents/bluetooth/`:

- `scanner.md` - BLE scanner agent definition
- `audio-hammer.md` - Audio stress tester agent definition
- `orchestrator.md` - Wave deployment coordinator

These integrate with the Claude Agent SDK for automated orchestration.

## Troubleshooting

### BLE Scanning Errors

```
[!] Scan error: [Errno 2] No such file or directory
```
- Cause: No Bluetooth hardware or DBus not available
- Solution: Run on Linux system with BT adapter, or use simulation mode

### Audio Generation Warnings

```
RuntimeWarning: Couldn't find ffmpeg or avconv
```
- Cause: FFmpeg not installed
- Solution: `sudo apt-get install ffmpeg`

### Permission Errors

```
BluetoothError: Permission denied
```
- Cause: Insufficient Bluetooth permissions
- Solution: Run with `sudo` or add user to `bluetooth` group

## Future Enhancements

- [ ] Classic Bluetooth scanning (pybluez integration)
- [ ] Real Bluetooth audio streaming (A2DP)
- [ ] Connection flooding implementation
- [ ] Malformed packet generation
- [ ] Automated report generation
- [ ] Web-based monitoring dashboard
- [ ] Multi-machine distributed scanning

## License

MIT License - See LICENSE file

## Disclaimer

This framework is provided for authorized defensive security research and educational purposes only. Users are responsible for ensuring they have proper authorization before testing any devices. Unauthorized use may violate laws and regulations.

---

**Remember: Always operate within authorized scope. Defensive research requires responsibility.**
