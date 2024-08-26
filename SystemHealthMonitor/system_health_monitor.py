import psutil
import platform
import time

def get_system_info():
    """Get basic system information."""
    uname = platform.uname()
    return {
        "System": uname.system,
        "Node Name": uname.node,
        "Release": uname.release,
        "Version": uname.version,
        "Machine": uname.machine,
        "Processor": uname.processor
    }

def get_cpu_usage():
    """Get CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Get memory usage statistics."""
    memory = psutil.virtual_memory()
    return {
        "Total Memory": memory.total / (1024 ** 3),  # Convert bytes to GB
        "Available Memory": memory.available / (1024 ** 3),
        "Used Memory": memory.used / (1024 ** 3),
        "Memory Usage": memory.percent
    }

def get_disk_usage():
    """Get disk usage statistics."""
    disk = psutil.disk_usage('/')
    return {
        "Total Disk Space": disk.total / (1024 ** 3),
        "Used Disk Space": disk.used / (1024 ** 3),
        "Free Disk Space": disk.free / (1024 ** 3),
        "Disk Usage": disk.percent
    }

def get_network_bandwidth():
    """Get network bandwidth statistics."""
    net = psutil.net_io_counters()
    return {
        "Bytes Sent": net.bytes_sent / (1024 ** 2),  # Convert bytes to MB
        "Bytes Received": net.bytes_recv / (1024 ** 2),
        "Packets Sent": net.packets_sent,
        "Packets Received": net.packets_recv
    }

def get_temperature_info():
    """Get temperature information (if available)."""
    if hasattr(psutil, 'sensors_temperatures'):
        temperatures = psutil.sensors_temperatures()
        return {k: [temp.current for temp in v] for k, v in temperatures.items()}
    else:
        return "Temperature monitoring not supported."

def print_report():
    """Print a report of the system health."""
    print("System Information:")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    print("\nCPU Usage:")
    print(f"CPU Usage: {get_cpu_usage()}%")

    print("\nMemory Usage:")
    memory = get_memory_usage()
    for key, value in memory.items():
        print(f"{key}: {value:.2f} GB" if 'Memory' in key else f"{key}: {value}%")

    print("\nDisk Usage:")
    disk = get_disk_usage()
    for key, value in disk.items():
        print(f"{key}: {value:.2f} GB" if 'Disk' in key else f"{key}: {value}%")

    print("\nNetwork Bandwidth:")
    net = get_network_bandwidth()
    for key, value in net.items():
        print(f"{key}: {value:.2f} MB")

    print("\nTemperature Information:")
    temp_info = get_temperature_info()
    if isinstance(temp_info, dict):
        for sensor, temps in temp_info.items():
            print(f"{sensor}: {', '.join(map(str, temps))}°C")
    else:
        print(temp_info)

if __name__ == "__main__":
    while True:
        print_report()
        time.sleep(60)  # Refresh every 60 seconds
