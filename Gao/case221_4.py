#实现ip排序
def ip_sort(ip_list):
    def strtoint(ipstr):
        parts = list(map(int, ipstr.split('.')))
        partsall =  (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8)  + parts[3]
        return partsall
    sortedip = sorted(ip_list, key=strtoint)
    return sortedip
ips = [
    '10.168.1.100',
    '192.0.0.2',
    '17.16.0.1',
    '10.168.1.2',
    '192.168.1.1'
]
print(ip_sort(ips))