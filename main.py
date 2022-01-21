from game import Game


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
