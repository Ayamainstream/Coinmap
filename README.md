# Coinmap
Coinmarketcap.com provides all the latest information about various cryptocurrencies in the market. It is collecting all the related news about different cryptocurrencies. 
## Installation
### Requirements 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests.
```bash
pip install requests
```
### Clone repository
Then install script by clonning repository.
```bash
git clone https://github.com/Ayamainstream/Coinmap.git
cd Coinmap
```
### Edit path in the script
Provide proper path to the file where data will be saved. You need to edit test.py file. In my case it is:
```python
sys.path.insert(0, '/Users/ayaze/Projects/Assignment2/src')
```
## Usage
```python
from coinmap import coin
scrapper = coin()
```
## Examples
Method of the Coin class should receive as a parameter the cryptocurrency name.
```python
news = scrapper.get_data("bitcoin")
print(news)
```
As an output this function provide a list of 12 news paragraphs with url from coinmarketcap.com.
```bash
[["BTC/USD Tests 56379 Technical Resistance:  Sally Ho's Technical Analysis 11 October 2021 BTC", 'Advertisement', 'Advertisement', 'Bitcoin ( BTC/USD ) continued to remain rangebound early in the North American session as the pair attracted strong two-way trading activity above the 54000 figure after recently peaking around the 56113 level , its strongest print following its acute decline in May.],[...],[...]...
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
