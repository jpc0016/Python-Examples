# CH16 Example
#
# americas.py
#
# Building a world map
#
from pygal.maps.world import World

wm = World()

wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# Open svg file with firefox or other web browser
wm.render_to_file('americas.svg')
