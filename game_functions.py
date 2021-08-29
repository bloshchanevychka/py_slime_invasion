import sys
import pygame
from bullet import Bullet
from slime import Slime
from time import sleep

def check_events(slime_settings, screen, paimon, bullets, stats, play, slimes):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				#print(event.key)
				check_keydown_events(event, slime_settings, screen, paimon, bullets, stats,  slimes)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,paimon)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(slime_settings, screen, stats, play, slimes, bullets, paimon, mouse_x, mouse_y)

def check_keydown_events(event, slime_settings, screen, paimon, bullets, stats,  slimes):
	if event.key == pygame.K_RIGHT:
		paimon.moving_right = True
	elif event.key == pygame.K_LEFT:
		paimon.moving_left = True
	elif event.key == pygame.K_UP:
		paimon.moving_up = True
	elif event.key == pygame.K_DOWN:
		paimon.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(slime_settings, screen, paimon, bullets)
	elif event.key == pygame.K_q:
		sys.exit()	
	elif event.key == pygame.K_p:
		start_game(slime_settings, screen, stats,  slimes, bullets, paimon)


def check_keyup_events(event, paimon):
	if event.key == pygame.K_RIGHT:
		paimon.moving_right = False
	elif event.key == pygame.K_LEFT:
		paimon.moving_left = False
	elif event.key == pygame.K_UP:
		paimon.moving_up = False
	elif event.key == pygame.K_DOWN:
		paimon.moving_down = False


def update_screen(slime_settings, screen, paimon, slimes, bullets, stats, play, sb):


	screen.fill(slime_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	paimon.blitme()
	#slime.blitme()
	for slime in slimes.sprites():
		slime.blitme()
	sb.show_score()
	if not stats.game_active:
		play.draw_button()
	pygame.display.flip()


def update_bullets(bullets, slimes, slime_settings, paimon, screen, sb, stats):

	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
			#print(len(bullets))
	check_bullet_slime_collision(bullets, slimes, slime_settings, screen, paimon, sb, stats)


def update_slimes(slime_settings, slimes, paimon, stats, screen, bullets):
		check_army_edges(slime_settings, slimes)
		slimes.update()

		if pygame.sprite.spritecollideany(paimon, slimes):
			#print('Paimon is eaten!!!!!!!')
			paimon_omnomnom(slime_settings, paimon, slimes, stats, screen, bullets)
		check_slime_bottom(slime_settings, stats, screen, slimes, bullets, paimon)


def fire_bullet(slime_settings, screen, paimon, bullets):

	if len(bullets) < slime_settings.bullets_allowed:
		new_bullet = Bullet(slime_settings, screen, paimon)
		bullets.add(new_bullet)


def get_slime_num_len(slime_settings, slime_width):

	avaliable_space_x = slime_settings.screen_width - slime_width
	slimes_num = int(avaliable_space_x / (2 * slime_width))
	return slimes_num


def get_rows_num(slime_settings, paimon_height, slime_height):

	avaliable_space_y = slime_settings.screen_height - 2 * paimon_height - 3 * slime_height
	rows_num = int(avaliable_space_y / (2 * slime_height))
	return rows_num


def create_slime(slime_settings, screen, slimes, slime_num, rows_num):

	slime = Slime(slime_settings,screen)
	slime_width = slime.rect.width
	slime.x = 0.2 * slime_width + 2 * slime_width * slime_num
	slime.rect.x = slime.x
	slime.rect.y = slime.rect.height/4 + 2 * slime.rect.height * rows_num
	slimes.add(slime)


def create_army(slime_settings, screen, paimon, slimes):

	slime = Slime(slime_settings, screen)
	slime_width = slime.rect.width
	slimes_num_x = get_slime_num_len(slime_settings, slime_width)
	rows_num = get_rows_num(slime_settings, paimon.rect.height, slime.rect.height)

	for row in range(rows_num):
		for slime_i in range(slimes_num_x):
			create_slime(slime_settings, screen, slimes, slime_i, row)
			

def check_army_edges(slime_settings, slimes):
	for slime in slimes.sprites():
		if slime.check_edges():
			change_army_direction(slime_settings, slimes)
			break


def change_army_direction(slime_settings, slimes):
	for slime in slimes.sprites():
		slime.rect.y += slime_settings.army_drop_speed
	slime_settings.slimes_direction *= -1 


def check_bullet_slime_collision(bullets, slimes, slime_settings, screen, paimon, sb, stats):
	collisions = pygame.sprite.groupcollide(bullets, slimes, True, True)
	if collisions:

		for slimes in collisions.values():
			stats.score += slime_settings.slime_points * len(slimes)
			sb.prep_score()
		check_high_score(stats, sb)	
	if len(slimes) == 0:
		bullets.empty()
		slime_settings.increase_spead()
		create_army(slime_settings, screen, paimon, slimes)


def paimon_omnomnom(slime_settings, paimon, slimes, stats, screen, bullets):
	if stats.lifes_left >0:
		stats.lifes_left -=1
		slimes.empty()
		bullets.empty()
		create_army(slime_settings, screen, paimon, slimes)
		paimon.center_paimon()
		sleep(0.5)
	else: 
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_slime_bottom(slime_settings, stats, screen, slimes, bullets, paimon):

	screen_rect = screen.get_rect()
	for slime in slimes.sprites():
		if slime.rect.bottom >= screen_rect.bottom:
			paimon_omnomnom(slime_settings, paimon, slimes, stats, screen, bullets)
			break

def check_play_button(slime_settings, screen, stats, play, slimes, bullets, paimon, mouse_x, mouse_y):
	button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(slime_settings, screen, stats,  slimes, bullets, paimon)
		

def start_game(slime_settings, screen, stats,  slimes, bullets, paimon):
	slime_settings.initialize_dynamic_settings()
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	stats.game_active = True
	bullets.empty()
	slimes.empty()
	create_army(slime_settings, screen, paimon, slimes)
	paimon.center_paimon()


def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()