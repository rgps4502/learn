#!/bin/bash
# 使用当前工作目录创建earnapp使用的目錄
mkdir "$PWD/earnapp-data1";mkdir "$PWD/earnapp-data2"
docker-compose up -d
https=$(docker exec docker_earnapp1_1 bash -c "wget -qO- https://brightdata.com/static/earnapp/install.sh > /tmp/earnapp.sh && echo 'yes' |sudo bash /tmp/earnapp.sh|grep 'https://earnapp.com'")
echo "請登入https://earnapp.com 後訪問$https"
echo "============================"
https=$(docker exec docker_earnapp2_1 bash -c "wget -qO- https://brightdata.com/static/earnapp/install.sh > /tmp/earnapp.sh && echo 'yes' |sudo bash /tmp/earnapp.sh|grep 'https://earnapp.com'")
echo "請登入https://earnapp.com 後訪問$https"