import csv
import signal
import sys
# import random
from hokuyolx import HokuyoLX

laser = HokuyoLX()

"""
Function to write LIDAR data to CSV. Takes
- generator_func: laser.iterdist(), although any generator yielding an int and a 1081-element array would work
- filename: name of the CSV file

This function stops writing on signal interrupt (usually Ctrl-C).
"""
def write_lidar_to_csv(generator_func, filename):
    def signal_handler(sig, frame):
        print("\nInterrupted. Closing file and exiting.")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the title row
        title_row = ["Timestamp"] + [f"Distance_{i}" for i in range(1081)]
        writer.writerow(title_row)
        
        try:
            for timestamp, lidar_scan in generator_func():
                if len(lidar_scan) != 1081:
                    print(f"Warning: Expected 1081 elements, got {len(lidar_scan)}. Skipping this row.")
                    continue
                writer.writerow([timestamp] + lidar_scan)
                csvfile.flush()  # write to file immediately
        except KeyboardInterrupt:
            print("\nInterrupted. Closing file and exiting.")
        finally:
            csvfile.close()

"""
Substitute for laser.iterdist() while I'm not in the shop
"""
def lidar_generator():
    import time
    import random
    while True:
        timestamp = int(time.time())
        lidar_scan = [random.uniform(0, 100) for _ in range(1081)]
        yield timestamp, lidar_scan

if __name__ == "__main__":
    write_lidar_to_csv(laser.iterdist, "lidar_output.csv")
