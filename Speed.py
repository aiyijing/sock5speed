import requests
import socket
import socks
import time
import getopt
import sys


def init(proxy):
    socks.set_default_proxy(socks.SOCKS5, proxy["host"], proxy['port'])
    socket.socket = socks.socksocket


def down_speed(url):
    try:

        start = time.clock()
        resp = requests.get(url, timeout=5)
        end = time.clock()

        total_time = end-start
        content_length = resp.headers.get("content-length")

        if not content_length:

            content_length = len(resp.content)

        speed = content_length / float(total_time)

        return total_time, speed, resp
    except Exception:
        return None, None, None


if __name__ == "__main__":

    # url
    req_url = ""

    # 代理
    proxy = {"host": "0.0.0.0", "port": 0}

    # loop
    loop = False

    # spare_time
    spare_time = 5

    # is Verb
    verb = False

    # total count
    count = 0

    # hit ratio
    hit_count = 0

    options, args = getopt.getopt(sys.argv[1:], "-h-l-vp:u:t:", ["proxy=", "url=", "time=", "loop", "help", "verb"])
    if not options:
        print("args:\n"
              "\t--proxy=127.0.0.1:1080 \t(代理服务器)\n"
              "\t--url=http://www.baidu.com \t(访问网址)\n"
              "\t--time=5 \t(每次间隔)\n"
              "\t--verb \t(显示下载内容)\n"
              "\t--loop \t(是否循环)\n"
              "\t--help \t(帮助)\n")
        exit(0)
    for name, value in options:
        if name == "--help":
            print("args:\n"
                  "\t--proxy=127.0.0.1:1080 \t(代理服务器)\n"
                  "\t--url=http://www.baidu.com \t(访问网址)\n"
                  "\t--time=5 \t(每次间隔)\n"
                  "\t--verb \t(显示下载内容)\n"
                  "\t--loop \t(是否循环)\n"
                  "\t--help \t(帮助)\n")
            exit(0)
        if name == "--proxy":
            host, port = value.split(":")
            proxy["host"] = host
            proxy['port'] = int(port)
        if name == "--url":
            req_url = value
        if name == "--loop":
            loop = True
        if name == "--verb":
            verb = True
        if name == "--time":
            spare_time = int(value)

    init(proxy)

    while True:

        count += 1
        total_time, speed, response = down_speed(req_url)

        if response:
            hit_count += 1
        else:
            print("Count: {}\ttotal:  \tTime Out\t HitRatio:{:.4}%".format(
                    count,
                    hit_count / float(count) * 100
                )
            )
            continue
        print("Count: {}\ttotal: {:.8} s\tspeed: {:.8} KB/sec\t HitRatio:{:.4}%".format(
                count,
                total_time,
                speed/1000,
                hit_count/float(count)*100
            )
        )

        if verb:
            print("Content:\n{}".format(response.text))
        if not loop:
            break

        time.sleep(spare_time)

