notes = """
events
 - location (x,y)
 - incident
 - skills required
 - progression offered
  - chosen from nearby events
"""

import random

class GameMap:
    def __init__(self, name, width=10, height=10):
        self.name = name
        self.width = width
        self.height = height
        self.hotspots = []
    
    def populate_hotspots(self, amount):
        for zone in range(1, amount+1):
            set_x = random.randint(1, self.width)
            set_y = random.randint(1, self.height)
            set_title = f"[{str(set_x)}, {str(set_y)}]_Hotspot"
            zone = Hotspot(set_title, set_x, set_y)
            self.hotspots.append(zone)
    
    def list_hotspots(self):
        print(f"There are currently {len(self.hotspots)} hotspots in {self.name}.")
        for hotspot in self.hotspots:
            print(self.hotspots.__repr__())
    
    def targeting_list(self):
        y_target_dict = dict()
        for y in range(1, self.height+1):
            y_target_dict[y] = []
            for hotspot in self.hotspots:
                coords = hotspot.coordinates()
                if coords[1] == y:
                    y_target_dict[y].append(coords[0])
        return y_target_dict
    
    def render_map(self):
        x_axis = range(1,self.width+1)
        y_axis = range(1,self.height+1)
        
        hs_locations = []
        for point in self.hotspots:
            hs_locations.append([point.x_coord, point.y_coord])
        
        top_axis = "____|"
        
        def render_header(number):
            if number < 10:
                return f"__{number}_|"
            else:
                return f"_{number}_|"
        
        for x in x_axis:
            top_axis += render_header(x)
        print(top_axis)
        
        grid_component = "    ."
        hs_component = "    %"
        
        side_axis = ""
        hotspot_locations = self.targeting_list()
        for y in y_axis:
            side_axis = render_header(y)
            for x in range(1, self.width+1):
                if x in hotspot_locations[y]:
                    side_axis += hs_component
                else:
                    side_axis += grid_component
            print(side_axis)

# Render Map Psuedo-Code
# make dictionary with 20 keys and each key's value is a list of x-axis locations needing a hotspot indicator. 
# for step in y-axis print x-width markers if current x in dictionary[y-step] print alternative marker





class Hotspot:
    def __init__(self, title, x_coord, y_coord):
        self.title = title
        self.x_coord = x_coord
        self.y_coord = y_coord
    
    def __repr__(self):
        rep = f"Hotspot: {self.title} at [{self.x_coord}, {self.y_coord}]."
        return rep
        
    def travel(self, x_move=0, y_move=0):
        self.x_coord += x_move
        self.y_coord += y_move
    
    def move(self, new_x_coord, new_y_coord):
        self.x_coord = new_x_coord
        self.y_coord = new_y_coord
    
    def locate(self):
        print(f"{self.title} can be found at [{self.x_coord}, {self.y_coord}].")
    
    def coordinates(self):
        return [self.x_coord, self.y_coord]

Wynnum = GameMap("Finding the academy", 20, 20)

Wynnum.populate_hotspots(10)

print("\n", Wynnum.targeting_list(), "\n\n")

Wynnum.render_map()