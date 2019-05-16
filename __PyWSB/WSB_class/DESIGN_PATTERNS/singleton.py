import urllib,re


_url=""

def get(refresh=False):
    if refresh:
        get.rates={}
    if get.rates:
        return get.rates

    with urllib.request.urlopen(_url) as file:
        for line in file:
            line=line.rstrip().decode("utf-8")
            if not line or line.startswith(("#","Date")):
                continue
            name,currency,*rest=re.split(r"\s*,\s",line)
            key="{}({})".format(name,currency)
            try:
                get.rates[key]=float(rest[-1])
            except ValueError as err:
                print("error{}:{}".format(err,line))
    return get.rates
get.rates={}


