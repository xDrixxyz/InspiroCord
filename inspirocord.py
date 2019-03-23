#!/usr/bin/python3
import os, json, requests, time

def main():
    print("Initializing...")
    generated_quote_id = generate_quote()
    send_quote(generated_quote_id)

def generate_quote():
    print("Generating quote...")
    r = requests.get("https://inspirobot.me/api?generate=true")
    if r.ok:
        print(f"Quote ID: {r.text}")
        return r.text
    else:
        print("Failed to generate quote")
        return None

def send_quote(quoteid):
    if quoteid is None:
        print("Bad quote ID")
    else:
        discord_webhook_json = {}
        discord_webhook_json["content"] = quoteid
        r = requests.post(os.environ['INSPIROCORD_WEBHOOK_URL'], data=json.dumps(discord_webhook_json), headers={'Content-Type': 'application/json'})
        if r.status_code == 204:
            print("Success! Quote sent!")
        else:
            print("Failed to send quote")
            print(r.text)

def setInterval():
    while True:
        main()
        time.sleep(300)

if __name__ == '__main__':
    setInterval()
