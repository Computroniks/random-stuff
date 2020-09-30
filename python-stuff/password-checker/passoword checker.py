try:
    0/0
    import tkinter as tk
    from tkinter import messagebox
    import json, sys, os, hashlib, binascii
    #See for hashing + salts
    #https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
    class passwdUtils:
        def __init__(self):
            try:
                with open('users.json') as json_file:
                    self.database = json.load(json_file)
            except FileNotFoundError:
                self.database = {}
                with open('users.json', 'w') as outfile:
                    json.dump(self.database, outfile)
        def addPasswd(self, username, passwd):
            self.username = username
            self.passwd = passwd
            self.salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            self.pwdhash = hashlib.pbkdf2_hmac('sha512', self.passwd.encode('utf-8'), self.salt, 100000)
            self.pwdhash = binascii.hexlify(self.pwdhash)
            self.database[self.username] =  (self.salt + self.pwdhash).decode('ascii')
            with open('users.json', 'w') as outfile:
                json.dump(self.database, outfile)
        def verifyPasswd(self, username, inputPasswd):
            try:
                self.storedPasswd = self.database[username]
            except KeyError:
                return False
            self.inputPasswd = inputPasswd
            self.salt = self.storedPasswd[:64]
            self.storedPasswd = self.storedPasswd[64:]
            self.pwdhash = hashlib.pbkdf2_hmac('sha512', self.inputPasswd.encode('utf-8'), self.salt.encode('ascii'), 100000)
            self.pwdhash = binascii.hexlify(self.pwdhash).decode('ascii')
            return self.pwdhash == self.storedPasswd
    class Gui(passwdUtils):
        def __init__(self):
            super().__init__()
            self.root = tk.Tk()
            self.root.title('Password Utils')
            self.root.geometry(('300x200'))
    if __name__ == '__main__':
        app = Gui()
except Exception as e:
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 0)
    



 
