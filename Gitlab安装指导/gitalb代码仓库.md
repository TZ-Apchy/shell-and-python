

# 前言

> 不管是在企业，还是个人，对于源码的安全性，是我们特别需要考虑的事情。
>
> GitLab 是一个用于仓库管理系统的开源项目，使用 Git 作为代码管理工具，并在此基础上搭建起来的 Web 服务。
>
> Gitlab 是被广泛使用的基于 git 的开源代码管理平台, 基于 Ruby on Rails 构建, 主要针对软件开发过程中产生的代码和文档进行管理,  Gitlab 主要针对 group 和 project 两个维度进行代码和文档管理, 其中 group 是群组, project 是工程项目, 一个 group 可以管理多个project , 可以理解为一个群组中有多项软件开发任务, 而一个 project 中可能包含多个 branch, 意为每个项目中有多个分支, 分支间相互独立, 不同分支可以进行归并。
>
> **可以使用自己安装的Gitlab，安装及配置如下。也可以使用https://gitlab.com/users/sign_in申请账号~**
>
> 若你没服务器，可以使用自己本地虚拟机，参考：https://blog.csdn.net/qq_42141141/article/details/126397059
>
> gitlab另外下载地址：https://packages.gitlab.com/gitlab/gitlab-ce

# 安装Gitlab

```shell
# 下载安装包（包比较大，建议下载离线包）
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-15.9.1-ce.0.el7.x86_64.rpm

# 安装前置依赖
yum install -y curl policycoreutils-python openssh-server

# centos8的前置依赖
yum install -y curl policycoreutils-python3 openssh-server
yum install -y perl

# 安装
rpm -i gitlab-ce-15.9.1-ce.0.el7.x86_64.rpm
```

> 安装成功的界面~

![](notePic\微信截图_20240201214817.png)

> 修改配置文件： `vim /etc/gitlab/gitlab.rb`
>
> 文件配置详情可以参考：https://blog.csdn.net/zhangweixbl4/article/details/135139342

```shell
# 编辑 /etc/gitlab/gitlab.rb 文件
# 修改 external_url 访问路径(自己节点ip加自定义端口[访问端口在这里写什么就是什么]，这个属性配置成什么，外部就通过这个访问~) http://<ip>:<port>
# 其他配置修改如下，修改这些配置的意义：避免占用太大内存，如果不修改，可能会将你内存占满
gitlab_rails['time_zone'] = 'Asia/Shanghai'  # 修改时区
puma['worker_processes'] = 2  # 工作节点数
sidekiq['max_concurrency'] = 8  # 最大并发数
postgresql['shared_buffers'] = "128MB"  # 缓存大小（占用内存大小，一般是内存1/4，最大14G）
postgresql['max_worker_processes'] = 4  # 进程数量
prometheus_monitoring['enable'] = false   # 默认开启，比较占用资源（内存、CPU），设置关闭 

# 其他配置
nginx['listen_port'] = 8080 # 这里配置的端口号，和 external_url 开启的端口号必须一致
git_data_dirs({ # 这是设置数据存储区域，一个是默认区域，一个是备份区域
  "default" => { # 这是默认数据存储区域
    "path" => "/xxx/xxx/gitlab/data" # 路径全部可以自定义
   },
   "alternative" => { # 这是备份数据存储区域，为避免磁盘损坏，丢失源码
    "path" => "/xxx/xxx/gitlab/data/backup" # 路径全部可以自定义
   }
})
```

> 更新配置并重启

```shell
gitlab-ctl reconfigure # 初始化  -----这么会比较久
gitlab-ctl restart # 开启服务

# 其他命令
gitlab-ctl stop # 关闭所有服务
gitlab-ctl restart # 重启所有服务
gitlab-ctl status # 查看所有服务状态
gitlab-ctl help # 帮助
gitlab-ctl reconfigure # 修改配置文件之后，需要重新加载下
gitlab-ctl show-config # 查看所有服务配置文件信息
gitlab-ctl tail # 查看日志
```

> 初始化成功，会看到初始账户和密码，初始密码是密文，必须去，目录下文件查看~

![](notePic\微信截图_20240111202119.png)

> 破解管理员的密码

```shell
[root@localhost ~]# gitlab-rails console -e production
--------------------------------------------------------------------------------
 Ruby:         ruby 2.7.4p191 (2021-07-07 revision a21a3b7d23) [x86_64-linux]
 GitLab:       14.3.2 (92acfb1b8a9) FOSS
 GitLab Shell: 13.21.1
 PostgreSQL:   12.7
--------------------------------------------------------------------------------
Loading production environment (Rails 6.1.3.2)
irb(main):001:0> user = User.where(id: 1).first   //查找UID是1的管理员账户
=> #<User id:1 @root>   
irb(main):002:0> user.password='root123'  //设置管理员的密码
=> "wjmwjm123"
irb(main):003:0> user.password_confirmation='root123'    //设置管理员的密码
=> "wjmwjm123"
irb(main):004:0> user.save!     //保存用户修改信息
Enqueued ActionMailer::MailDeliveryJob (Job ID: e643fa7a-ff6b-4ab9-b3c5-bd2fc607e78a) to Sidekiq(mailers) with arguments: "DeviseMailer", "password_change", "deliver_now", {:args=>[#<GlobalID:0x00007f0a6e3d97d8 @uri=#<URI::GID gid://gitlab/User/1>>]}
=> true
irb(main):006:0> exit
```

## 页面配置

