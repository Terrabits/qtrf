def to_list(ports_str):
    ports_str = ports_str.strip()

    # empty list?
    if not ports_str:
        return []

    # clean up trailing partial entry
    if ports_str[-1] == '-':
        ports_str = ports_str[:-1]
    if ports_str[-1] == ',':
        ports_str = ports_str[:-1]

    # empty list?
    if not ports_str:
        return []

    ports = list()
    parts = ports_str.split(',')
    for part in parts:
        part = part.strip()
        if '-' not in part:
            # single port
            port = int(part)
            if not port in ports:
                ports.append(port)
        else:
            # range
            start_port, stop_port = [int(i) for i in part.split('-')]
            for port in range(start_port, stop_port + 1):
                if not port in ports:
                    ports.append(port)
    ports.sort()
    return ports

def to_str(ports_list):
    if not ports_list:
        return ''

    # sort
    ports_list = ports_list.copy()
    ports_list.sort()

    parts = []
    while ports_list:
        port1 = ports_list.pop(0)
        if not ports_list:
            # no more ports
            parts.append(str(port1))
            break

        port2 = ports_list[0]
        if port2 != port1 + 1:
            # single port
            parts.append(str(port1))
            continue

        # range

        # take port2
        ports_list.pop(0)

        # find end of range
        increment = 1
        while ports_list and ports_list[0] == port1 + increment + 1:
            port2      = ports_list.pop(0)
            increment += 1

        parts.append(f'{port1}-{port2}')

    return ', '.join(parts)
