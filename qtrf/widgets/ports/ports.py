port_regex          = r'[1-9]\d*'
range_regex         = f'\\-{port_regex}'
port_or_range_regex = f'{port_regex}({range_regex})?'
is_valid_regex      = f'^{port_or_range_regex}(, ?{port_or_range_regex})*$'

def entry_to_list(entry):
    list = []
    for item in filter(None, entry.split(',')):
        new_list = _entry_item_to_list(item)
        for i in new_list:
            if not i in list:
                list.append(i)
    list.sort()
    return list
def _entry_item_to_list(item):
    if '-' in item:
        start, stop = map(int, item.split('-'))
        return list(range(start, stop + 1))
    # else
    return [int(item)]
def list_to_entry(list):
    list = list.copy()
    entries = []
    while list:
        if len(list) == 1:
            value_str = str(list.pop())
            entries.append(value_str)
            break;
        range_start = list.pop(0)
        for index, value in enumerate(list):
            if value != range_start + index + 1:
                # passed stop_range
                if index == 0:
                    entries.append(str(range_start))
                else:
                    range_stop = list[index-1]
                    entries.append(f'{range_start}-{range_stop}')
                    list = list[index:]
                break
            elif index == len(list) - 1:
                # current item is end of range
                entries.append(f'{range_start}-{value}')
                list.clear()
                break
    return ', '.join(entries)
