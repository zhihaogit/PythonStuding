# virtualenvwrapper将所有的虚拟环境都放在一个地方
# 可以自动补全 虚拟环境的名字

# 安装（确保 virtualenv已经安装）
pip install virtualenvwrapper

cd $HOME
mkdir Envs Devel
# 在 .bashrc或 .zshrc中修改环境变量
# 可参考 .zshrc_example
export WORKON_HOME=$HOME/Envs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

# 创建一个虚拟环境
mkvirtualenv my_project
# 会在 $HOME/Envs中创建 my_project文件夹

# 在虚拟环境上工作
workon my_project
# workon 也能停止当前所在的环境

# 可以创建一个项目，它会自动创建虚拟环境，并在 $WORKON_HOME中创建一个项目目录

mkproject myproject
workon myproject
# 会自动 cd到项目目录中

# 列举所有的环境
lsvirtualenv

# 导航到当前激活的虚拟环境的目录中，方便浏览 site-packages
cdvirtualenv

# 直接进入到 site-packages目录中
cdsitepackages

# 显示 site-packages目录中的内容
lssitepackages

# 停止虚拟环境
deactivate

# 删除
rmvirtualenv my_project