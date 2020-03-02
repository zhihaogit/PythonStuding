# pyenv是 python版本管理工具
# 可以改变全局的 python版本，安装多版本 python，可以设置目录级别的 python版本
# 还能创建和管理 virtual python environments
# 所有设置都是有用户级别的操作，不需要 sudo
# pyenv通过系统修改环境变量来实现 python不同版本的切换
# virtualenv通过将 python包安装到一个目录来作为 python包虚拟环境，通过切换目录来实现不同包环境间的切换

# pyenv没有采用将不同的 PATH植入不同的 shell这种高耦合的工作方式，而是简单地在 PATH的最前面插入了一个垫片路径(shims)
~/.pyenv/shims:/usr/local/bin:/usr/bin:/bin
# 所有对 python可执行文件的查找会首先被这个 shims路径截获，从而使后方的系统路径失效

# macos安装
brew install pyenv

# 在 .zshrc之类的文件中加入
export PATH = "$HOME/.pyenv/bin:$PATH"

# 常用命令
pyenv versions # 查看本机安装版本，星号表示当前正在使用的 python版本
pyenv install -l # 查看可安装版本
pyenv install 2.7.17 # 安装 pyhton
pyenv uninstall 2.7.17 # 卸载 python
# python切换
pyenv global 2.7.17 # 设置全局的 python版本，通过将版本号写入 ~/.pyenv/version文件的方式
pyenv local 2.7.17 # 设置 python本地版本，通过将版本号写入当前目录下的 .python-version文件的方式
# 以local方式设置的版本比 global高
pyenv shell 2.7.17 # 设置面向 shell的 python版本
pyenv shell --unset # 取消当前 shell设定的版本

pyenv rehash # 创建垫片路径(为所有已安装的可执行文件创建 shims)
# 增删 python版本或带有可执行文件的包(如 pip)以后，都需要执行一次命令


# pyenv-virtualenv
# pyenv的插件，通过 pyenv-virtualenv插件可以很好的和 virtualenv结合
# macos安装
brew install pyenv-virtualenv

# 在 .zshrc加入
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 创建虚拟环境
pyenv virtualenv 2.7.17 env-name
# 不指定 python版本，将使用默认的版本

# 列出当前虚拟环境
pyenv virtualenvs
pyenv activate env-name # 激活虚拟环境
pyenv deactivate # 退出虚拟环境，回到系统环境
pyenv virtualenvs-delete [-f|--force] env-name # 删除相应的虚拟环境
pyenv uninstall env-name # 删除相应的虚拟环境
