# Import the necessary library
import time
import speedtest
import csv
import math # Keep math if needed for other things, but not for basic Mbps conversion
import os
from datetime import datetime # Added for a more standard timestamp

# Function to convert BITS per second to MEGABITS per second
def bits_to_mbps(size_bits):
    # 1 Megabit = 1,000,000 bits
    # Return the numerical value, rounded to 2 decimal places
    if size_bits <= 0:
        return 0.0
    return round(size_bits / 1_000_000, 2)

# --- Main part of the script ---
print("Initializing Speedtest...")
try:
    # Instantiate the speedtest object
    speed = speedtest.Speedtest()

    # Optional: Add a small delay if you find it helps reliability
    # time.sleep(1)

    print("Getting best server based on ping...")
    # Get the best server (runs ping tests to find the closest)
    # This info will be stored in speed.results after tests run
    speed.get_best_server()
    # You can print server info here if desired, before the main tests
    best_server = speed.results.server
    print(f"Found best server: {best_server['sponsor']} ({best_server['name']}, {best_server['country']})")


    print("Performing download speed test...")
    # Get the download speed (returns BITS per second)
    download_speed_bps = speed.download()

    print("Performing upload speed test...")
    # Get the upload speed (returns BITS per second)
    upload_speed_bps = speed.upload()

    # Results are now available in speed.results
    results = speed.results

    # Get ping, timestamp, and server details from the results object
    ping_ms = results.ping
    # Use a standard ISO format timestamp for better compatibility
    # timestamp_utc = results.timestamp # This is UTC in ISO 8601 format
    # Or get current local time if preferred
    timestamp_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_info = results.server # Dictionary containing server details

    # Convert speeds to Mbps using the corrected function
    download_mbps = bits_to_mbps(download_speed_bps)
    upload_mbps = bits_to_mbps(upload_speed_bps)

    # Print the results
    print("\n--- Test Results ---")
    print(f"Timestamp: {timestamp_local}")
    print(f"Ping: {ping_ms:.2f} ms")
    print(f"Download: {download_mbps} Mbps")
    print(f"Upload: {upload_mbps} Mbps")
    print(f"Server: {server_info['sponsor']} ({server_info['name']}, {server_info['country']})")
    print(f"Server URL: {server_info['url']}") # Example of accessing server info

    # --- Save results to CSV ---
    csv_file_name = 'speed_test_results.csv'
    print(f"\nSaving results to {csv_file_name}...")

    # Define the field names (headers) for the CSV file
    field_names = ['Timestamp', 'Ping (ms)', 'Download (Mbps)', 'Upload (Mbps)', 'Server Name', 'Server Country', 'Server Sponsor', 'Server URL']

    # Prepare the data row as a dictionary (using numerical values for speeds)
    data_row = {
        'Timestamp': timestamp_local, # Using local time string
        'Ping (ms)': round(ping_ms, 2),
        'Download (Mbps)': download_mbps, # Store the number
        'Upload (Mbps)': upload_mbps,     # Store the number
        'Server Name': server_info['name'],
        'Server Country': server_info['country'],
        'Server Sponsor': server_info['sponsor'],
        'Server URL': server_info['url']
    }

    file_exists = os.path.exists(csv_file_name) and os.path.getsize(csv_file_name) > 0
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_row)
    print("Results saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")    