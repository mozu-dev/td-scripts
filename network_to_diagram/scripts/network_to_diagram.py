def get_network_data(network):
    operators = network.findChildren(depth=1)
    network_data = []
    for op in operators:
        op_data = {
            'name': op.name,
            'type': op.type,
            'inputs': [],
            'references': []}

        for input in op.inputs:
            if input:
                op_data['inputs'].append(input.name)

        for par in op.pars():
            if par.isOP and par.eval():
                ref_op = par.eval()
                if ref_op and ref_op is not op:
                    op_data['references'].append(ref_op.name)

        network_data.append(op_data)
    return network_data


def generate_mermaid_chart(network_data):
    mermaid_chart = "graph LR\n"

    for node in network_data:
        mermaid_chart += f"    {node['name']}[{node['name']}]\n"

    for node in network_data:
        for input_node in node['inputs']:
            mermaid_chart += f"    {input_node} --> {node['name']}\n"
        for reference_node in node['references']:
            mermaid_chart += f"    {reference_node} -.-> {node['name']}\n"

    return mermaid_chart


network_path = '/path/to/your/network'  # ex. '/project1'
network = op(network_path)

network_data = get_network_data(network)
mermaid_chart = generate_mermaid_chart(network_data)
print(mermaid_chart)
