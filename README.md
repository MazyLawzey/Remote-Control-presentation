# Remote Control Presentation
Remote Control Presentation - Control your slides from your phone via web interface;
If you have an improved version, I will be glad to see it in the pull request.

# Attention! if you have macos, then allow accessibility for ide 🚨

# Running HTTPS Site

Steps for local HTTPS server launch:

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Generate self-signed certificate for `localhost`:

```bash
bash generate_cert.sh
```

The script creates `certs/cert.pem` and `certs/key.pem`.

3. Launch the application (default port 443):

```bash
python3 main.py
```

Open in browser: https://localhost:443

To use a different port, export `PORT` before launch:

```bash
PORT=443 python3 main.py
```

Note: Browser will show security warning (self-signed certificate). For testing, add exception.
