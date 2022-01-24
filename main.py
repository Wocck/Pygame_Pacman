from game import Game


g = Game()
g.intro_screen(False)
g.new()
while g.running:
    g.main()
    g.game_over()
