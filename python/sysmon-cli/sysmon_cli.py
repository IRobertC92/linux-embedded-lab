#!/usr/bin/env python3
# =======================================================================================================================================================================
#  File        : sysmon_cli.py
#  Author      : Ionescu Robert-Constantin
#  Date        : 2025-10-21
#  Version     : 1.0
#  Description : Linux System Monitor CLI - displays CPU, memory, disk usage, calculates a health Score (0-100), optional csv logging for trend analysis.
# =======================================================================================================================================================================
#  Usage       : python3 sysmon_cli.py
# =======================================================================================================================================================================

import psutil
import time
import argparse
import csv
import json
from dataclasses import dataclass
from datetime import datetime
from rich.console import Console
from rich.table import Table

# =======================================================================================================================================================================
# TO DO SECTION / Requirements
# ======================================================================================================================================================================= 
# TODO - STEP1 - Gather system metrics: 
#                   - CPU usage (overall and optionally per-core)
#                   - Memory usage
#                   - Disk usage
#                   - Network bytes sent/received
# TODO - STEP2 - Calculate Health Score (0-100):
#                   - Weighted calculation: CPU 40%, Memory 40%, Disk 20%
#                   - Ensure score is capped between 0 and 100
# TODO - STEP3 - Display system stats in CLI:
#                   - Use rich.Table for a clean table display
#                   - Color-code usage values and health score:
#                       - Red if thresholds exceeded (CPU>80%, Memory>80%, Disk>90%)
#                       - Yellow for warning ranges
#                       - Green for normal
#                   - Include trend indicators (↑, ↓, →) for each metric
# TODO - STEP4 - Optional Features:
#                   - CSV logging for trend analysis
#                   - Include timestamp, metrics, health score
#                   - JSON output option
#                   - Per-core CPU display option
# TODO - STEP5 - Command-line Arguments:
#                   - --interval : refresh interval in seconds
#                   - --log : enable CSV logging
#                   - --logfile : CSV log file path
#                   - --max-iterations : stop after N updates
#                   - --max-runtime : stop after N seconds
#                   - --json : output JSON instead of table
#                   - --per-core : show per-core CPU usage
#
# TODO - STEP6 - Program Flow:
#                   - Initialize console and optional CSV file
#                   - Initialize psutil CPU percent for per-core if needed
#                   - Loop:
#                       - Retrieve stats
#                       - Calculate health
#                       - Display table or JSON
#                       - Log stats if enabled
#                       - Sleep until next interval
#                   - Stop conditions: max iterations or max runtime
#                   - Handle KeyboardInterrupt to exit gracefully

# =======================================================================================================================================================================
# Constants / Configuration / Data Structures
# ======================================================================================================================================================================= 

@dataclass
class SystemStats:
    cpu: float
    mem: float
    disk: float
    net_sent: int
    net_recv: int
    per_core: list = None

# =======================================================================================================================================================================
# Helper Functions
# =======================================================================================================================================================================

