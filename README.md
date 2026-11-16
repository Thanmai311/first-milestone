# Milestone 2: Web Server and Reverse Proxy

My Milestone 1 website, served on Linux (Ubuntu on WSL2) using Nginx as a
reverse proxy in front of a Flask app.

## How it works
Browser -> Nginx (port 80) -> Flask (port 5000) -> website files

- **Web server:** Nginx receives requests from the browser.
- **Reverse proxy:** Nginx forwards requests to the Flask app and returns its response.
- **Flask app (`app.py`):** serves the files in the `site` folder.

## Project structure
- `site/`: HTML, CSS and JavaScript of the website
- `app.py`: Flask application
- `deploy/nginx-mysite.conf`: Nginx reverse proxy configuration

## How to run
1. `sudo apt install nginx git python3 python3-venv -y`
2. `git clone https://github.com/Thanmai311/first-milestone.git`
3. `cd first-milestone`
4. `python3 -m venv venv` and `source venv/bin/activate`
5. `pip install flask`
6. Copy `deploy/nginx-mysite.conf` to `/etc/nginx/sites-available/mysite`
7. `sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/`
8. `sudo nginx -t` then `sudo service nginx restart`
9. `python app.py` and open http://localhost

## What I learned
- What a web server is and how Nginx serves requests
- What a reverse proxy is
- Basic Linux commands and managing services
