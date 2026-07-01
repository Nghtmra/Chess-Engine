# Imports
import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move

class Main:
    # Main application class: initializes pygame, window, and game controller
    def __init__(self):
        pygame.init()
        
        # Create the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')

        # Game object handles board, turns, sounds, and rendering
        self.game = Game()

    def mainloop(self):
        # Local references for cleaner code
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        # Main game loop
        while True:
            # Show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            # If dragging a piece, draw it on top
            if dragger.dragging:
                dragger.update_blit(screen)

            # Events
            for event in pygame.event.get():
                # Mouse button down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    # Check if clicked square contains a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        
                        # Only allow dragging if piece belongs to current player
                        if piece.color == game.next_player:

                            # Calculate legal moves for this piece
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)

                            # Begin dragging
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)

                            # Redraw board while dragging
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    # Highlight hovered square
                    game.set_hover(motion_row, motion_col)

                    # If dragging, update piece position and redraw
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        # Show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # Mouse button up
                elif event.type == pygame.MOUSEBUTTONUP:

                    # If a piece was being dragged, attempt to drop it
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # Create move object from initial → final square
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # Check if move is legal
                        if board.valid_move(dragger.piece, move):

                            # Check if capturing a piece
                            captured = board.squares[released_row][released_col].has_piece()

                            # Execute the move
                            board.move(dragger.piece, move)

                            # Handle en passant flags
                            board.set_true_en_passant(dragger.piece)  

                            # Play move or capture sound
                            game.play_sound(captured)

                            # Redraw board after move
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)

                            # Switch turns
                            game.next_turn()

                    # Stop dragging regardless of move validity
                    dragger.undrag_piece()

                # Key presses
                elif event.type == pygame.KEYDOWN:

                    # Changing theme
                    if event.key == pygame.K_t:
                        game.change_theme()

                     # Reset game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # Quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update the display every frame
            pygame.display.update()

# Start the game         
main = Main()
main.mainloop()