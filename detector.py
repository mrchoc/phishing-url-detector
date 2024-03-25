import urllib.request
import urllib.parse
import tarfile

def download():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/ALL-phishing-domains.tar.gz", "ALL-phishing-domains.tar.gz")
    file = tarfile.open("ALL-phishing-domains.tar.gz")
    file.extractall('./extracted')

def extract_domain(url):
    if "http" not in url:
        url = "http://" + url
    domain = urllib.parse.urlparse(url).netloc
    return domain

def blacklist(url):
    f = open("./extracted/ALL-phishing-domains.txt", "r")
    for line in f:
        line = line.strip()
        if line in url:
            print("detected in blacklist")
            return True
    return False

def detect_homoglyphs(url):
# Define a dictionary of homoglyph characters and their equivalent Latin character
    homoglyphs = {'а': 'a', 'Ь': 'B', 'ḉ': 'c', 'Ď': 'D', 'е': 'e', 'Ƒ': 'F', 'ĝ': 'g', 'Ĥ': 'H', 'і': 'i', 'Ј': 'J', 'к': 'k', 'Ĺ': 'L', 'м': 'm', 'ñ': 'n', 'Ρ': 'P', 'ř': 'r', 'Ş': 'S', 'ť': 't', 'υ': 'u', 'ν': 'v', 'Ŵ': 'W', 'χ': 'x', 'у': 'y', 'ž': 'z'}
    domain = extract_domain(url)
    for char in domain:
        if char in homoglyphs.keys():
    # If a homoglyph character is found in the domain name, report it as suspicious
            print("detected homoglyphs")
            return True
    # Otherwise, the URL is probably safe
    return False

def main():
    url = input()
    download()
    if blacklist(url) or detect_homoglyphs(url):
        print(f"{url} might be a phishing url")
    else:
        print(f"{url} is likely not a phishing url")

if __name__ == "__main__":
    main()
