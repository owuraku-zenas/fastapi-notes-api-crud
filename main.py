from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from notes_service import NotesService
from db import engine
from schemas import NoteModel, NoteCreateModel
from typing import List
from models import Note
import uuid
from http import HTTPStatus

app = FastAPI(
    title="Note API",
    description="A simple example",
    docs_url="/"
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
notesService = NotesService()

@app.get("/test")
def healthCheck():
    return "Web Service is up"

@app.get("/api/notes", response_model=List[NoteModel])
async def get_all_notes():
    notes = await notesService.get_all(session)
    return notes

@app.post("/api/notes", status_code=HTTPStatus.CREATED)
async def create_note(note_data: NoteCreateModel):
    new_note = Note(
        id = str(uuid.uuid4()),
        title = note_data.title,
        content = note_data.content
    )

    note = await notesService.add(session, new_note)

    return note

@app.get("/api/notes/{note_id}")
async def get_note_by_id(note_id: str):
    note = await notesService.get_by_id(session, note_id)

    return note

@app.put("/api/notes/{note_id}")
async def update_note(note_id: str, data: NoteCreateModel):
    note = await notesService.update(session, note_id, data={
        'title': data.title,
        'content': data.content
    })

    return note

@app.delete("/api/notes/{note_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_note(note_id: str):
    note = await notesService.get_by_id(session, note_id)
    await notesService.delete(session, note)

