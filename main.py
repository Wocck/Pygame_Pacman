from game import Game
'''
Just initializing game and setting while running loop
'''

g = Game()
g.intro_screen(False)
g.new()
while g.running:
    g.main()
    g.game_over()
