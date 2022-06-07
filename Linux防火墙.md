### Linux防火墙概述

##### 防火墙的基本概念和分类

> 常见防火墙类别：

+ 包过滤防火墙：针对IP及端口2个条件进行数据包的安全过滤，不考虑其他任何因素
+ 状态防火墙：包括包过滤防火墙的所有功能，同时追踪数据包的每一个工作状态，如下图所示：重点多了一个状态检查表

##### 防火墙基本管理工具

+ iptables：netfilter防火墙配置工具，Centos7之前的默认防火墙
+ firewalld：Centos7及之后版本的默认防火墙

##### iptables数据流量的分类

> 以流量的流向及源地址、目标地址等分类，大体可以分为3种流量：

+ 入站流量（目标地址为防火墙）
+ 出站流量（源地址为防火墙）
+ 转发流量（源地址、目标地址均不是防火墙）

```
Linux的Netfilter防火墙在tcp/ip协议栈中插入5个*hook function*，俗称为钩子（检查点），在各个环节对数据包处理。规则的匹配从上往下逐条检查，匹配后及采取丢弃、放行、修改、重定向等各种措施，如无匹配项，按照默认规则的配置，或放行，或阻止
```

##### iptables策略与规则链(5条规则链)

> iptables服务把处理或过滤流量的策略称为规则，多条规则组成一个规则链（chains），iptables具有5条规则链，处理各个传输环节的数据包，具体如下：

+ PREROUTING：路由选择前，路由选择前处理数据包；入站包及转发包都可以使用
+ INPUT：路由选择后，目的地为本机，入站包才可以使用
+ OUTPUT：本机产生的数据包对外转发，出站包才可以使用
+ FORWARD：路由选择后，目的不为本机，转发包才可以使用
+ POSTROUTING：离开本机网卡前，路由选择后处理数据包。所有数据包都可以使用，最后一步的处理，如SNAT，地址伪装

##### iptables表的概述（5张表）

> 表可以看作为了特定功能而实现的规则的分类，其目的就是为了便于实现不同的功能及目的。如filter表，实现包过滤功能，做出“通行”或“阻止”的行为，而不对数据包做任何的修改；nat表用于地址转换，转换源地址--SNAT，或转换目标地址--DNAT，五表分别为：

+ filter表：包过滤，使用3条链，如下： 

  - INPUT
  - Forward
  - OUTPUT

+ nat：地址转换，实现源地址或目的地址的转换，使用3条链： 

  + PREROUTING

  - OUTPUT
  - POSTROUTING

+ mangle：修改数据包的相关内容，如TTL、TOS字段等，其主要作用就是给数据包打标记，以便于做如策略路由的操作，表可以使用所有链；（暂时不用例会）

+ raw：连接跟踪处理，可以选择不追踪某些数据包，默认系统的所有数据包都会被跟踪。（暂时不用理会）

+ security：强制访问控制MAC（暂时不用理会）

> iptables最常用的两张表：filter、nat

```
fillter表：
```

- ALLOW 放行
- DROP 拒绝

```
nat表：
```

- SNAT 源地址转换
- DNAT 目的地址转换

##### iptables语法概要

```
iptables [-t table] CMD [chain] [rules] [-j target]
```

- table（表）：指定使用的表名，如果不指定，则filter为默认表
- CMD（操作命令）：添加、删除、更新链规则等各种指令
- chain（链）：指定链名称，如INPUT、OUTPUT等
- rules（匹配条件）：ip、端口、tcp/udp协议、接口-（物理接口、逻辑接口）等
- target(目标)：即动作，ALLOW、DROP等

##### iptable设置初始防火墙的3个步骤

- 清除所有规则

- 设置默认防火墙规则（DROP）
- 设置防火墙规则

1. 清除防火墙规则

```
iptables [-t table] [-FXZ] [chain]
```

- -F：清除指定链及表中的所有规则，若没有指定链，则清除所有链的所有规则
- -X：删除用户自定义链
- -Z：包、字节计数器全部清零

表、链规则太多，可以l利用脚本自动清除

