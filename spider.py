#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from optparse import OptionParser
import sys
from termcolor import colored
if sys.version_info[0] >= 3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

class Crawler:
    def __init__(self):
        self.about()
        self.script_desc()
        self.target_links = []


    def arguman_al(self):
        parse = OptionParser(description=self.description,epilog=self.kullanim,prog=self.program)
        parse.add_option("-u", "--url", dest="url", help="Destination url")
        (options, arguments) = parse.parse_args()
        if not options.url:
            parse.error("[-] Please specify a url, use --help for more information.")
        return options

    def get_links(self,url):
        try:
            if "http://" in url   or "https://" in url:
                response=requests.get(url)
                return re.findall('(?:href=")(.*?)"', str(response.content))
            else:
                response=requests.get("http://"+url)
                return re.findall('(?:href=")(.*?)"',str(response.content))
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass


    def crawl(self,url):
        href_links=self.get_links(url)
        if href_links:
            for link in href_links:
                link=urljoin(url,link)
                if "#" in link:
                    link=link.split("#")[0]
                if options.url in link and link not in self.target_links:
                    self.target_links.append(link)
                    print(link)
                    self.crawl(link)


    def result_count(self):
        print(colored("[+] in total, "+ str(len(self.target_links))+" No connections found","green"));

    def script_desc(self):
        self.program="spider"
        self.kullanim="""Example 1: python spider.py --url http://10.0.2.6/mutillidae
        \n\n\n\n\n 
        Example 2: python spider.py -u http://10.0.2.6/mutillidae """
        if sys.version_info[0] >= 3:
            self.description = "A web crawler script that crawls the target website and lists its links."
        else:
            self.description = unicode("A web crawler script that crawls the target website and lists its links.", "utf8")
            self.kullanim = unicode(self.kullanim,"utf8")


    def about(self):
        print(colored("__        __   _           ____                    _           ", "green"))
        print(colored("\ \      / /__| |__       / ___|_ __ __ ___      _| | ___ _ __ ", "green"))
        print(colored(" \ \ /\ / / _ \ '_ \     | |   | '__/ _` \ \ /\ / / |/ _ \ '__|", "green"))
        print(colored("  \ V  V /  __/ |_) |    | |___| | | (_| |\ V  V /| |  __/ |   ", "green"))
        print(colored("   \_/\_/ \___|_.__/      \____|_|  \__,_| \_/\_/ |_|\___|_|   ", "green"))
        print(colored("# author      :","green")+"Stephen Tumaini Kaingu")
        print(colored("# linkedin    :","green")+"https://www.linkedin.com/in/stephenkacloudy")
        print(colored("# github      :","green")+"https://github.com/highbreed")
        print(colored("# title       :","green")+"spider.py")
        print(colored("# description :","green")+"A web crawler script that crawls the target website and lists its links.")
        print(colored("# date        :","green")+"30.05.2019")
        print(colored("# version     :","green")+"1.0")
        print(colored("# ==============================================================================","green"))

    def keyboardinterrupt_message(self):
        print("[-] CTRL+C It was published. Exiting application ...")
        print("[-] Application exited!")


try:
    crawl=Crawler()
    options=crawl.arguman_al()
    print(colored("[+] Scanned Web Address:","green")+options.url+"\n")
    crawl.crawl(options.url)
    crawl.result_count()
except KeyboardInterrupt:
    crawl.keyboardinterrupt_message()


