# 🧠 MCP Notes Server

This repository contains a simple **FastMCP** server implementation created as part of my learning and exploration of the **MCP (Model Control Plane)** ecosystem.

## 📦 What's Inside

- `main.py`: Core FastMCP app that:
  - Exposes tools to add and read notes.
  - Provides a resource for the latest note.
  - Includes a prompt for summarizing all notes.

- `notes.txt`: File used to store note entries (automatically created if missing).

- `.mcp/config.json`: Configuration file to register this server with the MCP runtime.

## 🚀 Features

- `add_note`: Save a note.
- `read_notes`: Read all saved notes.
- `get_latest_note`: Fetch the most recent note.
- `note_summary_prompt`: Generates a prompt to summarize all notes.

## 🛠 Usage

Make sure you have [uv](https://github.com/astral-sh/uv) and the required MCP dependencies installed.

Then you can start the server using:

```bash
uv --directory /path/to/project run main.py
