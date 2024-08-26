import psutil
import os

def get_high_memory_processes(threshold=100):
    """
    Get a list of processes using more than the specified memory threshold in MB.
    """
    high_memory_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memory_usage_mb = proc.info['memory_info'].rss / (1024 * 1024)
            if memory_usage_mb > threshold:
                high_memory_processes.append((proc.info['pid'], proc.info['name'], memory_usage_mb))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return high_memory_processes

def terminate_process(pid):
    """
    Terminate a process by PID.
    """
    try:
        os.kill(pid, 9)
        print(f"Process with PID {pid} terminated.")
    except Exception as e:
        print(f"Failed to terminate process with PID {pid}: {e}")

def main():
    print("Checking for high memory usage processes...\n")
    threshold = int(input("Enter memory usage threshold in MB (e.g., 100): "))
    high_memory_processes = get_high_memory_processes(threshold)
    
    if high_memory_processes:
        print(f"\nProcesses using more than {threshold} MB of memory:")
        for pid, name, memory in high_memory_processes:
            print(f"PID: {pid}, Name: {name}, Memory Usage: {memory:.2f} MB")
        
        terminate = input("\nDo you want to terminate any processes? (y/n): ").lower()
        
        if terminate == 'y':
            pid_to_terminate = int(input("Enter the PID of the process to terminate: "))
            terminate_process(pid_to_terminate)
        else:
            print("No processes terminated.")
    else:
        print(f"No processes found using more than {threshold} MB of memory.")

if __name__ == "__main__":
    main()
