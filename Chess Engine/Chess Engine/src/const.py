# ============================================================
# Core Engine Constants
# ============================================================

# Screen dimensions
WIDTH = 1080
HEIGHT = 1080

# Board dimensions
ROWS = 8
COLS = 8

# Size of each square in pixels
SQSIZE = WIDTH // COLS

# Frames per second (for smooth dragging & animations)
FPS = 50


# ============================================================
# Asset Paths
# ============================================================

# Base asset directory
ASSETS_DIR = "assets"

# Piece images
PIECE_DIR = f"{ASSETS_DIR}/images"

# Sound effects
SOUND_DIR = f"{ASSETS_DIR}/sounds"


# ============================================================
# Game Settings
# ============================================================

# Default player colors
WHITE = "white"
BLACK = "black"

# AI settings
AI_COLOR = BLACK
AI_DEPTH = 2   # safe default depth


# ============================================================
# Board Index Helpers
# ============================================================

# Column labels (a–h)
COL_LABELS = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Row labels (1–8)
ROW_LABELS = ["1", "2", "3", "4", "5", "6", "7", "8"]


# ============================================================
# UI Settings
# ============================================================

# Hover outline color
HOVER_COLOR = (180, 180, 180)
