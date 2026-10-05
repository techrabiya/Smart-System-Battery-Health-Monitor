import psutil
import platform
from datetime import datetime

def check_system_health():
    print("=" * 50)
    print(" 🚀 RABIA'S ELITE SYSTEM & BATTERY MONITOR 🚀")
    print("=" * 50)
    
    print(f"System Platform : {platform.system()} {platform.release()}")
    print(f"Processor       : {platform.processor()}")
    print(f"Timestamp       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage       : {cpu_usage}%")
    
    ram = psutil.virtual_memory()
    print(f"Total RAM       : {round(ram.total / (1024**3), 2)} GB")
    print(f"Used RAM        : {ram.percent}%")
    
    battery = psutil.sensors_battery()
    if battery:
        plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
        print(f"Battery Percent : {battery.percent}%")
        print(f"Power Status    : {plugged}")
    else:
        print("Battery Status  : No battery detected (Desktop PC)")
    print("=" * 50)

if __name__ == "__main__":
    check_system_health()
