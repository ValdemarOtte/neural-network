def compute_output(inputs, weights):
    outputs = []
    output = 0
    for i, input in enumerate(inputs):
        for weight in weights:
            output += input * weight[i]
        outputs.append(output)
    
    if outputs[0] > outputs[1]:
        return 1
    return 0

inputs = [15, 17]
weights = [[0.6, 0.1], [0.3, 0.9]]

print(compute_output(inputs, weights))
