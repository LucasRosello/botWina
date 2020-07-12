wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
mv chromedriver /usr/local/bin

pip3 install selenium
mv 'config copy.py' 'config.py'
mv 'saldo copy.json' 'saldo.json'

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

#  0 * * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && /usr/bin/python3 /var/www/html/botWina/botWina.py