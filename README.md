📌 Overview
The Bonnyrigg Chess Engine is a complete chess application featuring:

Drag‑and‑drop piece movement

Full legal move generation

Special rule support (castling, en passant, promotion)

Move highlighting & last‑move tracing

Multiple board themes

Sound effects

Clean object‑oriented architecture

This project was developed as part of the HSC Software Engineering Major Project.

🎯 Features
Intuitive drag‑and‑drop interface

Real‑time move highlighting

Hover and last‑move indicators

Accurate rule enforcement

Multiple colour themes

Move & capture sound effects

Modular, maintainable code structure

🧠 System Architecture
The engine follows a layered architecture:

Code
Player Input
     ↓
GUI (game.py)
     ↓
Game Controller
     ↓
Board Logic (board.py)
     ↓
Move Validator
     ↓
Piece / Square / Move Classes
     ↓
Updated Display
📁 Project Structure
Code
ChessEngine/
│
├── assets/
│   ├── images/
│   └── sounds/
│
├── board.py
├── piece.py
├── square.py
├── move.py
├── dragger.py
├── game.py
├── main.py
├── config.py
├── theme.py
├── color.py
├── sound.py
└── const.py
Each module has a single responsibility, making the project easy to extend.

🛠️ Technologies Used
Python 3.x – main programming language

Pygame – rendering, input, sound

VS Code – development environment

GitHub – version control

🚀 Installation & Setup
1. Clone the repository
bash
git clone https://github.com/your-username/chess-engine.git
cd chess-engine
2. Install dependencies
bash
pip install pygame
3. Run the game
bash
python main.py
🎮 Controls
Action	Input
Move piece	Drag with mouse
Change theme	Press T
Reset game	Press R
Quit	Close window


📚 Code Highlights
Object‑Oriented Design
Piece subclasses: Pawn, Knight, Bishop, Rook, Queen, King

Square class for board cells

Move class for move representation

Board class for rule enforcement

Game class for rendering & interaction

Dragger class for drag‑and‑drop logic

Special Rules Implemented
Castling

En passant

Pawn promotion

Check detection

🧪 Testing
The engine was tested for:

Legal/illegal moves

Special rules

Edge cases (check, stalemate positions)

Drag‑and‑drop behaviour

Performance (FPS stability)

Theme visibility

📈 Future Improvements
AI opponent (minimax)

PGN export

Move history panel

Timer for competitive play

Online multiplayer

Animations & sound variations

Explore improvements:

AI Opponent

Move History

PGN Export

👤 Author
Danny Trieu Nguyen  
HSC Software Engineering Major Project

📎 License
This project is open‑source under the MIT License.
