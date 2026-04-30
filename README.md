# pi-ai-bot
在树莓派16G上运行的个人AI助理。
#2026年4月5日
新建项目。然后练习使用git的常用操作。本文档是公开的，所以不要存放类似token，ID之类的涉及个人信息的数据。
将仓库同步到本地，使用 git pull https://github.com/nanoorchis/pi-ai-bot.git --allow-unrelated-histories
将本地文件同步到仓库，需要三步:add commit push
记录一个坑，github不再支持使用密码，而是使用token。但是自己注册的时候因为选择了Fine-grained personal access token，而豆包则是按Generate new token (classic)来指导我操作，两个一直对不上。直到自己告诉豆包“列表中只有两个选项，一个是Metadata 属性为read-only，另一个是Repository security advisories，属性为Read and write”，豆包才告诉我“我明白问题了！你现在用的是Fine-grained personal access token，这个权限太细，很容易配置错”。
然后是按豆包的指导在VS code中搭建了开发环境。不方便的地方是在树莓派中的VS-code中暂时还无法使用中文。
目前是电脑ssh登录树莓派来编辑README.md文档。

