import re
from datetime import datetime

def extract_time(text):
    pattern = r"\d{2}:\d{2}:\d{2}"
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

def extract_name(text):
    pattern = r"gao_vs\d+_v\d+"
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

def extract_name_rs(text):
    pattern = r"rs_\d+_\d+"
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

def calculate_time_difference(time1, time2):
    format = "%H:%M:%S"
    regex = r"\d{2}:\d{2}:\d{2}"
    match1 = re.search(regex, time1)
    match2 = re.search(regex, time2)
    if match1 and match2:
        datetime1 = datetime.strptime(match1.group(), format)
        datetime2 = datetime.strptime(match2.group(), format)
        difference = datetime1 - datetime2
        return difference.total_seconds()
    else:
        return None


with open("Gao/log time.log", "r") as fileA, open("Gao/down time.log", "r") as fileB:
    textA = fileA.read()
    textB = fileB.read()

    matchesA = re.findall(r"\d{2}:\d{2}:\d{2}", textA)
    matchesB = re.findall(r"\d{2}:\d{2}:\d{2}", textB)

    rs_names = [extract_name_rs(line) for line in textA.splitlines()]
    vs_names = [extract_name(line) for line in textB.splitlines() if line]
    print(vs_names)
    rs_times = [time for time in matchesA if time in textA]
    vs_times = [time for time in matchesB if time in textB]

    for rs_name, rs_time in zip(rs_names, rs_times):
        if rs_name is None or rs_time is None:
            continue
        rs_num = int(re.search(r"\d+$", rs_name).group())
        #print(rs_num)
        for vs_name, vs_time in zip(vs_names, vs_times):
            if vs_name is None or vs_time is None:
                continue
            vs_num = int(re.search(r"\d+$", vs_name).group())
            print(vs_num)
            if rs_num == vs_num:
                difference = calculate_time_difference(rs_time, vs_time)
                print(f"Time difference for {rs_name} and {vs_name}: {difference} seconds")
