import pygame
from pygame.sprite import Group
from settings import Settings
from paimon import Paimon
import game_functions as gf
from game_stats import GameStats 
from button import Button 
from scoreboard import Scoreboard
#TODO add possibility to shoot down if slimes are under paimon

def run_game():

	pygame.init()
	slime_settings = Settings()
	screen = pygame.display.set_mode((slime_settings.screen_width, slime_settings.screen_height))
	pygame.display.set_caption("Slimes rainfall!")
	play = Button(slime_settings, screen, "Play")
	stats = GameStats(slime_settings)
	sb = Scoreboard(slime_settings, screen, stats)
	paimon = Paimon(screen, slime_settings)
	slimes = Group()
	bullets = Group()
	gf.create_army(slime_settings, screen, paimon, slimes)

	while True:
		gf.check_events(slime_settings, screen, paimon, bullets, stats, play, slimes)
		if stats.game_active:
			paimon.update()
			gf.update_bullets(bullets, slimes, slime_settings, paimon, screen, sb, stats)
			gf.update_slimes(slime_settings, slimes, paimon, stats, screen, bullets)
		gf.update_screen(slime_settings, screen, paimon, slimes, bullets,stats, play, sb)

run_game()