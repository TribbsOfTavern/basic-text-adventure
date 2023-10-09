###
#   Text Adventure
#   Written on stream @ twitch.tv/CodeNameTribbs
# 
#

class Item():
    """
        Item object, can moved from inventory to inventory, can interact with other objects.
    """
    def __init__(self, name:str="", description:str=""):
        self.name = name
        self.description = description
     
    def inspect(self):
        if (self.name is not None or self.name != "" ) and (
            self.description is not None or self.description != ""):
            print(f"You take a closer look at {self.name}.\n{self.description}")

class Player():
    """
        Player object. Keeps track of player information such as location and inventory.
    """
    def __init__(self, name:str="", inventory:list[Item]=[]):
        self.inventory = []
        self.name = None
        self.location = None
    
    def addItem(self, item:Item=None):
        if item is not None:
            self.inventory.append(item)
        
    def removeItem(self, item:Item=None):
        if item is not None:
            for i, obj in enumerate(self.inventory):
                if obj == item:
                    self.inventory.pop(i)
                    break

    def isItemInInventory(self, item_name:str=""):
        if self.inventory:
            for i, item in enumerate(self.inventory):
                if item_name.lower() == item.name.lower():
                    return True
            return False
        return False
    
    def setName(self, name:str=""):
        if name:
            self.name = name
        else:
            self.name = "Noname"

    def setLocation(self, room=None):
        self.location = room
    
class Door():
    """
        Door object to move player from room to room with a linked class Room. Can be locked or unlocked. 
    """
    def __init__(self, name:str="", linked_room=None, locked:bool=False, lock_item:Item=None, description:str=""):
        self.name = name
        self.description = description
        self.is_locked = locked
        self.linked_room = linked_room
        self.linked_door = None
        self.lock_item = lock_item
        
    def inspect(self):
        print(f"You take a closer look at the {self.name}.\n{self.description}")    
    
    def use(self, player:Player=None):
        if not self.is_locked and self.linked_room:
            player.location = self.linked_room
            print(f"You enter the room.")
        else:
            print(f"This door seems to be locked.")

    def linkDoor(self, door=None):
        self.linked_door = door
    
    def setLockItem(self, item=None):
        if item is not None:
            self.lock_item = item
    
    def interaction(self, item:Item=None):
        if item is not None:
            if item == self.lock_item:
                if self.is_locked: self.is_locked = False
                else: self.is_locked = True

                if self.linked_door != None:
                    self.linked_door.is_locked = self.is_locked
                
                if self.is_locked:
                    print(f"You used {self.lock_item.name} to lock {self.name}.")
                if not self.is_locked:
                    print(f"You used {self.lock_item.name} to unlock {self.name}")
            else:
                print("This might be the wrong item for the job.")
        else: 
            print("You must find an item like a key to unlock or lock a door.")
                
class Room():
    """
        Room object for a player to move into. Contains an list of class Item, and doors or class Door
    """
    def __init__(self, name:str="", description:str=""):
        self.name = name
        self.inventory = []
        self.description = description
        self.doors = []
        
    def addItem(self, item:Item=None):
        if item:
            self.inventory.append(item)
        
    def removeItem(self, item:Item=None):
        if item in self.inventory:
            self.inventory.remove(item)

    def addDoor(self, door:Door=None):
        self.doors.append(door)
    
    def removeDoor(self, door:Door=None):
        if door in self.doors:
            self.doors.remove(door)
    
    def inspect(self):
        print(f"You take a look at your surrounding.\n{self.description}")
        
    def search(self):
        if self.inventory or self.doors:
            text_doors = ""
            for i, d in enumerate(self.doors):
                text_doors += f"[{d.name}]"
            text_items = ""
            for i, e in enumerate(self.inventory):
                text_items += f"[{e.name}]"
            print(f"Searching around the room...")
            if text_items != "": print(f"You find {text_items}")
            if text_doors != "": print(f"Exits: {text_doors}")
        else:
            print(f"You search the room for a while, but there seems to be nothin of interest.")
            
class Clock():
    """
        Clock object that will tick in intervals until it has met its stop point.
        Glorified timer.
    """
    def __init__(self, start:float=0.0, stop:float=0.0, tick:float=0.0):
        self.start = start
        self.stop = stop
        self.tick = tick
        self.current = start
        self.is_alive = True

    def update(self):
        if self.is_alive:
            self.current += self.tick
            if self.current >= self.stop:
                self.is_alive = False
            
    def getTimeLeft(self) -> float:
        return self.stop - self.current

