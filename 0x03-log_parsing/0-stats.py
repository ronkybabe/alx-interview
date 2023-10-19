import sys
import signal

# Initialize variables to store metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def process_line(line):
    global total_size, line_count

    parts = line.split()
    if len(parts) == 7:
        ip, date, _, path, status_code_str, file_size_str = parts
        try:
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            total_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
        except ValueError:
            pass

    if line_count % 10 == 0:
        print_statistics()

# Handle KeyboardInterrupt (CTRL + C) gracefully
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
except KeyboardInterrupt:
    print_statistics()

