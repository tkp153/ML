import torch
torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = False
torch.backends.cudnn.allow_tf32 = True
data = torch.randn([1, 12, 320, 320], dtype=torch.half, device='cuda', requires_grad=True)
net = torch.nn.Conv2d(12, 32, kernel_size=[3, 3], padding=[1, 1], stride=[1, 1], dilation=[1, 1], groups=1)
net = net.cuda().half()
out = net(data)
out.backward(torch.randn_like(out))
torch.cuda.synchronize()

ConvolutionParams 
    memory_format = Contiguous
    data_type = CUDNN_DATA_HALF
    padding = [1, 1, 0]
    stride = [1, 1, 0]
    dilation = [1, 1, 0]
    groups = 1
    deterministic = false
    allow_tf32 = true
input: TensorDescriptor 0x81d41090
    type = CUDNN_DATA_HALF
    nbDims = 4
    dimA = 1, 12, 320, 320, 
    strideA = 1228800, 102400, 320, 1, 
output: TensorDescriptor 0x81f3eb70
    type = CUDNN_DATA_HALF
    nbDims = 4
    dimA = 1, 32, 320, 320, 
    strideA = 3276800, 102400, 320, 1, 
weight: FilterDescriptor 0x82378600
    type = CUDNN_DATA_HALF
    tensor_format = CUDNN_TENSOR_NCHW
    nbDims = 4
    dimA = 32, 12, 3, 3, 
Pointer addresses: 
    input: 0x7f4f94f18000
    output: 0x7f4f95170000
    weight: 0x7f4f959fe200