import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_info(base_url, soup):
    links = []
    base_domain = urlparse(base_url).netloc
    
    for a in soup.find_all('a', href=True):
        link = urljoin(base_url, a['href'])
        if urlparse(link).netloc == base_domain:
            links.append(link)
    
    title = soup.title.string if soup.title else 'No title'
    for a in soup.find_all('a'):
        a.extract()
    text = soup.get_text(separator=' ', strip=True)
    return title, links, text

def extract_from_links(base_url, links):
    websites_info = []
    for link in links:
        full_url = urljoin(base_url, link)
        try:
            soup = scrape(full_url)
            title, links, text = extract_info(full_url, soup)
            websites_info.append({
                'url': full_url,
                'title': title,
                'text': text,
                'links': links
            })
        except requests.exceptions.RequestException as e:
            continue
    return websites_info
