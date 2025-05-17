
from mcp.server.fastmcp import FastMCP
import os

# mcp = FastMCP("Demo")


# @mcp.tool()       
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b


# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

mcp =  FastMCP("notes")

FILELOC = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(FILELOC):
        with open(FILELOC, "w") as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a note to the notes file

    args:
        message(str): the content to be added
    returns:
        str: confirmation message
    """
    ensure_file()
    with open(FILELOC, "a") as f:
        f.write(message+ "\n")
    return "saved"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the notes file

    returns:
        All notes as a single string separated by line breaks.
        If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(FILELOC, "r") as f:
        content = f.read().strip()
    return content or "no notes yet"

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    get the most recently added note from the sticky note file.

    returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(FILELOC, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

    

if __name__ == "__main__":
    mcp.run()
