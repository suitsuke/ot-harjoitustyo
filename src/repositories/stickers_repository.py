class StickersRepository:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def find_by_user(self, username):
        #finds a list of stickers aqcuired by user and returns their id:s in a list
        list = []
        
        #todo
        return list
    
    def add_sticker(self, username, sticker):
        #adds sticker ownership to a user if they don't already have it
        pass

    def remove_sticker(self, username, sticker):
        #removes sticker ownership from a user (if they own it)
        pass

    def check_ownership(self, username, sticker):
        #checks if a user has a sticker or not
        #returns True if user has sticker, returns False if they don't

        pass
    
