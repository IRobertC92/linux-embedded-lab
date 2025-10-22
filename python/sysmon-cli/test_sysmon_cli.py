import pytest
from unittest.mock import patch, MagicMock
from sysmon_cli import (
calculate_health,
trend_symbol,
get_stats,
SystemStats,
)

#=====================================================
#Basic Function Tests
#=====================================================

def test_calculate_health_normal_ranges():
    """Health score should decrease with higher usage."""
    h_low = calculate_health(10, 10, 10)
    h_high = calculate_health(90, 90, 90)
    assert h_low > h_high
    assert 0 <= h_low <= 100
    assert 0 <= h_high <= 100

def test_calculate_health_edge_cases():
    """Health should stay within 0–100 regardless of inputs."""
    assert calculate_health(-10, 0, 0) == 100
    assert calculate_health(1000, 1000, 1000) == 0

def test_trend_symbol_neutral():
    """When difference < 0.5, should show yellow arrow."""
    symbol = trend_symbol(50, 50.3)
    assert "→" in symbol

def test_trend_symbol_positive_bad():
    """For metrics where positive is bad, ↑ = red."""
    symbol = trend_symbol(80, 70)
    assert "[red]" in symbol

def test_trend_symbol_positive_good():
    """For metrics where positive is good, ↑ = green."""
    symbol = trend_symbol(80, 70, positive_is_good=True)
    assert "[green]" in symbol

#=====================================================
#psutil Mock Tests
#=====================================================

@patch("sysmon_cli.psutil.cpu_percent", return_value=42)
@patch("sysmon_cli.psutil.virtual_memory")
@patch("sysmon_cli.psutil.disk_usage")
@patch("sysmon_cli.psutil.net_io_counters")

def test_get_stats_basic(mock_net, mock_disk, mock_mem, mock_cpu):
    """Verify get_stats() collects and returns mocked data correctly."""
    mock_mem.return_value.percent = 55
    mock_disk.return_value.percent = 65
    mock_net.return_value.bytes_sent = 102400
    mock_net.return_value.bytes_recv = 204800

    stats = get_stats(per_core=False)
    assert isinstance(stats, SystemStats)
    assert stats.cpu == 42
    assert stats.mem == 55
    assert stats.disk == 65
    assert stats.net_sent > 0
    assert stats.net_recv > 0
    assert stats.per_core is None

@patch("sysmon_cli.psutil.cpu_percent", side_effect=[50, [20, 30, 40]])
@patch("sysmon_cli.psutil.virtual_memory")
@patch("sysmon_cli.psutil.disk_usage")
@patch("sysmon_cli.psutil.net_io_counters")

def test_get_stats_per_core(mock_net, mock_disk, mock_mem, mock_cpu):
    """Ensure per-core stats list is populated when enabled."""
    mock_mem.return_value.percent = 50
    mock_disk.return_value.percent = 60
    mock_net.return_value.bytes_sent = 51200
    mock_net.return_value.bytes_recv = 25600

    stats = get_stats(per_core=True)
    assert isinstance(stats.per_core, list)
    assert all(isinstance(x, (int, float)) for x in stats.per_core)

#=====================================================
#Health + Stats Integration
#=====================================================

def test_health_consistency_with_stats():
    """Verify that calculated health makes logical sense."""
    fake_stats = SystemStats(cpu=50, mem=50, disk=50, net_sent=1000, net_recv=2000)
    health = calculate_health(fake_stats.cpu, fake_stats.mem, fake_stats.disk)
    assert 0 <= health <= 100