#!/usr/bin/env python3
"""
Aggressive Bluetooth Agent Monitoring Dashboard
Monitors all running scanner and audio hammer agents
"""
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path


def get_running_agents():
    """Get all running Bluetooth agent processes"""
    try:
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True
        )

        lines = [line for line in result.stdout.split('\n')
                if 'bt_scanner' in line or 'bt_audio' in line]
        lines = [line for line in lines if 'grep' not in line]

        return lines
    except Exception as e:
        return []


def read_scan_logs():
    """Read all scan log files"""
    log_files = list(Path('.').glob('*_scan*.json'))

    stats = {}
    for log_file in log_files:
        try:
            devices = set()
            scan_count = 0

            with open(log_file, 'r') as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        devices.add(data.get('mac_address'))
                        scan_count = data.get('scan_number', scan_count)

            stats[log_file.name] = {
                'unique_devices': len(devices),
                'total_scans': scan_count,
                'file_size': log_file.stat().st_size
            }
        except Exception as e:
            stats[log_file.name] = {'error': str(e)}

    return stats


def display_dashboard():
    """Display live monitoring dashboard"""
    print("\n" + "="*70)
    print("AGGRESSIVE BLUETOOTH RESEARCH - AGENT MONITORING DASHBOARD")
    print("="*70)
    print(f"Timestamp: {datetime.now()}")
    print()

    # Running agents
    agents = get_running_agents()
    print(f"🔥 ACTIVE AGENTS: {len(agents)}")
    print("-"*70)
    for i, agent in enumerate(agents, 1):
        parts = agent.split()
        if len(parts) > 10:
            print(f"{i}. PID:{parts[1]} CPU:{parts[2]}% MEM:{parts[3]}% CMD:{' '.join(parts[10:])}")

    print()

    # Scan statistics
    stats = read_scan_logs()
    if stats:
        print("📊 SCAN STATISTICS:")
        print("-"*70)
        for log_name, data in stats.items():
            if 'error' not in data:
                print(f"{log_name}:")
                print(f"  ├─ Unique Devices: {data['unique_devices']}")
                print(f"  ├─ Total Scans: {data['total_scans']}")
                print(f"  └─ Log Size: {data['file_size']:,} bytes")
            else:
                print(f"{log_name}: {data['error']}")

    print()
    print("="*70)
    print("Press Ctrl+C to exit monitoring")
    print("="*70)


def main():
    """Main monitoring loop"""
    try:
        while True:
            display_dashboard()
            time.sleep(5)
            print("\n" * 2)
    except KeyboardInterrupt:
        print("\n\n[*] Monitoring stopped")


if __name__ == "__main__":
    main()
