#! /bin/bash
echo "Start to pullh...\n"
cd /root/hexo/source/_posts
git pull origin master
cd /root/hexo 
echo "start generate file...\n"
hexo g

