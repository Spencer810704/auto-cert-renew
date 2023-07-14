import json
import argparse
import subprocess


acme_dns_api = {
    "godaddy"   : "dns_gd", 
    "cloudflare": "dns_cf"
}


def load_data() -> list:
    with open("data.json", "r") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":

    # 讀取Command參數
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    args = parser.parse_args()

    acme_path    = "/Users/spencer/.acme.sh"
    env          = {"LE_WORKING_DIR": acme_path}
    domain       = args.domain

    # 讀取域名商的API資訊(Godaddy、Cloudflare等)
    data_list = load_data()

    for data in data_list:
        if data['domain'] == domain:
            
            # acme.sh 每次執行時會讀取環境變數儲存到 ~/.acme.sh/account.conf 內 , 目前不支援多帳號管理
            # 所以透過每次執行腳本設定環境變數時儲存到 ~/.acme.sh/account.conf 更新 Key & Secret
            env.update({
                # Godaddy API 驗證資訊
                "GD_Key":    data['token']['key'],
                "GD_Secret": data['token']['secret'],
            })

            # 組合執行命令字串
            exec_command = [
                f"{acme_path}/acme.sh", "--issue", 
                "--dns",  acme_dns_api[data['dns_provider']], 
                "-d", domain, "-d", f"*.{domain}", 
                "--force", "--log",
                # "--test"
            ]

            # 執行acme簽發指令
            result = subprocess.run(exec_command, env=env, shell=False, capture_output=True)
            print(result.stdout.decode('utf-8'))
            print(result.stderr.decode('utf-8'))

