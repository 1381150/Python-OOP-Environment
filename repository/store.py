import path 
import sys

sys.path.append("..")

from models.notes import Note

class Store:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def removeNote(self, note: Note):
        self.notes.remove(note)