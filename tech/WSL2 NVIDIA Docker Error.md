There are plenty of tutorials online teaching you how to set up CUDA containers in WSL2. However, I encountered a very weird error which was **completely undocumented** on the web. I forgot the exact context but the error contains something like:
```txt
OMP: System error #13: Permission denied "OMP: Error #178"
OMP: Error #178: Function Can't open SHM2 failed
```

After struggling for hours searching on both Google and Baidu, I looked into the source code (by searching for `Can't open SHM2` inside OMP's repo) and realized that it was caused by shared memory (`shm`) permission issues. After changing the `docker run` argument `--ipc=host` tp `--shm-size=1g` (erm, which was recommended by NVIDIA [here](https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html)), the issue was resolved. I have quoted the paragrpah below, apparently this option is not compulsory:
> By default, Docker containers are allotted 64MB of shared memory. This can be insufficient, particularly when using all 8 GPUs. To increase the shared memory limit to a specified size, for example 1GB, include the `--shm-size=1g` flag in your docker run command.
> Alternatively, you can specify the `--ipc=host` flag to re-use the host’s shared memory space inside the container. Though this latter approach has security implications as any data in shared memory buffers could be visible to other containers.