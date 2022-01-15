## Install [mambaforge](https://github.com/conda-forge/miniforge)
> `mamba` = `conda` in C = infinitely faster = don't use `conda` ever again, please.

```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
rm Mambaforge-$(uname)-$(uname -m).sh
```

## Install Pytorch from [Mirror](https://cloud.tencent.com/developer/article/1627527)
> Somethings, the default `pytorch` channel is slow like a (disabled) turtle...

Commands from babies, adults please go and edit `~/.condarc`:
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
# reference
# https://mirror.tuna.tsinghua.edu.cn/help/anaconda/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

# Done
conda install pytorch torchvision cudatoolkit=10.0
```

## Cloning Conda Environment
> Running Docker container as a non-root user is a good practice (maybe its just a rumour lol). BUT, most Docker containers have packages installed as root user. What can we do?

### My Issue At the Time
**Goal:** 
Docker Pytorch environment with working `nvcc` and `nvprof`

**Issues:**
1. `nvcc` and `nvprof` versions need to match exactly (which is not true for CUDA 11.3 and 11.4, not matter whether you installed it using NVIDIA's CUDA images or conda's `cudatoolkit-dev`)
2. Pytorch only supports up to CUDA 11.3 (else you need to build it from source but no thanks mate)
3. `nvcc` and `nvprof` version needs to support my WSL's CUDA driver version (11.5) (not too sure if this is 100% necessary)
4. NVIDIA's `nvcr.io/nvidia/pytorch:21.12-py3` has pytorch installed in the `root`'s conda, but I want to run the container as non-root and be able to install additional packages

**Solution:**
Clone conda environment. My `Dockerfile` is as follows:
```dockerfile
FROM nvcr.io/nvidia/pytorch:21.12-py3

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Change shell
SHELL ["/bin/bash", "-c"]

# Add User
RUN groupadd --gid $USER_GID $USERNAME \
	&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
	&& apt-get update -y \
	&& apt-get upgrade -y \
	&& apt-get install -y sudo git wget curl htop build-essential ninja-build \
	&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
	&& chmod 0440 /etc/sudoers.d/$USERNAME

# Install conda packages for VSCode
RUN conda install -y black flake8 autoflake

USER user

# Include CUDA binaries in PATH
ENV PATH=/opt/conda/bin:/usr/local/cuda/bin:$PATH

# Create local conda environment
RUN conda init --all \
	&& conda create --name user --clone base
RUN echo "conda activate user" >> /home/user/.bashrc

WORKDIR /home/user

CMD "bash"
```

### Extra Note
Ideally, your docker non-root user should match your Windows user's UID and GID in order to preserve file permissions. However, if you use VSCode's `.devcontainer.json` to launch the container, they will run the UID and GID matching script for you (it might take a while though).