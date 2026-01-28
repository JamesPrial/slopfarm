#!/usr/bin/env python3
"""
Aggressive Bluetooth Device Scanner for Defensive Security Research
Continuously scans for BLE and Classic Bluetooth devices
"""
import asyncio
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Set
import argparse

try:
    from bleak import BleakScanner
    BLEAK_AVAILABLE = True
except ImportError:
    BLEAK_AVAILABLE = False
    print("Warning: bleak not installed. BLE scanning disabled.", file=sys.stderr)


class AggressiveBTScanner:
    """Aggressive Bluetooth scanner for defensive research"""

    def __init__(self, output_file: str = "bt_scan.json", duration_days: int = 1, scan_interval: float = 1.0):
        self.output_file = Path(output_file)
        self.duration = timedelta(days=duration_days)
        self.scan_interval = scan_interval
        self.discovered_devices: Set[str] = set()
        self.scan_count = 0
        self.start_time = datetime.now()

    async def scan_ble_devices(self):
        """Continuously scan for BLE devices"""
        if not BLEAK_AVAILABLE:
            print("BLE scanning unavailable - install bleak: pip install bleak")
            return

        print(f"[*] Starting aggressive BLE scanner (Duration: {self.duration})")
        print(f"[*] Logging to: {self.output_file}")

        end_time = self.start_time + self.duration

        while datetime.now() < end_time:
            try:
                self.scan_count += 1
                devices = await BleakScanner.discover(timeout=self.scan_interval)

                for device in devices:
                    device_data = {
                        "timestamp": datetime.now().isoformat(),
                        "mac_address": device.address,
                        "name": device.name or "Unknown",
                        "rssi": device.rssi,
                        "device_type": "BLE",
                        "metadata": device.metadata,
                        "scan_number": self.scan_count
                    }

                    # Log new devices
                    if device.address not in self.discovered_devices:
                        self.discovered_devices.add(device.address)
                        print(f"[+] NEW DEVICE: {device.address} ({device.name}) RSSI: {device.rssi}")

                    # Write to log file
                    with open(self.output_file, 'a') as f:
                        f.write(json.dumps(device_data) + "\n")

                # Status update
                if self.scan_count % 100 == 0:
                    elapsed = datetime.now() - self.start_time
                    remaining = end_time - datetime.now()
                    print(f"[*] Scan #{self.scan_count} | Devices: {len(self.discovered_devices)} | "
                          f"Elapsed: {elapsed} | Remaining: {remaining}")

                await asyncio.sleep(0.1)  # Brief pause between scans

            except Exception as e:
                print(f"[!] Scan error: {e}", file=sys.stderr)
                await asyncio.sleep(1)

        print(f"\n[*] Scanning complete!")
        print(f"[*] Total scans: {self.scan_count}")
        print(f"[*] Unique devices discovered: {len(self.discovered_devices)}")

    def scan_classic_bt(self):
        """Scan for Classic Bluetooth devices (requires pybluez)"""
        try:
            import bluetooth
            print("[*] Classic Bluetooth scanning not yet implemented")
            print("[*] Install pybluez: sudo apt-get install bluetooth libbluetooth-dev && pip install pybluez")
        except ImportError:
            print("[!] pybluez not available for Classic Bluetooth scanning")


async def main():
    parser = argparse.ArgumentParser(description='Aggressive Bluetooth Scanner for Defensive Research')
    parser.add_argument('-o', '--output', default='bt_scan.json', help='Output JSON file')
    parser.add_argument('-d', '--days', type=int, default=1, help='Duration in days (default: 1)')
    parser.add_argument('-i', '--interval', type=float, default=1.0, help='Scan interval in seconds')
    args = parser.parse_args()

    scanner = AggressiveBTScanner(
        output_file=args.output,
        duration_days=args.days,
        scan_interval=args.interval
    )

    await scanner.scan_ble_devices()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(0)
