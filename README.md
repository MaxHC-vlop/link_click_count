# Link click count

URL shortener with [bitly](https://bitly.com/pages/home/v2) service. If the URL is already shortened, returns the number of clicks on it.

## How to start

Clone the repository with ssh :
```bash
git clone git@github.com:MaxHC-vlop/link_click_count.git
```

Create a virtual environment on directory project :
```bash
python3.10 -m venv env
```

Start the virtual environment :
```bash
. env/bin/activate
```

Then use pip (or pip3, if there is a conflict with Python2) to install dependencies :
```bash
pip install -r requirements.txt
```

Create a file in the project directory `.env` :
```bash
touch .env
```

Create `API_TOKEN` variable in `.env` file given by [bitly](https://bitly.com/a/sign_in?rd=/a/oauth_apps):

```
API_TOKEN='SUPER_SECRET'
```

Arguments :

Main.py has one positional argument. You can give it a bitlink or a standard URL.

## Run

```bash
python3.10 main.py https://bit.ly/your_bit
# or
python3.10 main.py https://google.com
```

You will see :
```bash
Number of hits on the bitlink: 0
# or
Your new bitlink: bit.ly/your_bit
```