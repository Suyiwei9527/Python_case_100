keepport = 53330
curatcp = 36
rs_port = 80
portfirst = 5001
atcp_L4_nthreads = 2
atcp_L4_id_min = 64
startport = portfirst - (portfirst + rs_port) % atcp_L4_nthreads  + (curatcp - atcp_L4_id_min)
if startport < portfirst:
    startport += atcp_L4_nthreads
print((keepport - startport) % atcp_L4_nthreads == 0)
print (startport)