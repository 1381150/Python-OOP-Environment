import sys
sys.path.append("..")

from models.notes import Note
from service.noteservice import NoteService
from models.graph import Graph
from models.writer import Writer

class NoteController: 
    def __init__(self):
        self.note_service = NoteService()
        self.graph = Graph()
        self.writer = Writer("Default Writer")

    def create_note(self, title):
        self.note_service.addNewNote(title)

    def delete_note(self, note_id):
        self.note_service.deleteNote(note_id)

    def edit_note(self, note_id, text):
        self.note_service.editNote(note_id, text)

    def search_note_by_title(self, title):
        return self.note_service.searchNotebyTitle(title)

    def get_all_notes(self):
        return self.note_service.getAllNotes()

    def add_link(self, source_id, destination_id):
        self.graph.add_link(source_id, destination_id)

    def remove_link(self, source_id, destination_id):
        self.graph.remove_link(source_id, destination_id)

    def print_links(self):
        self.graph.print_links()

    def get_Note_By_Id(self, note_id):
        return self.note_service.getNotebyId(note_id)