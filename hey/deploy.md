# download and unzip binary
``` bash
mkdir Downloads
mkdir bin
curl -L https://github.com/ningliaoyuan/smartcloudshell/releases/download/v0.5/smartcloudshell_linux_64-bit.tar.gz -o ./Downloads/smartCloudShell.tar.gz
tar -xvzf ./Downloads/smartCloudShell.tar.gz -C ./bin
```

# export path to include hey
```
vim .bashrc
export PATH=$PATH:~/bin
source .bashrc
```