```
for table in {filter,nat,mangle,raw}
do
	for CMD in {"-F","-X","-Z"}
	do
    	iptables -t $table $CMD
    done
done
注：可以先查看下系统中的现存规则，再决定是否保存后再清除

# 查看系统iptables默认规则，如果没有使用-t tablename指定表，则默认为filter表
iptables -nvL

# 参数的含义为：
-L：列出链中的规则
-v：显示详细信息，包括每条规则的匹配包数量和匹配字节数 
-n：只显示 IP 地址和端口号码，不显示域名和服务名称

详细列出filter表中所有链的规则，并显示行号(--line-numbers 显示策略所在的行号)
iptables -nvL --line-numbers
```

2. 设置防火墙默认规则

> iptables默认策略为ACCEPT，表示匹配不到其他策略就放行，通常这种情况是不允许的，所以需要修改默认策略为DROP，但要注意先放行SSH协议，否则在修改默认策略后，远程SSH连接终端会连接不上

```
# 修改iptables的默认规则为DROP（默认操作的是filter表）
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
```

3. 设置防火墙规则

> 防火墙规则从上往下匹配，一旦匹配到了相关规则，则剩余的规则不再检查。

```
iptables [-t 要操作的表] <操作命令> [要操作的链] [规则号码] [匹配条件] [-j 匹配到以后的动作]
```

> 常用的控制类型

```
ACCEPT：允许数据包通过
DROP：直接丢弃数据包，不给出回应
REJECT：礼貌拒绝，会回显消息
```

> 常用命令选项：可通过iptables -h查看

- -A：规则链末尾添加规则，常用的添加规则方式
- -I：在指定规则的位置插入一条规则，需要先使用--line-numbers选项确定规则的位置
- -R：替换掉指定的规则号规则
- -D：删除指定的规则号规则
- -P：设置默认策略
- -F：清空规则链中的规则

- -L：列出链中的规则
- -v：显示详细信息，包括每条规则的匹配包数量和匹配字节数，需要配合-L参数使用
- -n：只显示 IP 地址和端口号码，不显示域名和服务名称，需要配合-L参数使用
- --line-numbers：列出规则时，显示其在链上相应的编号

- -s：检查报文的源IP地址是否符合此处指定的范围，或是否等于此处给定的地址
- -d：检查报文的目标IP地址是否符合此处指定的范围，或是否等于此处给定的地址
- -p：匹配报文中的协议
- -j：指定要进行的处理动作
- -i：指定数据包从哪个网卡流入
- -o：指定数据包从哪个网卡流出
- --sport：源端口
- --dport：目的端口
- -m：扩展用法
  - conntrack:
    + NEW,RELATED,ESTABLISHED
  - multiport(80,22,443等) :
    - --sports 源端口范围
    - --dports 目的端口范围

- --ports  # 不区分源、目的端口，匹配即执行动作