# Function to retrieve current system stats
def get_stats(per_core=False):
    try:
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net = psutil.net_io_counters()
        cores = psutil.cpu_percent(interval=None, percpu=True) if per_core else None
        return SystemStats(cpu, mem, disk, net.bytes_sent // 1024, net.bytes_recv // 1024, cores)
    except Exception as e:
        console.print(f"[red]Error getting system stats: {e}[/red]")
        return SystemStats(0, 0, 0, 0, 0)

# Function to calculate a simple health score (0–100)
def calculate_health(cpu, mem, disk):
    health = 100 - (cpu * 0.4 + mem * 0.4 + disk * 0.2)
    return max(0, min(100, health))

# Function to return a colored arrow showing trend
def trend_symbol(current, previous, positive_is_good=False):
    """
    - positive_is_good=False: ↑ = worse, ↓ = better (for CPU, mem, disk)
    - positive_is_good=True : ↑ = better, ↓ = worse (for Health)
    """
    if previous is None:
        return "→"
    diff = current - previous
    if abs(diff) < 0.5:
        return "[yellow]→[/yellow]"
    if positive_is_good:
        return "[green]↑[/green]" if diff > 0 else "[red]↓[/red]"
    else:
        return "[red]↑[/red]" if diff > 0 else "[green]↓[/green]"

# Function to display system stats with rich table and trend indicators
def display(stats: SystemStats, health, prev_stats=None, prev_health=None, per_core=False):
    table = Table(title="Linux System Monitor", show_lines=True)
    table.add_column("Resource", style="cyan", no_wrap=True)
    table.add_column("Usage", style="magenta", justify="right")

    # Trends
    cpu_trend = trend_symbol(stats.cpu, getattr(prev_stats, 'cpu', None))
    mem_trend = trend_symbol(stats.mem, getattr(prev_stats, 'mem', None))
    disk_trend = trend_symbol(stats.disk, getattr(prev_stats, 'disk', None))
    health_trend = trend_symbol(health, prev_health, positive_is_good=True)

    table.add_row("CPU (%)", f"{color(stats.cpu, 80)} {cpu_trend}")
    table.add_row("Memory (%)", f"{color(stats.mem, 80)} {mem_trend}")
    table.add_row("Disk (%)", f"{color(stats.disk, 90)} {disk_trend}")

    # Health color
    if health > 70:
        health_str = f"[green]{health:.1f}[/green]"
    elif health > 40:
        health_str = f"[yellow]{health:.1f}[/yellow]"
    else:
        health_str = f"[red]{health:.1f}[/red]"
    table.add_row("Health Score", f"{health_str} {health_trend}")

    # Network info
    table.add_row("Net Sent (KB)", str(stats.net_sent))
    table.add_row("Net Recv (KB)", str(stats.net_recv))

    # Per-core CPU usage
    if per_core and stats.per_core:
        for i, val in enumerate(stats.per_core):
            table.add_row(f"Core {i}", color(val, 80))

    console.clear()
    console.print(table)

# Function to display health score coloring
def color(value, limit):
    return f"[red]{value}[/red]" if value > limit else str(value)

# Function to append stats to CSV, creating headers if needed
def log_stats(file_path, stats: SystemStats, health):
    header = ["timestamp", "cpu", "mem", "disk", "health", "net_sent", "net_recv"]
    file_exists = False
    try:
        file_exists = open(file_path).readable()
    except FileNotFoundError:
        pass
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists or f.tell() == 0:
                writer.writerow(header)
                writer.writerow([datetime.now(), stats.cpu, stats.mem, stats.disk, health, stats.net_sent, stats.net_recv])

# Function to print system stats in JSON format (with trends)
def output_json(stats: SystemStats, health, prev_stats=None, prev_health=None):
    json_obj = {
        "timestamp": datetime.now().isoformat(),
        "cpu": stats.cpu,
        "mem": stats.mem,
        "disk": stats.disk,
        "health": health,
        "net_sent_kb": stats.net_sent,
        "net_recv_kb": stats.net_recv,
    }

    # Trends
    trends = {}
    if prev_stats:
        trends["cpu"] = stats.cpu - prev_stats.cpu
        trends["mem"] = stats.mem - prev_stats.mem
        trends["disk"] = stats.disk - prev_stats.disk
    if prev_health is not None:
        trends["health"] = health - prev_health

    if trends:
        json_obj["trends"] = trends

    print(json.dumps(json_obj, indent=2))

# =======================================================================================================================================================================
# Main function / Control loop
# =======================================================================================================================================================================

def main(interval=2, log=False, logfile="system_log.csv", max_iterations=None, max_runtime=None, json_output=False, per_core=False):
    console.print("[bold blue]Starting Linux System Monitor CLI[/bold blue]")
    if log:
        console.print(f"[bold green]Logging enabled:[/bold green] {logfile}")

    psutil.cpu_percent(interval=None)  # initialize non-blocking measurement
    start_time = time.time()
    iteration = 0
    next_time = start_time
    prev_stats = None
    prev_health = None

    while True:
        stats = get_stats(per_core=per_core)
        health = calculate_health(stats.cpu, stats.mem, stats.disk)

        if json_output:
            output_json(stats, health, prev_stats, prev_health)
        else:
            display(stats, health, prev_stats, prev_health, per_core)

        if log:
            log_stats(logfile, stats, health)

        prev_stats, prev_health = stats, health
        iteration += 1
        elapsed = time.time() - start_time

        if max_iterations and iteration >= max_iterations:
            console.print("[bold yellow]Max iterations reached. Stopping monitor.[/bold yellow]")
            break
        if max_runtime and elapsed >= max_runtime:
            console.print("[bold yellow]Max runtime reached. Stopping monitor.[/bold yellow]")
            break

        next_time += interval
        sleep_time = next_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

# =======================================================================================================================================================================
# Script Entry / Code Section
# =======================================================================================================================================================================

console = Console()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux System Monitor CLI (with full trend indicators)")
    parser.add_argument('--interval', type=float, default=2, help='Update interval in seconds')
    parser.add_argument('--log', action='store_true', help='Enable CSV logging')
    parser.add_argument('--logfile', type=str, default="system_log.csv", help='CSV log file path')
    parser.add_argument('--max-iterations', type=int, default=None, help='Stop after this many updates')
    parser.add_argument('--max-runtime', type=int, default=None, help='Stop after this many seconds')
    parser.add_argument('--json', action='store_true', help='Output in JSON format instead of table')
    parser.add_argument('--per-core', action='store_true', help='Show per-core CPU usage')
    args = parser.parse_args()

    try:
        main(
            interval=args.interval,
            log=args.log,
            logfile=args.logfile,
            max_iterations=args.max_iterations,
            max_runtime=args.max_runtime,
            json_output=args.json,
            per_core=args.per_core
        )
    except KeyboardInterrupt:
        console.print("\n[bold red]Monitor stopped by user[/bold red]")