def parseCommands(ins:str, player:Player=None):
    if ' ' in ins:
        cmd, params = ins.split(' ', 1)
    else:
        cmd = ins

    if cmd == "use":
        if " on " in params:
            objA, objB = params.split(' on ')
            if player.isItemInInventory(objA):
                objA_found = False
                used_item = None
                for i, item in enumerate(player.inventory):
                    if objA == item.name.lower(): used_item = item
                    objA_found = True
                    break
                if objA_found:
                    curr_room = player.location
                    for i, door in enumerate(curr_room.doors):
                        if objB == door.name.lower():
                            door.interaction(used_item)
        else:
            curr_room = player.location
            for i, door in enumerate(curr_room.doors):
                if params == door.name.lower():
                    door.use(player)
                    break
        return
    # --------
    if cmd == "search":
        player.location.search()
        return
    # --------
    if cmd == "pickup":
        obj = params
        curr_room = player.location
        found = False
        for i, item in enumerate(curr_room.inventory):
            if obj == item.name.lower():
                player.inventory.append(item)
                curr_room.inventory.pop(i)
                found = True
                print(f"You added {params} to your inventory.")
                break
        if not found:
            print(f"You attempt to pick up {params} but it doesn't exist.")
        return
    # --------
    if cmd == "drop":
        obj = params
        curr_room = player.location
        found = False
        for i, item in enumerate(player.inventory):
            if obj == item.name.lower():
                curr_room.inventory.append(item)
                player.inventory.pop(i)
                found = True
                print(f"You dropped {params[1]}.")
                break
        if not found:
            print(f"You are not carrying {params[1]}.")
        return
    # --------
    if cmd == "inspect":
        obj = params
        curr_room = player.location
        found = False
        for i, item in enumerate(player.inventory):
            if obj == item.name.lower():
                found = True
                print(f"You take a closer look at {item.name}\n.{item.description}")
                break
        if not found:
            for i, item in enumerate(curr_room.inventory):
                if obj == item.name.lower():
                    found = True
                    print(f"You take a closer look at {item.name}.\n{item.description}")
                    break
        if not found:
            for i, item in enumerate(curr_room.doors):
                if obj == item.name.lower():
                    found = True
                    print(f"You take a closer look at he door.\n {item.description}")
                    break
        if not found:
            print("You can't inspect what isn't there.")
        return
    # --------
    if cmd == "check":
        if params == "clock":
            print(f"You only have {game_clock.getTimeLeft()} time left.")
        if params == "inventory":
            if player.inventory and player.inventory != []:
                print(f"Current inventory")
                text = ""
                for i, item in enumerate(player.inventory):
                    if i % 3 == 0: text += "\n"
                    text += f"[{item.name}]"
                print(text)
            else:
                print(f"You don't have anything in your inventory.")
        return
    # --------

if __name__ == "__main__":
    ###
    #   Setting up the adventure
    #
    
    #
    #   Adventure: Player starts in a room with a locked door they need to find the key for. If they find the key before
    #   the clock runs out, then they have escaped and won. Else it's game over as the rooms collapse.
    #
    
    ###
    # Rooms
    #
    room_1 = Room(
        name= "Room 1",
        description= "It's damp, the quickly carved room reminds you that this cave could come down at any time.",
    )
    room_2 = Room(
        name= "Room 2",
        description= "This room is already partially caved in. There could have been a route further in, but now there is just rubble everywhere."
    )
    room_3 = Room(
        name= "Room 3",
        description="This room is the best carved out. Looks like someone used this as a campsite at one point."
    )
    
    game_clock = Clock(start=6.00, stop=8.00, tick=0.25)
    
    room_1_s_door = Door(name="Exit", locked=True, linked_room=None, 
        description="An Iron barred door, too heavy and sturdy to move or break easily. There appears to be a lock on it.")
    room_1_n_door = Door(name="North Door", locked=False, linked_room=room_2,
        description = "A shabby wooden door leading into the north room.")
    room_1_w_door = Door(name="West Door", locked=False, linked_room=room_3,
        description = "A shabby wooden door leading into the west room.")
    room_2_s_door = Door(name="South Door", locked=False, linked_room=room_1,
        description= "A shabby wooden door leading into the south room.")
    room_3_e_door = Door(name="East Door", locked=False, linked_room=room_1, 
        description="A shabby wooden door leading into the east room.")
    
    room_1_n_door.linkDoor(room_2_s_door)
    room_2_s_door.linkDoor(room_1_n_door)
    room_1_w_door.linkDoor(room_3_e_door)
    room_3_e_door.linkDoor(room_1_w_door)
    
    item_key = Item(name="Key", description="A small rusted key.")
    item_stone = Item(name="Stick", description="It's a stick.")
    
    room_1.addDoor(room_1_s_door)
    room_1.addDoor(room_1_n_door)
    room_1.addDoor(room_1_w_door)
    room_2.addDoor(room_2_s_door)
    room_3.addDoor(room_3_e_door)
    
    room_3.addItem(item_stone)
    room_2.addItem(item_key)
    
    room_1_s_door.setLockItem(item_key)
    
    ###
    # Player Setup
    #
    player = Player()
    escaped = False
    
    print(f"{'Cave Escape':^10}")
    msg = """
        You have found youself locked in a cavern room.
        Find a way to escape before time runs out!
    """
    print(msg)
    # Get the players name.
    print("What is your name? ", end="")
    inp_name = input()
    player.setName(inp_name)
    player.setLocation(room_1)
    
    # Entering game loop
    while game_clock.is_alive:
        print(f"You are in room [{player.location.name}] with {game_clock.getTimeLeft()} time left.")
        print("""
    What would you like to do now?
    [use <object>]     [pickup <object>]
    [drop <object>]    [inspect <object>]
    [check inventory]   [check clock]
        """)
        print("? ", end="")
        inp = input()
        parseCommands(inp, player)
        
        game_clock.update()
        if not room_1_s_door.is_locked:
            escaped = True
            break
        
    if escaped:
        print(f"Congratulations, {player.name}, you've made it out this time.")
    else:
        print(f"In your desperate search, you can feel the room shake, something gives way.\n",
              "The sound of of rubble against the Iron bound door can be heard.\n",
              "Your heart sinks as you realized whatever hope behind that door has been seal.\n",
              "You are trapped here.\n",
              "Game over.")
    exit()