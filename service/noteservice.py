import sys

sys.path.append("..")   

from models.notes import Note
from models.graph import Graph
from modeles.writer import Writer
from repository.store import Store

class NoteService:
    def __init__(self, note_repository):
        self.note_repository = note_repository

    def create_note(self, title, content):
        note = {
            'title': title,
            'content': content
        }
        return self.note_repository.save(note)

    def get_note_by_id(self, note_id):
        return self.note_repository.find_by_id(note_id)

    def update_note(self, note_id, title=None, content=None):
        note = self.note_repository.find_by_id(note_id)
        if not note:
            return None
        if title:
            note['title'] = title
        if content:
            note['content'] = content
        return self.note_repository.update(note)

    def delete_note(self, note_id):
        return self.note_repository.delete(note_id)