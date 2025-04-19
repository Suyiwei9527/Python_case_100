with open('Gao/ePolicy/test.txt', 'w') as f:
    f.write(("wrk.headers[\"Connection\"] = \"b\"\n") * (10000 * 1 * 1))