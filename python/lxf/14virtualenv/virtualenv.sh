# virtualenv
# 如果系统的 python3只有一个版本，所有的第三方的包都会被 pip安装到 python3的 site-packages目录下
# 开发多个应用程序时，每个应用需要各自拥有一套独立的 python运行环境，方便不同版本包的安装

# 安装 virtualenv
pip install virtualenv

# 查看版本
virtualenv --version

# 新建一套独立的 python运行环境
cd $HOME
mkdir myproject
cd myproject
virtualenv --no-site-packages venv
# --no-site-packages参数表示不会将系统 python环境中的所有第三方包复制到这个虚拟环境中

# 创建一个指定 python版本
virtualenv -p /usr/bin/python2.7 venv2.7
# 或者在 .bashrc或 .zshrc中将一个环境变量将解释器改为全局性的
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7

# 激活 虚拟环境
source venv/bin/activate

# 安装第三方包
pip install jinja2
# 在 venv环境中，用 pip安装的包都被安装到 venv环境下，系统 python环境不受影响

# 创建 requirement，冷冻住包的版本
pip freeze > requirement.txt

# 根据 requirement安装包
pip install -r requirement.txt

# 退出当前的 venv环境
deactivate
# 回到正常的环境，pip和 python都将在系统 python环境运行

# 删除虚拟环境
rm -rf venv venv2.7
# 只需删除它的文件夹

# virtualenv为应用提供了隔离的 python运行环境，解决了不同应用间多版本的冲突问题
