# system input

- download deb file: linux sogou pinyin input
- install the software
- add chinese language support
- reboot and add pinyin input to fcix

# install pip3

sudo -H apt install python3-pip

# ubuntu system snapshot

- download timeshift

# bash 自动补全忽略大小写

在 ~/.inputrc 文件末尾添加一行
set completion-ignore-case on
关闭 terminal ， 重新打开

# 系统常用命令

- code directory： 用 vscode 打开文件夹
- firefox refference： 用浏览器打开本地文件或远程文件

# electronic 版本的微信

electronic wechat

# electronic app 安装
npm install
npm run

# git 开发流程

- git clone 
- git add
- git commit
- git push

> gitignore file: /-directory | * | ? | ! |

# selenium 环境准备

- pip install selenium
- 下载浏览器驱动 geckodriver | chromedriver
- 测试是否安装成功 
    - python -c "from selenium import webdriver;webdriver.Chrome().get('https://www.baidu.com')"
    - python -c "from selenium import webdriver;webdriver.Firefox().get('https://www.baidu.com')"

> sudo apt install chromium-browser

# python 命令行

- pydoc -p 8000 
- python -m module args
    - python -m virtualenv
- python -c code
- python --version