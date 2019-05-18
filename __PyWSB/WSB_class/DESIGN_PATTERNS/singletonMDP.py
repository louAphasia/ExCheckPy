import urllib.parse
import urllib.request

class URLFetcher1:

    def __init__(self,url):
        self.urls=[]
    def fetch(self,url):
        req=urllib.request.Request(url)
        with urllib.request.urlopen(req)as response:
            if response.code==200:
                the_page=response.read()
                print(the_page)
                urls=self.urls
                urls.append(url)
                self.urls=urls

class SingletonType(type):
    _instances={}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super(SingletonType,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

#rewrite URLfetcher as Singleton

class URLFetcher(metaclass=SingletonType):

    def fetch(self,url):
        req = urllib.request.Request(url)  #
        with urllib.request.urlopen(req)as response:   #
            if response.code == 200:      #
                the_page = response.read()    #
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls
    def dump_url_registry(self):
        return ',  '.join(self.urls)


def main():
     MY_URLS=['https://google.com,'
              'https://python.org'
              ]

     print(URLFetcher() is URLFetcher())

     fetcher=URLFetcher()
     for url in MY_URLS:
         try:
             fetcher.fetch(url)
         except Exception as e:
             print(e)
     print('--------------')
     doneurls=fetcher.dump_url_registry()
     print(f'Done Urls: {doneurls}')

if __name__=='__main__':


    main()