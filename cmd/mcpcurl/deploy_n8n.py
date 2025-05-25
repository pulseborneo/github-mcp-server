import subprocess

def install_docker():
    print("🚧 安裝 Docker 中...")
    subprocess.run("curl -fsSL https://get.docker.com -o get-docker.sh", shell=True)
    subprocess.run("sh get-docker.sh", shell=True)
    print("✅ Docker 安裝完成。")

def deploy_n8n():
    print("🚀 部署 n8n 容器...")
        docker_cmd = (
        "docker run -d "
        "--name n8n "
        "-p 5678:5678 "
        "-v ~/.n8n:/home/node/.n8n "
        "-e N8N_BASIC_AUTH_ACTIVE=true "
        "-e N8N_BASIC_AUTH_USER=admin "
        "-e N8N_BASIC_AUTH_PASSWORD=admin123 "
        "n8nio/n8n"
    )
    )
    

    """
    subprocess.run(docker_cmd, shell=True)
    
    print("✅ n8n 已啟動！請開啟 http://[您的IP]:5678 登入")

def main():
    install_docker()
    deploy_n8n()

if __name__ == "__main__":
    main()
