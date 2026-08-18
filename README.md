# Discord Avatar Changer

A simple Python script that changes your Discord profile picture to a random image from a folder. It uses `curl_cffi` to mimic a real Chrome browser so your request doesn't get flagged as a bot.

## Preview

## Preview

https://raw.githubusercontent.com/NoTinyxd/Pfp-Changer/main/preview.mp4

## What it does

* **Picks a random photo:** Pulls a `.png`, `.jpg`, `.jpeg`, or `.webp` file from `Input/pfps/`.
* **Prepares the image:** Converts the file into Base64 so Discord can read it.
* **Fakes real browser headers:** Generates fresh `sec-ch-ua`, `x-super-properties`, and build info every time it runs.
* **Updates profile:** Sends a `PATCH` request to Discord's API with your new picture.

It does one thing: you run it, it changes your pfp, and it turns off. No bloated menus or background loops.

## Setup

1.  Install the requirement:
    ```bash
    pip install curl_cffi
    ```

2.  Set up your folder like this:

    ```text
    project/
    ├── Input/
    │   ├── config.json
    │   ├── token.txt        # Paste your Discord account token here
    │   └── pfps/            # Put your avatar pictures here
    └── src/
        └── modules/
            ├── helpers/
            │   ├── header.py
            │   └── avatar.py
            └── main.py
    ```

3.  Make sure `Input/config.json` looks like this:

    ```json
    {
      "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    ```

    Use a real Chrome User-Agent. The script reads the version number to build valid browser headers.

## How to run

Run the main file from your terminal:

```bash
python src/modules/main.py
```

Here are the common response codes you might see:

| Code | Status | Meaning |
| :--- | :--- | :--- |
| **`200`** |  Success | Profile picture changed successfully. |
| **`400`** |  Bad Request | Hit hCaptcha. No support for captcha yet. |

## Might Add Later

It does what I need for now. If I feel like working on it later, I might add proxy support, multi-token runs, or auto-delays or any shit stuff. Or maybe I won't.

## Issues

If something breaks, open an Issue on GitHub with:

1.  What you clicked/ran
2.  What happened vs. what was supposed to happen
3.  The response code and message (hide your token before pasting!)
4.  Your OS and Python version

*Don't DM me on Discord for support. Use GitHub issues.*

## Rules

* **Don't skid it:** Don't copy this code, change the name, and pretend you built it.
* **Don't sell it:** This is free. Selling it or hiding it behind a paywall makes you a scammer.
* **Keep it personal:** Use it on your own accounts and your own computer.
* **Give credit:** If you fork this or use parts of it, link back here.

## Disclaimer

This is for educational purposes. Use it at your own risk. If Discord flags or bans your account, that's on you.

## ☕ Donations

This tool is 100% free. If it saved you some time and you want to throw a few bucks my way, LTC is appreciated:

`LXdgPhE4UfVUgtfXkT7wR1T4Jxam9sCsbb`