- iprange
  - --src-range from[-to] && [!] --src-range from[-to]
  - --dst-range from[-to] && [[!] --dst-range from[-to]

### iptables的安装和相关配置文件

##### 安装

```
1.先关闭firewall防火墙，两个需要同时开启
systemctl stop firewalld.service     # 停止firewall
systemctl disable firewalld.service  # 禁止开机启动
2.安装iptables防火墙
yum -y install iptables-services
```

##### 配置文件的位置

```
ll /etc/sysconfig/iptables-config
-rw------- 1 root root 2116 Oct  2  2020 iptables-config
```

##### 启动服务，并设置开机自启动

```
# 查看服务状态
service iptables status
systemctl status iptables
# 重启服务
service iptables restart
systemctl restart iptables
# 启动服务
systemctl start iptables.service
# 设置开机启动
systemctl enable iptables.service
# 设置iptables防火墙规则后需要保存，才能在下次开机时自动启用规则：
service iptables save
systemctl enable iptables
```

### 实践案例

##### 小试牛刀

```
# 查看nat表中所有链的规则
iptables -t nat -nvL

# 显示filter表包括ip和port的详细信息(不能是-Lnv，L不能在最前面)
iptables -nvL

# 清除filter表中所有链上的规则(不指明表，默认是filter表)
iptables -F
iptables -t filter -F

# 清空NAT表中所有链上的规则
iptables -t nat -F

# 禁止filter表的INPUT链任何数据访问(ssh也不能连接了，谨慎操作)
iptables -t filter -A INPUT -j DROP

# 在filter表的INPUT链中最后一条规则后面添加允许任何tcp协议访问本机
iptables -t filter -A INPUT -p tcp -j ACCEPT

# 在filter表INPUT链第二行插入规则,允许tcp的80端口通过
iptables -I INPUT 2 -p tcp --dport 80 -j ACCEPT

# 禁止192.168.193.151机器tcp的22号端口(即ssh访问)访问本机
iptables -A INPUT -s 192.168.193.151 -p tcp --dport 22 -j DROP

# 禁止本机tcp的22号端口访问192.168.193.151机器(即ssh访问)
iptables -A OUTPUT -d 192.168.193.151 -p tcp --sport 22 -j DROP

# 显示编号的数据包流入规则
iptables -nvL INPUT --line-numbers

# 删除filter表中INPUT链的第三条规则
iptables -D INPUT 3
```

##### 清除默认

1. 设置22端口访问规则(即ssh连接)

```
# 允许远程22端口访问本机
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
# 允许本机22端口数据包流出
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
# 清除filter表的默认规则
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
# 查看配置的规则
iptables -vnL
注：此时ssh连接正常
```

##### 状态检查

> 通过状态检查表，只要数据包能够进来就可以出去(iptables规则链再进行匹配时，从上往下匹配，先检查第一条规则，一旦匹配到了相关规则，后续规则就不再匹配，即状态检查规则应放第一位)

```
# 插入一条规则，放在第一个位置，-m扩展用法，指定conntrack链接跟踪，ctstate即状态，指名要跟踪的状态，
iptables -I INPUT 1 -p tcp -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -vnL --line-numbers
iptables -I OUTPUT 1 -p tcp -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -vnL --line-numbers
# 删除OUTPUT链中的22端口数据包流出规则，此时ssh终端仍然能保持连接状态
iptables -D OUTPUT 2
# 查看路由
route
# 修改规则，指定只有虚拟机路由IP可以访问，禁止其他机器ssh远程连接访问本机
iptables -R INPUT 2 -s 192.168.193.0 -p tcp --dport 22 -j ACCEPT
```

##### IP的指定

> 指定数据包流向，即访问机器的IP，-d选项控制

```
# 指定要访问机器的IP
iptables -R INPUT 2 -s 192.168.193.0 -d 192.168.193.150 -p tcp --dport 22 -j ACCEPT
```

##### 指定网卡

> 指定数据包访问从哪个网卡流入，即设置iptables -nvL中的in标签，-i选项

```
# 查看网卡信息
ifconfig
ip addr
# 指定数据包流向，从ens33网卡流入访问本机
iptables -R INPUT 2 -s 192.168.193.0 -d 192.168.193.150 -p tcp --dport 22 -i ens33 -j ACCEPT
```

##### 新包访问

> 新数据包流出

```
# 由于前面设定的状态表在OUTPUT链中没有设定额外的规则，只有INPUT表中能够访问的数据流入包才能正常流出，新的数据包无法流出，即ssh连接其他机器会被拒绝，yum下载也会被拒绝等
ssh 192.168.193.151
yum -y install nginx
# 修改流出状态表规则，去掉了-p指定的协议类型
iptables -R OUTPUT 1 -m conntrack --ctstate NEW,RELATED,ESTABLISHED -j ACCEPT
```

##### 替换已有

```
# 只允许192.168.193.151访问本机
iptables -R INPUT 1 -s 192.168.193.151 -p tcp --dport 22 -j ACCEPT
注：INPUT链后面的规则编号必须带
```

##### 源IP范围

```
# 只允许151到154的机器访问本机(包括边界，即151和154都能ssh访问)
iptables -R INPUT 1 -m iprange --src-range 192.168.193.151-192.168.193.154 -p tcp --dport 22 -j ACCEPT
# 不允许151到154的机器访问本机(包括边界，即151和154也不能访问)
iptables -R INPUT 1 -m iprange ! --src-range 192.168.193.151-192.168.193.154 -p tcp --dport 22 -j ACCEPT
```

##### 放多端口

> 指定多个端口，避免写多条规则

```
# 放行多个端口，-m指定多端口选项multiport
iptables -A INPUT -m multiport -p tcp --dport 80,8080,443 -j ACCEPT
```
