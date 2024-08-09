import requests
from bs4 import BeautifulSoup

def print_grid_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    lines = text.split('\n')
    character_positions = []
    for line in lines:
        if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            parts = line.split()
            if len(parts) == 3:
                x, char, y = parts
                character_positions.append((int(x), int(y), char))
    
    max_x = max(pos[0] for pos in character_positions)
    max_y = max(pos[1] for pos in character_positions)
    
    grid = [[' ' for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    
    for x, y, char in character_positions:
        grid[x][y] = char
    
    for row in grid:
        print(''.join(row))
#This is a test on the example url given in the question to check if the code runs:
url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
print_grid_from_url(url)