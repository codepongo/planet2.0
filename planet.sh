#/bin/sh
cp /home/zuohaitao/www/html/rss/index.html /home/zuohaitao/www/html/rss/index`date '+%Y%m%d'`.html
cd /home/zuohaitao/planet
python planet.py config.ini > ../log/planet.log 2>&1
