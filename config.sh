# Chrome Driver
wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
mv chromedriver /usr/local/bin

# Selenium
pip3 install selenium
cp 'config copy.py' 'config.py'
cp 'saldo copy.json' 'saldo.json'

# Cron
crontab -l > mycron
echo "0 * * * * export DISPLAY=:0 && export PATH=$""PATH:/usr/local/bin && /usr/bin/python3 /var/www/html/botWina/botWina.py" >> mycron
crontab mycron
rm mycron



echo "Acordate de añadir los parametros al config.py"
exit;