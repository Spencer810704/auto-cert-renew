Table of contents
- [簡介](#簡介)
- [安裝](#安裝)
- [使用](#使用)


# 簡介
(目前功能開發中 , 尚未完成)

以下為工具安裝方式


# 安裝

```shell
# Clone專案
git clone https://github.com/Spencer810704/auto-cert-renew

# 切換目錄
cd auto-cert-renew

# 安裝套件
pip install -r requirements.txt
```

# 使用

取消使用 acme.sh 的 crontab 功能 , 取而代之的是使用系統監控程式呼叫更新指定的域名

```shell

acme.sh --uninstall-cronjob

```