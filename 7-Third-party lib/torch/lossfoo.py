"""
loss functions
"""
import torch
import torch.nn as nn
import torch.nn.functional as f

lf = 'CrossEntropyLoss'

if lf == 'L1Loss':
    x = torch.rand(3, 2, requires_grad=True)
    y = torch.rand(3, 2)
    foo = nn.L1Loss(reduction='mean')
    loss0 = foo(x, y)
    loss1 = (x - y).abs().sum() / 6
    print(loss0, loss1)

if lf == 'MSELoss':
    x = torch.rand(3, 2, requires_grad=True)
    y = torch.rand(3, 2)
    foo = nn.MSELoss(reduction='mean')
    loss0 = foo(x, y)
    loss1 = (x - y).pow(2).sum() / 6
    print(loss0, loss1)

if lf == 'CrossEntropyLoss':
    x = torch.rand(3, 5, requires_grad=True) + 0.1
    y = torch.randint(0, 4, (3,), dtype=torch.long)
    x = f.softmax(x, 1)
    foo = nn.CrossEntropyLoss(reduction='mean')
    loss0 = foo(x, y)
    yc, r = torch.zeros(x.size(0)), 0
    for y in y.tolist():
        yc[r] = x[r, y]
        r = r + 1
    loss1 = yc.exp() / x.exp().sum(1)
    loss1 = -1 * loss1.log()
    loss1 = loss1.sum() / x.size(0)
    print(loss0, loss1)

if lf == 'CTCLoss':
    pass

if lf == 'NLLLoss':
    x = torch.rand(3, 4, dtype=torch.float32)
    y = torch.randint(0, 3, (3,))
    foo = nn.NLLLoss(weight=None)
    x = f.softmax(x, 1).log()
    loss0 = foo(x, y)
    loss1, r = 0, 0
    for index in y.tolist():
        loss1 = loss1 + x[r, index]
        r = r + 1
    loss1 = -1 * loss1 / x.size(0)
    print(loss0, loss1)

if lf == 'PoissonNLLLoss':
    pass

if lf == 'KLDivLoss':
    x = torch.rand(3, 4, dtype=torch.float32)
    x = f.softmax(x, 1).log()
    y = torch.rand(3, 4, dtype=torch.float32)
    y = f.softmax(y, 1)
    foo = nn.KLDivLoss()
    loss0 = foo(x, y)
    loss1 = y * (y.log() - x)
    loss1 = loss1.sum() / x.size(0) / x.size(1)
    print(loss0.item(), loss1.item())

if lf == 'BCELoss':
    x = torch.rand(4, 3, requires_grad=False)
    y = torch.rand(4, 3, requires_grad=True)
    foo = nn.BCELoss(reduction='mean')
    loss0 = foo(y, x)
    loss1 = -1 * x * y.log()
    loss1 = loss1 + (-1) * (torch.ones_like(x) - x) * (torch.ones_like(y) - y).log()
    loss1 = loss1.sum() / loss1.size(0) / loss1.size(1)
    print(loss0, loss1)

if lf == 'BCEWithLogitsLoss':
    pass

if lf == 'MarginRankingLoss':
    foo = nn.MarginRankingLoss(margin=0.2)
    x1 = torch.rand(3, dtype=torch.float32)
    x2 = torch.rand(3, dtype=torch.float32)
    y = torch.tensor([1, -1, 1])
    loss0 = foo(x1, x2, y)
    temp = -1 * (x1 - x2) * y + 0.2
    loss1 = temp.relu().sum() / x1.size(0)
    print(loss0.item(), loss1.item())

if lf == 'HingeEmbeddingLoss':
    pass

if lf == 'MultiLabelMarginLoss':
    pass

if lf == 'SmoothL1Loss':
    pass

if lf == 'SoftMarginLoss':
    pass

if lf == 'MultiLabelSoftMarginLoss':
    pass

if lf == 'CosineEmbeddingLoss':
    pass

if lf == 'MultiMarginLoss':
    pass

if lf == 'TripletMarginLoss':
    pass
