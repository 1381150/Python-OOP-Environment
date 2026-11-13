import sys

sys.path.append("..")   

from models.notes import Note
from models.graph import Graph
from modeles.writer import Writer
from repository.store import Store

class NoteService:

    note_id = 0

    def __init__(self):
        self.store = Store()
    
    def addNewNote(self, title):
        self.note_id += 1
        note = Note(title, self.note_id)
        self.store.add_note(note) 

    def deleteNote(self, note_id):
        note_to_delete = None
        for note in self.store.get_notes():
            if note.id == note_id:
                note_to_delete = note
                break
        if note_to_delete:
            self.store.remove_note(note_to_delete)
        else:
            raise Exception(f"Note with ID {note_id} not found.") 

    def getNotebyId(self, note_id):
        for note in self.store.get_notes():
            if note.id == note_id:
                return note
        raise Exception(f"Note with ID {note_id} not found.")

    def editNote(self, note_id, text):
        note = self.getNotebyId(note_id)
        note.edit(text)