```shell
# 查看默认密码
cat /etc/gitlab/initial_root_password
# 登录后修改默认密码 > 右上角头像 > Perferences > Password

# 默认的服务使用的是外网的服务，可以关闭~
# 修改系统配置（关闭头像配置）：点击左上角三横 > Admin
# Settings > General > Account and limit > 取消 Gravatar enabled > Save changes

# 关闭用户注册功能（一般内网，员工账号等都是自己配置，无需外面注册）
# Settings > General > Sign-up restrictions > 取消 Sign-up enabled > Save changes

# 开启 webhook 外部访问
# Settings > Network > Outbound requests > Allow requests to the local network from web hooks and services 勾选 > Save changes

# 设置语言为中文（全局）
# Settings > Preferences > Localization > Default language > 选择简体中文 > Save changes

# 设置当前用户语言为中文
# 右上角用户头像 > Preferences > Localization > Language > 选择简体中文 > Save changes
```

# 卸载

```shell
# 停止服务
gitlab-ctl stop

# 卸载 rpm 软件（注意安装的软件版本是 ce 还是 ee）
rpm -e gitlab-ce

# 查看进程
ps -ef|grep gitlab 
# 干掉第一个 runsvdir -P /opt/gitlab/service log 进程

# 删除 gitlab 残余文件
find / -name *gitlab* | xargs rm -rf
find / -name gitlab | xargs rm -rf
```

# 使用

## 配置SSH秘钥

> 本地生成ssh秘钥方式~

```shell
git config --global user.name "Your Name"
git config --global user.email your@example.com

# 生成公钥私钥(cd ~/.ssh)
ssh-keygen -t rsa -C "your@example.com"

# 打开gitlab的找到User Settings下的SSH Keys，在Add an SSH key中，复制 id_rsa.pub中的内容到key里，在Title这里给这个key设置一个名字，点击Add key就可以了

# 此设置是 Git 命令 push 的默认模式为 simple，当我们执行 git push 没有指定分支时，自动使用当前分支，而不是报错。
git config --global push.default simple
```

> 会在.ssh文件下生成俩个文件：`id_rsa`和`id_rsa.pub`
>
> gitlab界面右上角点击头像 - Preferences（偏好设置） - 左列SSH秘钥 - 将`id_rsa.pub`内容复制到秘钥 - 点击保存即可
>
> 到期时间可以不设置，不设置表示永不过期！！

![](notePic\微信截图_20240207192829.png)

------

![](notePic\微信截图_20240207193030.png)

## 创建空白项目

> 点击左上角仪表盘回到首页 - 新建项目 - 创建空白项目 - 填入对应信息 - 新建项目

![](notePic\微信截图_20240207193136.png)

------

![](notePic\微信截图_20240207193202.png)

------

![](notePic\微信截图_20240207193243.png)

> 点击左上角仪表盘回到首页，可以看到我们创建的项目 - 点击进入可以看到项目信息，分支，代码拉取方式等等

![](notePic\微信截图_20240207193436.png)

------

![](notePic\微信截图_20240207193508.png)

## 初始化本地项目 提交 远程git仓库

```shell
# 进入项目内
cd /xx/project

# 初始化
git init

# 若init后是master分支，修改本地分支名称
git branch -m master main

# 添加代码到缓存区
git add .

# 和远程仓库建立连接
git remote add origin http://121.40.45.228:8859/gitlab-instance-c82aafb6/k8s-cicd-demo.git
git branch -M main
git commit -m 'xx'

# 推送代码
git pull --rebase origin main
git push -uf origin main
```

# 添加账户

> 左上角三个横杠 - admin(管理员)

![](notePic\微信截图_20240204203135.png)

> 在概述内 - 用户(可以看到所有已存在的用户) - 新用户

![](notePic\微信截图_20240204203328.png)

> 填入要新增的账号信息和访问权限，然后点击“Create user”完成账号创建

<img src="notePic\微信截图_20240204203549.png" style="zoom:67%;" />



> 设置账户密码
>
> - 若邮箱收到验证，点开即可设计密码

![](notePic\2587d9680f5941f784be1f9cd5194f42.png)

> - 若邮箱未收到验证，即可保存后再次点击编辑，然后设置初始密码（这里的操作是root账户）

![](notePic\微信截图_20240204204349.png)

------

![](notePic\微信截图_20240204204420.png)

> 新用户 首次登录时重新设置新的密码

![](notePic\微信截图_20240204204831.png)

# 注册方式添加用户

> 点击登录界面的注册连接

<img src="notePic\微信截图_20240204205257.png" style="zoom: 67%;" />

> 填写注册信息 ，注册后不会立马生效，需要等管理员审核后才能登录

<img src="notePic\微信截图_20240204205517.png" style="zoom:67%;" />

> 进入管理员账户 - 左上角三个横 - 概览 - 用户 - 等待批准

![](notePic\微信截图_20240204205707.png)

> 审批

![](notePic\微信截图_20240204205838.png)

# 用户删除

> 进入管理员账户 - 左上角三个横 - 概览 - 用户

![](notePic\微信截图_20240204210051.png)

# 给用户拉项目

> 进入项目 - 项目信息 - 成员 - 邀请成员

![](notePic\微信截图_20240204210318.png)

> 输入成员名称 ，可以设置成员权限角色、访问到期时间

<img src="notePic\微信截图_20240204210403.png" style="zoom: 80%;" />

# 常见问题

> 问题一

首次界面502访问失败

> 若是你使用 gitlab-ctl stop后，再restart，访问是502，需要等等，内部组件启动需要时间~

```shell
# 大问题就是服务器:  1.端口号冲突  2.cpu占用过高、内存不足  3.版本兼容性

# 看下是否是服务器端口冲突了
ss -ntulp | grep 8080

# 查看内存
free -mh

# 版本问题
# 可能是你对应的操作系统不兼容该版本，那只能下载 v10.几的版本了。

```

