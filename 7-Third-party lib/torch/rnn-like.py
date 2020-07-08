import torch
import torch.nn
import torch.nn.utils.rnn

input_size, hidden_size = 3, 4
layers, directions = 2, 2
batch_size, sequence_length = 6, [6, 5, 4, 3, 2, 1]
ml = torch.nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=layers, bidirectional=True)
h0 = torch.ones(layers * directions, batch_size, hidden_size)
c0 = torch.ones(layers * directions, batch_size, hidden_size)
input0, n, input1 = [], 0, torch.zeros(sequence_length[0], batch_size, input_size)
for sl in sequence_length:
    rand_input = torch.rand(sl, input_size)
    input0.append(rand_input)
    input1[0:sl, n:n + 1, :] = rand_input.unsqueeze(1)
    n = n + 1
x = input1
input0 = torch.nn.utils.rnn.pack_sequence(input0)
input1 = torch.nn.utils.rnn.pack_padded_sequence(input1, sequence_length)
out = ml(x, (h0, c0))
out0 = ml(input0, (h0, c0))
out1 = ml(input1, (h0, c0))