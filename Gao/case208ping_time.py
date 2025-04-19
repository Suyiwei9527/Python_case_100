import subprocess
import re

def ping_and_filter(host, count, threshold=0.5, output_file='time'):
    all_time = []
    with open(output_file, 'w+') as f:
        process = subprocess.Popen(['ping', '-c', count, host , '-D'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate()
        time_pattern = re.compile(r'time=([\d.]+) ms')
        lines = output.splitlines()
        all_time.extend(line + '\n' for line in lines[-3:])
        for line in lines:
            match = time_pattern.search(line)
            if match:
                time_ms = float(match.group(1))
                if time_ms > threshold:
                    all_time.append(line + '\n')
        f.writelines(all_time)
ping_and_filter('10.108.187.251','10')