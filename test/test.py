import sys
sys.path.insert(0, '/Users/ayaze/Projects/Assignment2/src')

from coinmap import coin

scrapper = coin()
print(scrapper.get_data("bitcoin"))