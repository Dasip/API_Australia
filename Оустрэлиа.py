from mymapapi import show_map

def main():
    map_locations = 'll=135.746181,-27.483765&spn=20,20'
    map_type = 'sat'
    map_param = ''
    show_map(map_locations, map_type, map_param)
    
if __name__ == '__main__':
    main()