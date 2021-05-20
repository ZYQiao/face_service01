#!/bin/bash
mongo -u my_root -p my_123456 <<EOF
use 具体的数据库名;
db.createUser({user:'用户名',pwd:'密码',roles:[{role:'readWrite',db:'具体的数据库名'}]});
EOF