## Install Dependencies

```
pip install -r requirements.txt
```

## Install ChromeDriver

https://chromedriver.chromium.org/downloads

#### Note : Check your Chrome Browser version, Install the same ChromeDriver version 

```
sudo apt-get install unzip
unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads
sudo mv -f ~/Downloads/chromedriver /usr/local/share/
sudo chmod +x /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

## Run App

```
python app.py \ python3 app.py
```