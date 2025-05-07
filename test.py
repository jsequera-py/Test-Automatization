import time
import subprocess
import os   

script_path = "C:\\Users\\jesus\\OneDrive\\PYTHON\\pytest-files\\speedookcla.py"
duration_seconds = 3600 # 1 hour
interval_seconds = 300 # Every 5 minutes for 12 runs in an hour
end_time = time.time() + duration_seconds
run_count = 0
print(f"Starting execution loop. Will run '{os.path.basename(script_path)}' every {interval_seconds}s for {duration_seconds}s.")
print("-" * 30)

while time.time() < end_time:
    print(f"Run {run_count}: Starting at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 30)
    subprocess.run(["python", script_path])
    run_count += 1  # Increment the run count
    time.sleep(interval_seconds) # Wait before the next run    
