import qsharp
qsharp.init(project_root='.')
print(qsharp.eval("mkvqe.measureall([0.1, 0.2, 0.3, 0.4], 10)"))