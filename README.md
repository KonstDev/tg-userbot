# tg-Userbot

Userbot is application that can do diiferent things in Telegram messages.
## Installation

Install  Python and Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
sudo apt-get install python3
pip3 install whois
sudo apt-get install whois
pip3 install qrcode[pil]
pip3 install Pyrogram
pip3 install translators
```

## Launching

Clone this repo using [git](https://git-scm.com/) and run python-3 file "main1.py".
```bash
sudo apt-get install git
git clone https://github.com/KonstDev/tg-userbot
cd ubot
python3 main1.py
``` 

## Usage

`.funny <text>` - MaKe TeXt LiKe ThIs   
ex: `.funny hello world` 
  
`.whois <domain>` - gives whois information about domain.  
ex: `.whois google.com`  

`.translate <text>` - Translates text to preset using `.lang` languange, default language is english.

`.chlang <lang>` - Changes preset [language](https://pypi.org/project/translators/).     
  ex: `.chlang ru`
 
`.eval <expression> ` - Gives result of expression.    
ex: `.eval 2+2**2+4`  

`.eval_l <commanв>` - run command on your machine and return stdout.  
ex: `.eval_l lscpu`
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
