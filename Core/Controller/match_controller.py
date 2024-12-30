#match_controller
MODE = {
    "advantage":"",
    "multiplayer":""
}
class match_controller:
    '''
    use to control everything in a match
    use control map, unit, weather
    '''
    map_data = []

    def __init__(self):
        return

    def load_match_data(self,match_data):
        self.map_data = match_data
        return


