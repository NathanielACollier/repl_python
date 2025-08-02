# pip install speedtest-cli
import speedtest as st

def speedTest():
    test = st.Speedtest()

    down = test.download()
    down = round(down / 10**6,2)
    print(f"Download speed in Mbps: {down}")

    up = test.upload()
    up = round(up / 10**6, 2)
    print(f"Upload Speed in Mbps: {up}")

    ping = test.results.ping
    print(f"Ping: {ping}")

speedTest()
