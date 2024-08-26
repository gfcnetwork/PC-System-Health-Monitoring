Explanation
get_system_info: Retrieves basic system information using the platform library.
get_cpu_usage: Gets the current CPU usage percentage.
get_memory_usage: Provides details about total, available, and used memory.
get_disk_usage: Reports on total, used, and free disk space.
get_network_bandwidth: Shows the amount of data sent and received over the network.
get_temperature_info: Retrieves temperature information if available (not all systems support this).
print_report: Prints all collected metrics to the console.
Main Loop: Continuously prints the report every 60 seconds.

Ctrl+C to stop, in the terminal. 

Example output:

System Information:
System: Windows
Node Name: Whataboutnow
Release: 11
Version: 10.0.22111
Machine: AMD64
Processor: Intel64 Family 6 Model 186 Stepping 2, GenuineIntel

CPU Usage:
CPU Usage: 2.5%

Memory Usage:
Total Memory: 7.65 GB
Available Memory: 0.65 GB
Used Memory: 7.00 GB
Memory Usage: 91.50 GB

Disk Usage:
Total Disk Space: 475.86 GB
Used Disk Space: 145.43 GB
Free Disk Space: 330.43 GB
Disk Usage: 30.60 GB

Network Bandwidth:
Bytes Sent: 135.23 MB
Bytes Received: 1624.72 MB
Packets Sent: 478939.00 MB
Packets Received: 1511981.00 MB

Temperature Information:
Temperature monitoring not supported.

