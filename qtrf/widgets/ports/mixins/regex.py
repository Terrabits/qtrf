single_port_regex   = r'[1-9]\d*'
end_port_regex      = f'\\-{single_port_regex}'
port_or_range_regex = f'{single_port_regex}({end_port_regex})?'
ports_list_regex    = f'^{port_or_range_regex}(,\\s*{port_or_range_regex})*$'
