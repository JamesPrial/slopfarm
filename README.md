# slopfarm

## Aggressive Bluetooth Defensive Research Framework

A comprehensive framework for Bluetooth security research using parallel agent deployment and wave-based attack patterns.

### Quick Start

```bash
# Deploy aggressive scanner wave
python3 bt_scanner.py -o scan.json -d 1 -i 0.5 &

# Deploy audio stress tester
python3 bt_audio_hammer.py -t 24

# Monitor all agents
python3 monitor_agents.py
```

### Features

- 🔥 **Parallel Wave Deployment** - Launch multiple agents simultaneously
- 📡 **Aggressive BLE Scanning** - Continuous device detection (configurable 24h-365d)
- 🔊 **Audio Stress Testing** - Test speaker resilience with tone/sweep/noise patterns
- 📊 **Real-time Monitoring** - Dashboard for tracking all active agents

### Documentation

See [BLUETOOTH_RESEARCH.md](./BLUETOOTH_RESEARCH.md) for complete documentation.

### Components

- `bt_scanner.py` - Aggressive Bluetooth device scanner
- `bt_audio_hammer.py` - Audio stress testing tool
- `monitor_agents.py` - Real-time agent monitoring dashboard
- `.claude/agents/bluetooth/` - Agent definitions for Claude Agent SDK

### Safety Notice

⚠️ **For authorized defensive security research only.** Only test devices you own or have explicit permission to test.
