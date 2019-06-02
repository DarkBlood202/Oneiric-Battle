def GameStart():
	import pygame, math, random

	WIDTH=640; HEIGHT=480; FPS=60; BLACK=(0,0,0); RED=(255,0,0); GRAY=(127,127,127)
	GREEN=(0,255,0); BLUE=(0,0,255); WHITE=(255,255,255); FULLSCREEN=False

	def load_sprite(image):
		img=pygame.image.load('data/img/'+ image)
		return img

	def load_sound(sound):
		snd=pygame.mixer.Sound('data/sfx/'+sound)
		return snd

	def strip_from_sheet(sheet, start, size, columns, rows=1):
		sprites_list=[]
		for j in range(rows):
			for i in range(columns):
				location=(start[0]+size[0]*i,start[1]+size[1]*j)
				sprites_list.append(sheet.subsurface(pygame.Rect(location, size)))
		return sprites_list

	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init()
	pygame.init()
	pygame.display.set_caption('Oneiric Battle!')
	icon=load_sprite('icon.png'); pygame.display.set_icon(icon)
	if not FULLSCREEN:	screen=pygame.display.set_mode((WIDTH,HEIGHT))
	else:	screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
	clock=pygame.time.Clock()

	#load gui
	gui_main=pygame.image.load('data/gui/main.png').convert(); gui_main_rect=gui_main.get_rect()
	gui_cursor=pygame.image.load('data/gui/cursor.png').convert_alpha(); gui_warning=pygame.image.load('data/gui/gui_warning.png').convert_alpha()
	gui_cursor_p1=pygame.image.load('data/gui/gui_cursor_p1.png').convert(); gui_cursor_p1.set_colorkey(BLACK)
	gui_cursor_p2=pygame.image.load('data/gui/gui_cursor_p2.png').convert(); gui_cursor_p2.set_colorkey(BLACK)
	gui_select=pygame.image.load('data/gui/selection.png').convert_alpha(); gui_select_rect=gui_select.get_rect(center=(WIDTH//2,HEIGHT//2))
	gui_stage=pygame.image.load('data/gui/stage.png').convert_alpha()
	gui_lives=pygame.image.load('data/gui/gui_lives.png').convert(); gui_lives.set_colorkey(GREEN)

	#load player title
	gi_title=pygame.image.load('data/gui/gi_title.png').convert_alpha(); jm_title=pygame.image.load('data/gui/jm_title.png').convert_alpha()
	la_title=pygame.image.load('data/gui/la_title.png').convert_alpha(); zv_title=pygame.image.load('data/gui/zv_title.png').convert_alpha()
	dl_title=pygame.image.load('data/gui/dl_title.png').convert_alpha()

	#load gauge bar
	spr_bar=pygame.image.load('data/gui/bar.png').convert(); spr_bar.set_colorkey(BLACK); spr_bar_rect=spr_bar.get_rect()

	#load portraits
	port_gi=pygame.image.load('data/portraits/port_gi.png').convert_alpha(); port_gi_rect=port_gi.get_rect()
	port_jm=pygame.image.load('data/portraits/port_jm.png').convert_alpha(); port_jm_rect=port_jm.get_rect()
	port_la=pygame.image.load('data/portraits/port_la.png').convert_alpha(); port_la_rect=port_la.get_rect()
	port_zv=pygame.image.load('data/portraits/port_zv.png').convert_alpha(); port_zv_rect=port_zv.get_rect()
	port_dl=pygame.image.load('data/portraits/port_dl.png').convert_alpha(); port_dl_rect=port_dl.get_rect()

	#load general sprites
	spr_overlay=load_sprite('overlay.png').convert(); spr_overlay.set_colorkey(GREEN); spr_overlay_rect=spr_overlay.get_rect()
	spr_gi=load_sprite('spr_gi.png').convert_alpha(); spr_jm=load_sprite('spr_jm.png').convert_alpha()
	spr_la=load_sprite('spr_la.png').convert_alpha(); spr_zv=load_sprite('spr_zv.png').convert_alpha()
	spr_dl=load_sprite('spr_dl.png').convert_alpha()
	spr_laser=load_sprite('spr_la_ex_shot.png').convert(); spr_moon=load_sprite('spr_dl_ex_shot.png').convert_alpha()
	spr_laser_obj=load_sprite('spr_laser_obj.png').convert(); spr_laser_obj.set_colorkey(BLACK)
	spr_gi_ex_shot=load_sprite('spr_gi_ex_shot.png').convert(); spr_gi_ex_shot.set_colorkey(GREEN)
	spr_jm_ex_shot=load_sprite('spr_jm_ex_shot.png').convert_alpha()
	spr_smallstar=load_sprite('bullets/spr_smallstar.png').convert(); spr_smallstar.set_colorkey(BLACK)
	spr_bigstar=load_sprite('bullets/spr_bigstar.png').convert(); spr_bigstar.set_colorkey(BLACK)
	spr_magic_sign=load_sprite('spr_magic_sign.png').convert(); spr_magic_sign.set_colorkey(BLACK)
	spr_knife=load_sprite('bullets/spr_knife.png').convert(); spr_knife.set_colorkey(GREEN)
	spr_boss_gi=load_sprite('bosses/spr_boss_gi.png').convert_alpha(); spr_boss_la=load_sprite('bosses/spr_boss_la.png').convert_alpha()
	spr_boss_jm=load_sprite('bosses/spr_boss_jm.png').convert_alpha(); spr_boss_zv=load_sprite('bosses/spr_boss_zv.png').convert_alpha()
	spr_boss_dl=load_sprite('bosses/spr_boss_dl.png').convert_alpha()
	spr_gi_ex_atk=load_sprite('ex/spr_gi_ex_atk.png').convert(); spr_gi_ex_atk.set_colorkey(GREEN)
	spr_zv_ex_atk=load_sprite('ex/spr_zv_ex_atk.png').convert(); spr_zv_ex_atk.set_colorkey(BLACK)
	spr_hb=load_sprite('spr_hb.png').convert_alpha()
	spr_clean_bullet=load_sprite('spr_clean_bullet.png').convert_alpha()

	#loading sprite sheets
	sheet_dark_plasma=pygame.image.load('data/bck/dark_plasma.png').convert()
	sheet_particle_tunnel=pygame.image.load('data/bck/particle_tunnel.png').convert()
	sheet_shadow_machinery=pygame.image.load('data/bck/shadow_machinery.png').convert()
	sheet_red_capsule=pygame.image.load('data/bck/red_capsule.png').convert()
	sheet_tri_tunnel=pygame.image.load('data/bck/tri_tunnel.png').convert()
	sheet_time_tunnel=pygame.image.load('data/bck/time_tunnel.png').convert()

	sheet_smallbullet=load_sprite('bullets/spr_smallbullet.png').convert(); sheet_smallbullet.set_colorkey(BLACK)
	sheet_medbullet=load_sprite('bullets/spr_medbullet.png').convert(); sheet_medbullet.set_colorkey(BLACK)
	sheet_bigbullet=load_sprite('bullets/spr_bigbullet.png').convert(); sheet_bigbullet.set_colorkey(BLACK)
	sheet_ghostbullet=load_sprite('bullets/spr_ghostbullet.png').convert(); sheet_ghostbullet.set_colorkey(BLACK)

	sheet_shots=load_sprite('spr_shot.png').convert_alpha()
	sheet_enemy=load_sprite('spr_enemy.png').convert_alpha()
	sheet_explosion=load_sprite('spr_explosion.png').convert_alpha()
	sheet_zv_ex_shot=load_sprite('spr_zv_ex_shot.png').convert_alpha()
	sheet_dl_ex_atk=load_sprite('ex/spr_dl_ex_atk.png').convert_alpha()

	sheet_gui_effect=pygame.image.load('data/gui/gui_effect.png').convert()
	sheet_gui_boss_atk=pygame.image.load('data/gui/gui_boss_atk.png').convert_alpha()
	sheet_gui_round_end=pygame.image.load('data/gui/gui_round_end.png').convert_alpha()

	spr_jm_ex_atk=[]
	for i in range(2):
		img=load_sprite('ex/spr_jm_ex_atk_{}.png'.format(i)).convert_alpha()
		spr_jm_ex_atk.append(img)
	spr_fire_list=[]
	for i in range(2):
		img=load_sprite('spr_fire_{}.png'.format(i)).convert_alpha()
		spr_fire_list.append(img)

	#sprite sheets to sprites
	spr_shot=strip_from_sheet(sheet_shots,(0,0),(12,55),5)
	spr_enemy_list=strip_from_sheet(sheet_enemy,(0,0),(38,34),3)
	spr_explosion_list=strip_from_sheet(sheet_explosion,(0,0),(62,62),5)
	spr_smallbullet_list=strip_from_sheet(sheet_smallbullet,(0,0),(9,9),9)
	spr_medbullet_list=strip_from_sheet(sheet_medbullet,(0,0),(13,13),9)
	spr_bigbullet_list=strip_from_sheet(sheet_bigbullet,(0,0),(27,27),9)
	spr_ghostbullet=strip_from_sheet(sheet_ghostbullet,(0,0),(13,13),3)

	spr_zv_ex_shot=strip_from_sheet(sheet_zv_ex_shot,(0,0),(126,65),4)
	spr_dl_ex_atk=strip_from_sheet(sheet_dl_ex_atk,(0,0),(100,50),2,2)

	gui_effect=strip_from_sheet(sheet_gui_effect,(0,0),(288,84),5)
	gui_boss_atk=strip_from_sheet(sheet_gui_boss_atk,(0,0),(167,30),5)
	gui_round_end=strip_from_sheet(sheet_gui_round_end,(0,0),(274,133),2)

	#load backgrounds
	bck_dark_plasma_list=strip_from_sheet(sheet_dark_plasma,(0,0),(640,480),4,4)
	bck_shadow_machinery_list=strip_from_sheet(sheet_shadow_machinery,(0,0),(288,448),4,4)
	bck_red_capsule_list=strip_from_sheet(sheet_red_capsule,(0,0),(288,448),5,3)
	bck_particle_tunnel_list=strip_from_sheet(sheet_particle_tunnel,(0,0),(288,448),5,2)
	bck_time_tunnel_list=strip_from_sheet(sheet_time_tunnel,(0,0),(288,448),6,3)
	bck_tri_tunnel_list=strip_from_sheet(sheet_tri_tunnel,(0,0),(288,448),11)

	#load boss backgrounds
	bck_boss_gi_back=pygame.image.load('data/bck/bosses/back/gi_back.png').convert()
	bck_boss_la_back=pygame.image.load('data/bck/bosses/back/la_back.png').convert()
	bck_boss_jm_back=pygame.image.load('data/bck/bosses/back/jm_back.png').convert()
	bck_boss_zv_back=pygame.image.load('data/bck/bosses/back/zv_back.png').convert()
	bck_boss_dl_back=pygame.image.load('data/bck/bosses/back/dl_back.png').convert()

	#load boss foregrounds
	bck_boss_gi_front=pygame.image.load('data/bck/bosses/front/gi_front.png').convert_alpha()
	bck_boss_la_front=pygame.image.load('data/bck/bosses/front/la_front.png').convert(); bck_boss_la_front.set_colorkey(WHITE)
	bck_boss_jm_front=pygame.image.load('data/bck/bosses/front/jm_front.png').convert(); bck_boss_jm_front.set_colorkey(WHITE)
	bck_boss_zv_front=pygame.image.load('data/bck/bosses/front/zv_front.png').convert_alpha()
	bck_boss_dl_front=pygame.image.load('data/bck/bosses/front/dl_front.png').convert(); bck_boss_dl_front.set_colorkey(GREEN)
	bck_boss_dl_front_alpha=pygame.image.load('data/bck/bosses/front/dl_front_alpha.png').convert_alpha()

	#load sounds
	snd_hit=load_sound('snd_hit.ogg'); snd_hit.set_volume(0.25)
	snd_select=load_sound('snd_select.ogg')
	snd_start=load_sound('snd_start.ogg')
	snd_charged=load_sound('snd_charged.ogg'); snd_charged.set_volume(0.25)
	snd_backLaser=load_sound('snd_backLaser.ogg'); snd_backLaser.set_volume(0.5)
	snd_frontLaser=load_sound('snd_frontLaser.ogg'); snd_frontLaser.set_volume(0.5)
	snd_swordSlash=load_sound('snd_swordSlash.ogg')
	snd_effectRelease=load_sound('snd_effectRelease.ogg')
	snd_moon=load_sound('snd_moon.ogg'); snd_moon.set_volume(0.25)
	snd_knifeAppear=load_sound('snd_knifeAppear.ogg')
	snd_knifeStop=load_sound('snd_knifeStop.ogg')
	snd_knifeShoot=load_sound('snd_knifeShoot.ogg')
	snd_bullet=load_sound('snd_bullet.ogg')
	snd_bossDefeat=load_sound('snd_bossDefeat.ogg')
	snd_isCharging=load_sound('snd_isCharging.ogg')
	snd_fo=load_sound('snd_fo.ogg')
	snd_spiritual=load_sound('snd_spiritual.ogg')
	snd_gotHit=load_sound('snd_gotHit.ogg')
	snd_cross=load_sound('snd_cross.ogg')
	snd_recovery=load_sound('snd_recovery.ogg')
	snd_unchoose=load_sound('snd_unchoose.ogg')
	snd_getBonus=load_sound('snd_getBonus.ogg')

	snd_bossAttack=[]
	for i in range(4):
		snd=load_sound('snd_bossAttack_{}.ogg'.format(i))
		snd_bossAttack.append(snd)

	#define some functions
	def draw_ex_bar(surface,x,y,amount,maxamount,color=WHITE):
		BAR_LENGTH=255; BAR_HEIGHT=3
		fill = amount/maxamount*BAR_LENGTH
		fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
		pygame.draw.rect(surface,color,fill_rect)

	def draw_lives(surface,x,y,lives,img):
		for i in range(lives):
			img_rect=img.get_rect()
			img_rect.x=x+14*i
			img_rect.y=y
			surface.blit(img,img_rect)

	#define the classes
	class CONTROL:
		def __init__(self):
			self.screen=0
		def create_players(self,side,index):
			if not side:
				if index==0:	self.player_1=Player(0,0)
				elif index==1:	self.player_1=Player(0,1)
				elif index==2:	self.player_1=Player(0,2)
				elif index==3:	self.player_1=Player(0,3)
				elif index==4:	self.player_1=Player(0,4)
				all_sprites.add(self.player_1)
			else:
				if index==0:	self.player_2=Player(1,0)
				elif index==1:	self.player_2=Player(1,1)
				elif index==2:	self.player_2=Player(1,2)
				elif index==3:	self.player_2=Player(1,3)
				elif index==4:	self.player_2=Player(1,4)
				all_sprites.add(self.player_2)

	class MenuArrow(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image=gui_cursor; self.rect=self.image.get_rect()
			self.options=0
		def update(self):
			if self.options>2:	self.options=0
			if self.options<0:	self.options=2
			if self.options==0:	self.rect=(197,210)
			elif self.options==1:	self.rect=(197,258)
			elif self.options==2:	self.rect=(195,355)
		def enter(self):
			snd_start.play()
			if self.options==0:
				control.screen+=1; dark_plasma=Background(bck_dark_plasma_list); backgrounds.add(dark_plasma); self.kill()
			elif self.options==2: exit()

	class SelectionScreen:
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.player_1_index=0; self.player_2_index=0
			self.chooseStage=False; self.ready=False
		def update(self):
			if control.screen==1:
				if not self.ready:
					self.ready=True
					self.cursor1=CursorP1(203,157)
					self.cursor2=CursorP2(424,157)
				if self.cursor1.hasChosen and self.cursor2.hasChosen:
					if not self.chooseStage:
						self.stagecursor=StageCursor()
						self.chooseStage=True
		def start(self):
			self.testspawn=TestSpawn()
			self.cursor1.kill(); self.cursor2.kill()

	class CursorP1(pygame.sprite.Sprite):
		def __init__(self,x,y):
			pygame.sprite.Sprite.__init__(self); all_sprites.add(self)
			self.image=gui_cursor_p1; self.rect=self.image.get_rect(topleft=(x,y))
			self.options=0; self.hasChosen=False; self.update_timer=pygame.time.get_ticks()
		def update(self):
			if self.options==0:	screen.blit(port_gi,(0,0)); self.rect.y=145
			elif self.options==1:	screen.blit(port_la,(0,0)); self.rect.y=180
			elif self.options==2:	screen.blit(port_jm,(0,0)); self.rect.y=220
			elif self.options==3:	screen.blit(port_zv,(0,0)); self.rect.y=250
			elif self.options==4:	screen.blit(port_dl,(0,0)); self.rect.y=290
			if self.options>4:	self.options=0
			if self.options<0:	self.options=4
			now=pygame.time.get_ticks()
			if now-self.update_timer>100:
				self.update_timer=now
				keystate=pygame.key.get_pressed()
				if not self.hasChosen:
					if keystate[pygame.K_w]:	self.options-=1; snd_select.stop(); snd_select.play()
					if keystate[pygame.K_s]:	self.options+=1; snd_select.stop(); snd_select.play()
					if keystate[pygame.K_v]:	self.choose()
				else:
					if keystate[pygame.K_b]:	self.unchoose()
		def choose(self):
			snd_start.play()
			selection.player_1_index=self.options
			self.hasChosen=True
		def unchoose(self):
			snd_unchoose.play()
			self.hasChosen=False

	class CursorP2(pygame.sprite.Sprite):
		def __init__(self,x,y):
			pygame.sprite.Sprite.__init__(self); all_sprites.add(self)
			self.image=gui_cursor_p2; self.rect=self.image.get_rect(topright=(x,y))
			self.options=0; self.hasChosen=False; self.update_timer=pygame.time.get_ticks()
		def update(self):
			pgi=port_gi.get_rect(topright=(640,0))
			pla=port_la.get_rect(topright=(640,0))
			pjm=port_jm.get_rect(topright=(640,0))
			pzv=port_zv.get_rect(topright=(640,0))
			pdl=port_dl.get_rect(topright=(640,0))
			if self.options==0:	screen.blit(port_gi,pgi); self.rect.y=145
			elif self.options==1:	screen.blit(port_la,pla); self.rect.y=180
			elif self.options==2:	screen.blit(port_jm,pjm); self.rect.y=220
			elif self.options==3:	screen.blit(port_zv,pzv); self.rect.y=250
			elif self.options==4:	screen.blit(port_dl,pdl); self.rect.y=290
			if self.options>4:	self.options=0
			if self.options<0:	self.options=4
			now=pygame.time.get_ticks()
			if now-self.update_timer>100:
				self.update_timer=now
				keystate=pygame.key.get_pressed()
				if not self.hasChosen:
					if keystate[pygame.K_UP]:	self.options-=1; snd_select.stop(); snd_select.play()
					if keystate[pygame.K_DOWN]:	self.options+=1; snd_select.stop(); snd_select.play()
					if keystate[pygame.K_KP1]:	self.choose()
				else:
					if keystate[pygame.K_KP2]:	self.unchoose()
		def choose(self):
			snd_start.play()
			selection.player_2_index=self.options
			self.hasChosen=True
		def unchoose(self):
			snd_unchoose.play()
			self.hasChosen=False

	class StageCursor(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self); all_sprites.add(self)
			self.image=gui_stage; self.rect=self.image.get_rect(center=(WIDTH//2,HEIGHT//2))
			self.options=0; self.update_timer=pygame.time.get_ticks()
		def update(self):
			if self.options==0:	screen.blit(gui_cursor,(190,145))
			elif self.options==1:	screen.blit(gui_cursor,(190,180))
			elif self.options==2:	screen.blit(gui_cursor,(190,220))
			elif self.options==3:	screen.blit(gui_cursor,(190,250))
			elif self.options==4:	screen.blit(gui_cursor,(190,290))
			now=pygame.time.get_ticks()
			if now-self.update_timer>100:
				self.update_timer=now
				keystate=pygame.key.get_pressed()
				if keystate[pygame.K_UP] or keystate[pygame.K_w]:	self.options-=1; snd_select.stop(); snd_select.play()
				elif keystate[pygame.K_DOWN] or keystate[pygame.K_s]:	self.options+=1; snd_select.stop(); snd_select.play()
				elif keystate[pygame.K_RETURN]:
					self.stage_call(); selection.start(); control.screen=2; self.kill()
			if self.options>4:	self.options=0
			if self.options<0:	self.options=4
		def stage_call(self):
			snd_start.play()
			backgrounds.empty()
			if self.options==0:
				t_A=Background(bck_time_tunnel_list,'dreams.ogg',16,16,1.5); t_B=Background(bck_time_tunnel_list,None,336,16,1.5)
				backgrounds.add(t_A,t_B)
			elif self.options==1:
				s_m_A=Background(bck_shadow_machinery_list,'machinery.ogg',16,16); s_m_B=Background(bck_shadow_machinery_list,None,336,16)
				backgrounds.add(s_m_A,s_m_B)
			elif self.options==2:
				p_t_A=Background(bck_particle_tunnel_list,'bits.ogg',16,16); p_t_B=Background(bck_particle_tunnel_list,None,336,16)
				backgrounds.add(p_t_A,p_t_B)
			elif self.options==3:
				t_t_A=Background(bck_tri_tunnel_list,'rat.ogg',16,16,1.5); t_t_B=Background(bck_tri_tunnel_list,None,336,16,1.5)
				backgrounds.add(t_t_A,t_t_B)
			elif self.options==4:	
				red_A=Background(bck_red_capsule_list,'moon.ogg',16,16); red_B=Background(bck_red_capsule_list,None,336,16)
				backgrounds.add(red_A,red_B)
			control.create_players(0,selection.player_1_index); control.create_players(1,selection.player_2_index)

	class Player(pygame.sprite.Sprite):
		def __init__(self,side,index):
			pygame.sprite.Sprite.__init__(self); players.add(self); self.hp=5
			self.index=index; self.shot_delay=90; self.last_shot=pygame.time.get_ticks()
			if index==0:	self.image=spr_gi; self.speed=8; self.max_charge=200
			elif index==1:	self.image=spr_la; self.speed=4; self.max_charge=160
			elif index==2:	self.image=spr_jm; self.speed=5; self.max_charge=240
			elif index==3:	self.image=spr_zv; self.speed=6; self.max_charge=260
			elif index==4:	self.image=spr_dl; self.speed=5; self.max_charge=180
			self.mask=pygame.mask.from_surface(spr_hb)
			self.invulnerable_timer=pygame.time.get_ticks(); self.invulnerable=True
			self.side=side; self.orig_speed=self.speed; self.radius=1; self.slow=False
			self.rect=self.image.get_rect(); self.charge=0; self.maxed=False; self.available=int(self.max_charge/4)+1
			if not side:
				self.rect.center=(143,430); self.left_limit=16; self.right_limit=303
				self.key_left=pygame.K_a; self.key_right=pygame.K_d; self.key_up=pygame.K_w; self.key_down=pygame.K_s
				self.key_shoot=pygame.K_v; self.key_charge=pygame.K_b; self.bar_x=32; self.key_slow=pygame.K_c
			else:
				self.rect.center=(479,430); self.left_limit=336; self.right_limit=623
				self.key_left=pygame.K_LEFT; self.key_right=pygame.K_RIGHT; self.key_up=pygame.K_UP; self.key_down=pygame.K_DOWN
				self.key_shoot=pygame.K_KP1; self.key_charge=pygame.K_KP2; self.bar_x=352; self.key_slow=pygame.K_KP3
			title=Title(index,side); all_sprites.add(title)
		def update(self):
			if self.invulnerable:
				now5=pygame.time.get_ticks()
				if now5-self.invulnerable_timer>5000:
					self.invulnerable_timer=now5; self.invulnerable=False; snd_getBonus.play()
			keystate=pygame.key.get_pressed()
			if not self.slow:
				if keystate[self.key_slow]:	self.speed=self.orig_speed/2; self.draw_hitbox()
				else:	self.speed=self.orig_speed
			else:	self.speed=1
			if keystate[self.key_left] and self.rect.left>self.left_limit:	self.rect.x-=self.speed
			if keystate[self.key_right] and self.rect.right<self.right_limit:	self.rect.x+=self.speed
			if keystate[self.key_up] and self.rect.top>16:	self.rect.y-=self.speed
			if keystate[self.key_down] and self.rect.bottom<463:	self.rect.y+=self.speed
			if keystate[self.key_shoot]:	self.shoot()
			if self.available>=self.max_charge:	self.available=self.max_charge
			if keystate[self.key_charge]:
				if self.charge<self.available:	self.charge+=1
			else:
				if (self.max_charge/4<self.charge<self.max_charge/2):	self.exshootlv1()
				elif (self.max_charge/2<self.charge<self.max_charge*3/4):	self.exshootlv2(); self.available-=int(self.max_charge/4)-1
				elif (self.max_charge*3/4<self.charge<self.max_charge):	self.exshootlv3(); self.available-=int(self.max_charge/2)-1
				elif (self.charge>=self.max_charge):	self.exshootlv4(); self.available-=int(self.max_charge*3/4)-1
				self.charge=0
			self.slow=False
			draw_ex_bar(screen,self.bar_x,459,self.available,self.max_charge,GRAY)
			draw_ex_bar(screen,self.bar_x,459,self.charge,self.max_charge)
			if not self.side:	lifeorig=126
			else:	lifeorig=446
			draw_lives(screen,lifeorig,17,self.hp,gui_lives)
			if self.charge in (int(self.max_charge/4),int(self.max_charge/2),int(self.max_charge*3/4),self.max_charge):
				if not self.maxed:	snd_charged.play()
			if self.charge==self.max_charge:	self.maxed=True
			else: self.maxed=False
		def draw_hitbox(self):
			hitbox=spr_hb; hitbox_rect=hitbox.get_rect(center=self.rect.center); screen.blit(hitbox,hitbox_rect)
			#pygame.draw.circle(screen,GREEN,self.rect.center,self.radius)
		def shoot(self):
			if self.charge==0:
				now=pygame.time.get_ticks()
				if now-self.last_shot>self.shot_delay:
					self.last_shot=now
					shot0=Shot(self.rect.centerx-9,self.rect.centery,self.index); all_sprites.add(shot0); shots.add(shot0)
					shot1=Shot(self.rect.centerx+9,self.rect.centery,self.index); all_sprites.add(shot1); shots.add(shot1)
		def ex_attack(self):
			if self.index==0:
				if not self.side: ex=Gi_Ex_Attack(random.randint(336+64,623-64),random.randint(16+128,304),0)
				else:	ex=Gi_Ex_Attack(random.randint(16+64,303-64),random.randint(16+128,304),1)
			elif self.index==1:
				if not self.side:	ex=LA_Ex_Attack(random.randint(336+32,623-32),448)
				else:	ex=LA_Ex_Attack(random.randint(16+32,303-32),448)
			elif self.index==2:
				if not self.side: ex=JM_Ex_Attack(random.randint(336+64,623-64),random.randint(16+128,304))
				else:	ex=JM_Ex_Attack(random.randint(16+64,303-64),random.randint(16+128,304))
			elif self.index==3:
				if not self.side:	ex=ZV_Ex_Attack(random.randint(336+64,623-64),random.randint(16+128,304),random.randint(0,359),1)
				else:	ex=ZV_Ex_Attack(random.randint(16+64,303-64),random.randint(16+128,304),random.randint(0,359),1)
			elif self.index==4:
				if not self.side:	ex=Dl_Ex_Attack(random.randint(336+64,623-64),random.randint(300,448))
				else:	ex=Dl_Ex_Attack(random.randint(16+64,303-64),random.randint(300,448))
			all_sprites.add(ex); ex_attacks.add(ex)
		def cleancircle(self,duration):
			for i in range(36):
				cc=CleanBullet(self.rect.centerx,self.rect.centery,10*i,2,duration)
		def exshootlv1(self):
			if self.index==0:
				for i in range(6):
					for j in range(3):
						amulet0=Amulet(self.rect.centerx,self.rect.centery,(i*60)+(j*15),1+j); all_sprites.add(amulet0)
						ex_shots.add(amulet0)
			elif self.index==1:
				snd_frontLaser.stop(); snd_frontLaser.play()
				laser0=Laser(self.rect.centerx-9,self.rect.bottom,self.side,1,1); all_sprites.add(laser0); ex_shots.add(laser0)
				laser0.duration=720
				laser1=Laser(self.rect.centerx+9,self.rect.bottom,self.side,1,1); all_sprites.add(laser1); ex_shots.add(laser1)
				laser1.duration=720
			elif self.index==2:
				for i in range(23):
					orb=Orb(self.rect.centerx,self.rect.centery,random.randint(0,359),random.randint(1,2),self.side)
					all_sprites.add(orb); ex_shots.add(orb)
			elif self.index==3:
				snd_swordSlash.stop(); snd_swordSlash.play()
				sword=Sword(self.rect.centerx,self.rect.top,200); all_sprites.add(sword); ex_shots.add(sword)
			elif self.index==4:
				snd_moon.stop(); snd_moon.play()
				moon=Moon(self.rect.centerx,self.rect.top); all_sprites.add(moon); ex_shots.add(moon)
		def exshootlv2(self):
			effect_release=EffectRelease(self.side,self.index)
			self.cleancircle(2)
			if self.index==0:
				if not self.side:	randx=random.randint(436,522)
				else:	randx=random.randint(100,186)
				randy=random.randint(100,200)
				knife_spawner=Knife_Spawner(randx,randy,self.side,1,1); all_sprites.add(knife_spawner)
			elif self.index==1:
				if not self.side:	randx=random.randint(336,623); randx2=random.randint(336,623)
				else:	randx=random.randint(16,303); randx2=random.randint(16,303)
				randy=random.randint(16,150); randy2=random.randint(16,150)
				laser0=Laser_Object(randx,randy,self.side); all_sprites.add(laser0)
				laser1=Laser_Object(randx2,randy2,self.side); all_sprites.add(laser1)
			elif self.index==2:
				if not self.side:	randx=random.randint(436,522)
				else:	randx=random.randint(100,186)
				randy=random.randint(96,296)
				x_spawner=XSpawner(randx,randy,spr_smallbullet_list); all_sprites.add(x_spawner)
			elif self.index==3:
				if not self.side:	randx=random.randint(436,522); randx2=random.randint(436,522)
				else:	randx=random.randint(100,186); randx2=random.randint(100,186)
				randy=random.randint(116,164); randy2=random.randint(332,364)
				g_spawner0=GhostSpawner(randx,randy2,0,spr_smallbullet_list); all_sprites.add(g_spawner0)
				g_spawner1=GhostSpawner(randx2,randy,1,spr_smallbullet_list); all_sprites.add(g_spawner1)
			elif self.index==4:
				if not self.side: x_val1=346; x_val2=613
				else:	x_val1=26; x_val2=293
				for i in range(15):
					star0=Star(x_val1,random.randint(16,463),random.randint(-45,45),1,0)
					star1=Star(x_val2,random.randint(16,463),random.randint(135,225),1,0)
					bullets.add(star0); bullets.add(star1)
		def exshootlv3(self):
			effect_release=EffectRelease(self.side,self.index)
			self.cleancircle(3)
			if self.index==0:
				if not self.side:	randx=random.randint(352,480);randx2=random.randint(495,607)
				else:	randx=random.randint(32,144);randx2=random.randint(175,287)
				randy=random.randint(100,200);randy2=random.randint(100,200)
				knife_spawner=Knife_Spawner(randx,randy,self.side,2); all_sprites.add(knife_spawner)
				knife_spawner1=Knife_Spawner(randx2,randy2,self.side,2); all_sprites.add(knife_spawner1)
			elif self.index==1:
				if not self.side:	randx=random.randint(336,623);randx2=random.randint(336,623);randx3=random.randint(336,623);randx4=random.randint(336,623)
				else:	randx=random.randint(16,303);randx2=random.randint(16,303);randx3=random.randint(16,303);randx4=random.randint(16,303)
				randy=random.randint(16,150);randy2=random.randint(16,150);randy3=random.randint(16,150);randy4=random.randint(16,150)
				laser0=Laser_Object(randx,randy,self.side,1);all_sprites.add(laser0); laser1=Laser_Object(randx2,randy2,self.side,1);all_sprites.add(laser1)
				laser2=Laser_Object(randx3,randy3,self.side,1);all_sprites.add(laser2); laser3=Laser_Object(randx4,randy4,self.side,1);all_sprites.add(laser3)
			elif self.index==2:
				if not self.side:	randx=random.randint(436,522); randx2=random.randint(436,522)
				else:	randx=random.randint(100,186); randx2=random.randint(100,186)
				randy=random.randint(96,296); randy2=random.randint(96,296)
				x_spawner0=XSpawner(randx,randy,spr_medbullet_list); all_sprites.add(x_spawner0)
				x_spawner1=XSpawner(randx2,randy2,spr_medbullet_list); all_sprites.add(x_spawner1)
			elif self.index==3:
				if not self.side:	randx=random.randint(436,522);randx2=random.randint(436,522);randx3=random.randint(436,522);randx4=random.randint(436,522)
				else:	randx=random.randint(100,186);randx2=random.randint(100,186);randx3=random.randint(100,186);randx4=random.randint(100,186)
				randy=random.randint(116,164);randy2=random.randint(332,364);randy3=random.randint(116,164);randy4=random.randint(332,364)
				g_spawner0=GhostSpawner(randx,randy2,0,spr_medbullet_list); all_sprites.add(g_spawner0)
				g_spawner1=GhostSpawner(randx2,randy,1,spr_medbullet_list); all_sprites.add(g_spawner1)
				g_spawner2=GhostSpawner(randx3,randy4,0,spr_medbullet_list); all_sprites.add(g_spawner2)
				g_spawner3=GhostSpawner(randx4,randy3,1,spr_medbullet_list); all_sprites.add(g_spawner3)
			elif self.index==4:
				if not self.side: x_val1=356; x_val2=603
				else:	x_val1=36; x_val2=283
				for i in range(20):
					star0=Star(x_val1,random.randint(16,463),random.randint(-45,45),2,1)
					star1=Star(x_val2,random.randint(16,463),random.randint(135,225),2,1)
					bullets.add(star0); bullets.add(star1)
		def exshootlv4(self):
			effect_release=EffectRelease(self.side,self.index)
			self.cleancircle(4)
			self.bossbck=BossBackground(self.side,self.index); self.bossfore=BossForeground(self.side,self.index)
			if self.index==0:	boss=Boss_Gi(self.side)
			elif self.index==1:	boss=Boss_LA(self.side)
			elif self.index==2:	boss=Boss_JM(self.side)
			elif self.index==3:	boss=Boss_ZV(self.side)
			elif self.index==4:	boss=Boss_Dl(self.side)
			bosses.add(boss); all_sprites.add(boss); snd_bossAttack[random.randint(0,3)].play()

	class Shot(pygame.sprite.Sprite):
		def __init__(self,x,y,index):
			pygame.sprite.Sprite.__init__(self)
			if index==0:	self.image=spr_shot[0]
			elif index==1:	self.image=spr_shot[1]
			elif index==2:	self.image=spr_shot[2]
			elif index==3:	self.image=spr_shot[3]
			elif index==4:	self.image=spr_shot[4]
			self.rect=self.image.get_rect(); self.rect.center=(x,y)
			self.speed=25
		def update(self):
			self.rect.y-=self.speed
			if self.rect.bottom<16:	self.kill()

	class Title(pygame.sprite.Sprite):
		def __init__(self,pj,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side
			if pj==0:	self.image=gi_title
			elif pj==1:	self.image=la_title
			elif pj==2:	self.image=jm_title
			elif pj==3:	self.image=zv_title
			elif pj==4:	self.image=dl_title
			self.rect=self.image.get_rect()
			if side==0:	self.rect.center=(150,256)
			elif side==1:	self.rect.center=(479,256)
			self.out=pygame.time.get_ticks(); self.moveOut=False; self.lastMoveOut=pygame.time.get_ticks()
		def update(self):
			now=pygame.time.get_ticks()
			if now-self.out>2160 and not self.moveOut:
				self.moveOut=True
			now2=pygame.time.get_ticks()
			if now2-self.lastMoveOut>30 and self.moveOut:
				self.lastMoveOut=now2
				if self.side==0:	self.rect.x-=8
				elif self.side==1:	self.rect.x+=8
			if self.side==0 and self.rect.right<16:	self.kill()
			elif self.side==1 and self.rect.left>623:	self.kill()

	class Background(pygame.sprite.Sprite):
		def __init__(self,background_list,bgm=None,x=0,y=0,delay=1):
			if bgm is not None:
				pygame.mixer.music.load('data/bgm/'+bgm); pygame.mixer.music.play(loops=-1)
			pygame.sprite.Sprite.__init__(self)
			self.list=background_list
			self.image=self.list[0]; self.rect=self.image.get_rect(topleft=(x,y))
			self.frame=0; self.frame_rate=30*delay; self.last_update=pygame.time.get_ticks()
		def update(self):
			self.image=self.list[self.frame]
			now=pygame.time.get_ticks()
			if now-self.last_update>self.frame_rate:
				self.last_update=now; self.frame+=1
				if self.frame==len(self.list):
					self.image=self.list[0]
					self.frame=0

	class Enemy_H(pygame.sprite.Sprite):
		def __init__(self,xPos,yPos,amp,speed,right=True):
			self.step=0; self.amp=amp; self.speed=speed/100; self.last_sine=pygame.time.get_ticks()
			self.yPos=yPos; self.right=right; self.death_time=pygame.time.get_ticks()
			pygame.sprite.Sprite.__init__(self)
			self.frame=0; self.frame_rate=90; self.last_update=pygame.time.get_ticks()
			self.image=spr_enemy_list[0]; self.rect=self.image.get_rect()
			self.rect.center=(xPos,yPos); self.radius=4
		def update(self):
			self.image=spr_enemy_list[self.frame]
			now=pygame.time.get_ticks()
			if now-self.last_update>self.frame_rate:
				self.last_update=now; self.frame+=1
				if self.frame==len(spr_enemy_list):
					self.image=spr_enemy_list[0]
					self.frame=0
			self.sine_movement()
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639) and self.right:	self.right=False; self.yPos+=19
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336) and not self.right:	self.right=True; self.yPos+=19
			if self.right:	self.rect.x+=3
			if not self.right:	self.rect.x-=3
			if self.rect.top>=480:	self.kill()
		def sine_movement(self):
			now2=pygame.time.get_ticks()
			if now2-self.last_sine>30:
				self.last_sine=now2
				self.rect.y=int(-1*math.sin(self.step*4)*self.amp)+self.yPos
				self.step+=self.speed
		def death(self):
			self.remove(all_sprites)
			now3=pygame.time.get_ticks()
			if now3-self.death_time>60:
				self.death_time=now3
				snd_hit.stop(); snd_hit.play()
				explosion=Explosion(self.rect.centerx,self.rect.centery); all_sprites.add(explosion); explosions.add(explosion)
				self.kill()

	class Enemy_R(pygame.sprite.Sprite):
		def __init__(self,x,y):
			self.death_time=pygame.time.get_ticks()
			pygame.sprite.Sprite.__init__(self)
			self.frame=0; self.frame_rate=90; self.last_update=pygame.time.get_ticks()
			self.image=spr_enemy_list[0]; self.rect=self.image.get_rect()
			self.rect.center=(x,y); self.radius=4
			self.hspeed=random.randint(0,3); self.vspeed=random.randint(1,3)
		def update(self):
			self.image=spr_enemy_list[self.frame]
			now=pygame.time.get_ticks()
			if now-self.last_update>self.frame_rate:
				self.last_update=now; self.frame+=1
				if self.frame==len(spr_enemy_list):
					self.image=spr_enemy_list[0]
					self.frame=0
			self.rect.x+=self.hspeed; self.rect.y+=self.vspeed
		def death(self):
			self.remove(all_sprites)
			now3=pygame.time.get_ticks()
			if now3-self.death_time>60:
				self.death_time=now3
				snd_hit.stop(); snd_hit.play()
				explosion=Explosion(self.rect.centerx,self.rect.centery); all_sprites.add(explosion); explosions.add(explosion)
				self.kill()

	class Explosion(pygame.sprite.Sprite):
		def __init__(self,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_explosion_list[0]; self.rect=self.image.get_rect(center=(x,y))
			self.frame=0; self.last_update=pygame.time.get_ticks()
			self.radius=4
			if self.rect.centerx<=321:	control.player_1.available+=2
			if self.rect.centerx>=322:	control.player_2.available+=2
		def update(self):
			self.image=spr_explosion_list[self.frame]
			now=pygame.time.get_ticks()
			if now-self.last_update>30:
				self.last_update=now; self.frame+=1
				if self.frame==len(spr_explosion_list):
					self.kill()

	class Fire(pygame.sprite.Sprite):
		def __init__(self,x,y,left):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_fire_list[0]; self.rect=self.image.get_rect(center=(x,y))
			self.bounceCounter=0; self.left=left; self.speed=1; self.hp=15
		def update(self):
			self.rect.y+=self.speed
			if self.rect.top>463:
				self.rect.bottom=0
				if self.left:	self.rect.x=random.randint(16,303)
				else:	self.rect.x=random.randint(336,623)
			if self.hp<=0:
				snd_hit.stop(); snd_hit.play()
				explosion=Explosion(self.rect.centerx,self.rect.centery)
				all_sprites.add(explosion); explosions.add(explosion)
				self.bounce(); self.hp=15
		def bounce(self):
			self.image=spr_fire_list[1]
			self.bounceCounter+=1
			self.speed+=1
			self.rect.bottom=0
			if self.left:	self.rect.x=random.randint(336,623); self.left=False
			else:	self.rect.x=random.randint(16,303); self.left=True
			if self.bounceCounter>3:
				self.image=spr_fire_list[0]
				self.bounceCounter=0; self.speed=1;
				if not self.left:	fire=Fire(random.randint(336,623),0,False)
				else:	fire=Fire(random.randint(16,303),0,True)
				all_sprites.add(fire); fires.add(fire)
		def ex_attack(self):
			if self.left:	control.player_1.ex_attack()
			else:	control.player_2.ex_attack()
			self.kill()

	class Bullet(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,size_list,index):
			pygame.sprite.Sprite.__init__(self)
			if size_list==spr_smallbullet_list:	cancelable.add(self); self.radius=2
			elif size_list==spr_medbullet_list:	self.radius=4
			elif size_list==spr_bigbullet_list:	self.radius=8
			self.image=size_list[index]
			self.rect=self.image.get_rect(center=(x,y))
			angle=math.radians(-angle)
			self.speed_x=speed*math.cos(angle)
			self.speed_y=speed*math.sin(angle)
			self.pos_x=x
			self.pos_y=y
		def update(self):
			#pygame.draw.circle(screen,GREEN,self.rect.center,self.radius)
			self.pos_x+=self.speed_x
			self.pos_y+=self.speed_y
			self.rect.center=(self.pos_x,self.pos_y)
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639):	self.kill()
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336):	self.kill()
			if self.rect.bottom<=0:	self.kill()
			if self.rect.top>=HEIGHT:	self.kill()

	class Laser(pygame.sprite.Sprite):
		def __init__(self,x,y,side,up=True,follow=False,scale=16):
			pygame.sprite.Sprite.__init__(self)
			self.image=self.image=pygame.transform.scale(spr_laser,(7,scale*28)).convert()
			self.rect=self.image.get_rect();
			self.side=side; self.follow=follow
			self.rect.centerx=x; self.duration=1440
			self.up=up
			if up:	self.rect.bottom=y
			else:	self.rect.top=y
			self.death_time=pygame.time.get_ticks()
		def update(self):
			if self.follow:
				keystate=pygame.key.get_pressed()
				if not self.side:
					if keystate[control.player_1.key_left]:	self.rect.x-=control.player_1.speed
					if keystate[control.player_1.key_right]:	self.rect.x+=control.player_1.speed
					if keystate[control.player_1.key_up]:	self.rect.y-=control.player_1.speed
					if keystate[control.player_1.key_down]:	self.rect.y+=control.player_1.speed
				else:
					if keystate[control.player_2.key_left]:	self.rect.x-=control.player_2.speed
					if keystate[control.player_2.key_right]:	self.rect.x+=control.player_2.speed
					if keystate[control.player_2.key_up]:	self.rect.y-=control.player_2.speed
					if keystate[control.player_2.key_down]:	self.rect.y+=control.player_2.speed
			now=pygame.time.get_ticks()
			if now-self.death_time>self.duration:	self.kill()
			if self.up and not self.follow:
				if self.rect.bottom<=0:	self.kill()
			else:
				if self.rect.top>=480:	self.kill()

	class Laser_Object(pygame.sprite.Sprite):
		def __init__(self,x,y,side,shoot=False):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_laser_obj; self.rect=self.image.get_rect(center=(x,y))
			self.timer=pygame.time.get_ticks(); self.hasShot=False
			self.timer_2=pygame.time.get_ticks(); self.side=side
			self.shoot=shoot; self.shoot_timer=pygame.time.get_ticks()
		def update(self):
			pygame.draw.lines(screen,WHITE,0,[(self.rect.center),(self.rect.centerx,480)])
			now=pygame.time.get_ticks()
			if now-self.timer>1440 and not self.hasShot:
				snd_backLaser.stop(); snd_backLaser.play()
				laser=Laser(self.rect.centerx,self.rect.centery,self.side,False); lasers.add(laser)
				self.hasShot=True
			now2=pygame.time.get_ticks()
			if now2-self.timer_2>2880 and self.hasShot:
				self.timer_2=now2
				self.kill()
			now3=pygame.time.get_ticks()
			if now3-self.shoot_timer>360:
				self.shoot_timer=now3
				snd_bullet.stop(); snd_bullet.play()
				for i in range(12):
					if self.shoot:	bullet0=Bullet(self.rect.centerx,self.rect.centery,i*30+15,1,spr_medbullet_list,3)
					else:	bullet0=Bullet(self.rect.centerx,self.rect.centery,i*30+15,1,spr_smallbullet_list,3)
					bullets.add(bullet0)

	class Amulet(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed):
			pygame.sprite.Sprite.__init__(self)
			self.image=pygame.transform.rotate(spr_gi_ex_shot,angle).convert()
			self.rect=self.image.get_rect(center=(x,y))
			self.speed=speed
			self.pos_x=x; self.pos_y=y
			self.angle=math.radians(-angle)
		def update(self):
			self.pos_x+=self.speed*math.cos(self.angle)
			self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639):	self.kill()
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336):	self.kill()
			if self.rect.bottom<=16:	self.kill()
			if self.rect.top>=464:	self.kill()

	class Knife(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,side,hspeed=1,rev=False):
			pygame.sprite.Sprite.__init__(self)
			self.rev=rev
			if self.rev:	self.image=spr_smallbullet_list[7]; cancelable.add(self); self.radius=2
			else:	self.image=pygame.transform.rotate(spr_knife,angle).convert(); self.radius=3
			self.rect=self.image.get_rect(center=(x,y))
			self.speed=speed; self.pos_x=x; self.pos_y=y
			self.angle=math.radians(-angle); self.side=side
			self.timer_1=pygame.time.get_ticks(); self.timer_2=pygame.time.get_ticks()
			self.hasStopped=False; self.hasPointed=False; self.pointer=0; self.huntingspeed=hspeed
		def update(self):
			#pygame.draw.circle(screen,GREEN,self.rect.center,self.radius)
			if not self.rev:	self.image=pygame.transform.rotate(spr_knife,math.degrees(-self.angle)).convert()
			self.pos_x+=self.speed*math.cos(self.angle)
			self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			now=pygame.time.get_ticks()
			if now-self.timer_1>1080 and not self.hasStopped:
				self.timer_1=now; snd_knifeStop.stop(); snd_knifeStop.play()
				self.hasStopped=True; self.speed=0
				self.timer_2=pygame.time.get_ticks()
			now2=pygame.time.get_ticks()
			if now2-self.timer_2>1440 and not self.hasPointed:
				self.timer_2=now2; snd_knifeShoot.stop(); snd_knifeShoot.play()
				if not self.side:	self.pointer=math.atan2(control.player_2.rect.centery-self.rect.centery,control.player_2.rect.centerx-self.rect.centerx)
				else:	self.pointer=math.atan2(control.player_1.rect.centery-self.rect.centery,control.player_1.rect.centerx-self.rect.centerx)
				self.angle=self.pointer; self.speed=self.huntingspeed; self.hasPointed=True
			if (303<=self.rect.left<=319 or 623<=self.rect.left<=639):	self.kill()
			elif (0<=self.rect.right<=16 or 320<=self.rect.right<=336):	self.kill()
			if self.rect.bottom<=16:	self.kill()
			if self.rect.top>=464:	self.kill()

	class Knife_Spawner(pygame.sprite.Sprite):
		def __init__(self,x,y,side,hspeed=1,rev=False):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_magic_sign; self.rect=self.image.get_rect(center=(x,y))
			self.hasShot=False; self.timer_1=pygame.time.get_ticks(); self.side=side
			self.hspeed=hspeed; self.rev=rev
		def update(self):
			now=pygame.time.get_ticks()
			if now-self.timer_1>1080 and not self.hasShot:
				self.timer_1=now; snd_knifeAppear.stop(); snd_knifeAppear.play(); self.hasShot=True
				for i in range(24):
					knife=Knife(self.rect.centerx,self.rect.centery,15*i,2,self.side,self.hspeed,self.rev)
					knife1=Knife(self.rect.centerx,self.rect.centery,15*i+7,1,self.side,self.hspeed,self.rev)
					bullets.add(knife); bullets.add(knife1)
				self.kill()

	class Sword(pygame.sprite.Sprite):
		def __init__(self,x,y,duration):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_zv_ex_shot[0]
			self.rect=self.image.get_rect()
			self.rect.centerx=x; self.rect.bottom=y
			self.duration=duration; self.timer=pygame.time.get_ticks()
			self.last_update=pygame.time.get_ticks(); self.frame=0; self.frame_rate=30
			self.orig_x=x
		def update(self):
			self.rect.centerx=self.orig_x+random.choice((-15,15))
			now=pygame.time.get_ticks()
			if now-self.last_update>self.frame_rate:
				self.last_update=now
				if self.frame_rate>0:	self.frame+=1
				if self.frame==len(spr_zv_ex_shot):
					self.image=spr_zv_ex_shot[3]
					self.frame=3
					self.frame_rate=0
			self.image=spr_zv_ex_shot[self.frame]
			now2=pygame.time.get_ticks()
			if now2-self.timer>self.duration:	self.kill()

	class Orb(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,side):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_jm_ex_shot; self.rect=self.image.get_rect(center=(x,y))
			self.angle=math.radians(-angle); self.side=side
			self.pos_x=x; self.pos_y=y; self.speed=speed; self.hasStopped=False
			self.stop_timer=pygame.time.get_ticks(); self.shoot_timer=pygame.time.get_ticks()
		def update(self):
			self.pos_x+=self.speed*math.cos(self.angle)
			self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			if not self.side:
				if 0<=self.rect.right<=16:	self.kill()
				if 303<=self.rect.left<=319:	self.kill()
			else:
				if 320<=self.rect.right<=336:	self.kill()
				if 623<=self.rect.left<=639:	self.kill()
			if self.rect.bottom<=16:	self.kill()
			now=pygame.time.get_ticks()
			if now-self.stop_timer>720 and not self.hasStopped:	self.stop_timer=now; self.speed=0; self.hasStopped=True
			now2=pygame.time.get_ticks()
			if now2-self.shoot_timer>1440 and self.hasStopped:
				self.shoot_timer=now2; self.angle=math.radians(-random.randint(70,110)); self.speed=random.randint(5,8)

	class Moon(pygame.sprite.Sprite):
		def __init__(self,x,y):
			pygame.sprite.Sprite.__init__(self)
			self.image_orig=spr_moon; self.image=self.image_orig.copy()
			self.rect=self.image.get_rect(center=(x,y)); self.rot=0
			self.rot_speed=15; self.last_update=pygame.time.get_ticks()
		def rotate(self):
			now=pygame.time.get_ticks()
			if now-self.last_update>30:
				self.last_update = now
				self.rot=(self.rot + self.rot_speed)%360
				new_image=pygame.transform.rotate(self.image_orig,self.rot).convert_alpha()
				old_center=self.rect.center
				self.image=new_image
				self.rect=self.image.get_rect()
				self.rect.center=old_center
		def update(self):
			self.rect.y-=3
			if self.rect.bottom<=0:	self.kill()
			self.rotate()

	class Star(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,size):
			pygame.sprite.Sprite.__init__(self)
			if not size:	self.image_orig=spr_smallstar; cancelable.add(self); self.radius=2
			else:	self.image_orig=spr_bigstar; self.radius=5
			self.image=self.image_orig.copy(); self.rot=0; self.rot_speed=15
			self.rect=self.image.get_rect(center=(x,y)); angle=math.radians(-angle)
			self.speed_x=speed*math.cos(angle); self.speed_y=speed*math.sin(angle)
			self.pos_x=x; self.pos_y=y; self.last_update=pygame.time.get_ticks()
		def rotate(self):
			now=pygame.time.get_ticks()
			if now-self.last_update>30:
				self.last_update = now
				self.rot=(self.rot + self.rot_speed)%360
				new_image=pygame.transform.rotate(self.image_orig,self.rot).convert()
				old_center=self.rect.center
				self.image=new_image
				self.rect=self.image.get_rect()
				self.rect.center=old_center
		def update(self):
			#pygame.draw.circle(screen,GREEN,self.rect.center,self.radius)
			self.rotate()
			self.pos_x+=self.speed_x
			self.pos_y+=self.speed_y
			self.rect.center=(self.pos_x,self.pos_y)
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639):	self.kill()
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336):	self.kill()
			if self.rect.bottom<=0:	self.kill()
			if self.rect.top>=HEIGHT:	self.kill()

	class XSpawner(pygame.sprite.Sprite):
		def __init__(self,x,y,size_list):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_magic_sign; self.rect=self.image.get_rect(center=(x,y))
			self.spin=0; self.last_shot=pygame.time.get_ticks(); self.death_time=pygame.time.get_ticks()
			self.size=size_list
		def update(self):
			now=pygame.time.get_ticks()
			if now-self.last_shot>90:	self.last_shot=now; self.shoot()
			now2=pygame.time.get_ticks()
			if now2-self.death_time>2880:	self.kill()
		def shoot(self):
			snd_bullet.stop(); snd_bullet.play()
			self.spin=(self.spin+6)%360
			for i in range(4):
				bullet=Bullet(self.rect.centerx,self.rect.centery,i*90-self.spin,2,self.size,0)
				bullets.add(bullet)

	class GhostSpawner(pygame.sprite.Sprite):
		def __init__(self,x,y,down,size_list):
			pygame.sprite.Sprite.__init__(self); self.down=down
			self.image=spr_magic_sign; self.rect=self.image.get_rect(center=(x,y))
			self.spin=0; self.last_shot=pygame.time.get_ticks(); self.death_time=pygame.time.get_ticks()
			self.size=size_list
		def update(self):
			if self.down:	self.rect.y+=1
			else:	self.rect.y-=1
			now=pygame.time.get_ticks()
			if now-self.last_shot>90:	self.last_shot=now; self.shoot()
			now2=pygame.time.get_ticks()
			if now2-self.death_time>2880:	self.kill()	
		def shoot(self):
			snd_bullet.stop(); snd_bullet.play()
			self.spin=(self.spin-6)&-360
			for i in range(2):
				ghost=Bullet(self.rect.centerx,self.rect.centery,i*180-self.spin,1,self.size,random.choice([0,3,4]))
				bullets.add(ghost)

	class TestSpawn(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image=pygame.Surface((1,1)); self.rect=self.image.get_rect()
			self.pattern=0; self.spawn_new=pygame.time.get_ticks(); self.counter=0
			self.new_pattern=pygame.time.get_ticks(); self.new_bullet=pygame.time.get_ticks()
		def update(self):
			now=pygame.time.get_ticks()
			if now-self.spawn_new>200 and self.counter<5:
				self.spawn_new=now; self.counter+=1
				self.spawn()
			if self.counter>=5:
				now2=pygame.time.get_ticks()
				if now2-self.new_pattern>5000:
					for i in range(random.randint(1,3)):
						fire=Fire(random.randint(16+16,303-16),16,1); fire0=Fire(random.randint(336+16,623-16),16,0)
						all_sprites.add(fire,fire0); fires.add(fire,fire0)
					self.new_pattern=now2
					self.counter=0
			now3=pygame.time.get_ticks()
			if now3-self.new_bullet>1000:
				self.new_bullet=now3
				for i in range(random.randint(1,5)):
					bullet0=Bullet(random.randint(25,294),25,random.randint(260,280),random.randint(1,2),spr_smallbullet_list,random.randint(0,7))
					bullet1=Bullet(random.randint(345,614),25,random.randint(260,280),random.randint(1,2),spr_smallbullet_list,random.randint(0,7))
					bullets.add(bullet0); bullets.add(bullet1)
		def spawn(self):
			enemy=Enemy_H(35,35,20,5); all_sprites.add(enemy); enemies.add(enemy)
			enemy0=Enemy_H(355,35,20,5); all_sprites.add(enemy0); enemies.add(enemy0)
			for i in range(2):
				enemy1=Enemy_R(random.randint(36,283),16); all_sprites.add(enemy1); enemies.add(enemy1)
				enemy2=Enemy_R(random.randint(356,603),16); all_sprites.add(enemy2); enemies.add(enemy2)

	class EffectRelease(pygame.sprite.Sprite):
		def __init__(self,side,index):
			pygame.sprite.Sprite.__init__(self)
			snd_effectRelease.stop(); snd_effectRelease.play()
			if index==0:	self.image=gui_effect[0]
			if index==1:	self.image=gui_effect[1]
			if index==2:	self.image=gui_effect[2]
			if index==3:	self.image=gui_effect[3]
			if index==4:	self.image=gui_effect[4]
			self.rect=self.image.get_rect(); self.side=side
			if not side:	self.rect.topleft=(16,118)
			else:	self.rect.topleft=(336,118)
			all_sprites.add(self); self.frame_update=pygame.time.get_ticks()
		def update(self):
			if not self.side:	screen.blit(gui_warning,(335,16))
			else:	screen.blit(gui_warning,(16,16))
			now=pygame.time.get_ticks()
			if now-self.frame_update>60:
				self.frame_update=now
				pygame.time.wait(720)
				self.kill()

	class BossBackground(pygame.sprite.Sprite):
		def __init__(self,side,index):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.index=index; self.scroll=0
			self.image=pygame.Surface((1,1)); self.rect=self.image.get_rect()
			boss_backgrounds.add(self); self.origin_y=16
			if self.index==0 or self.index==2:	self.scroller_timer=pygame.time.get_ticks()
			if not self.side:	self.origin_x=336
			else: self.origin_x=16
		def update(self):
			if self.index==0:
				now=pygame.time.get_ticks()
				if now-self.scroller_timer>30:	self.scroller_timer=now; self.origin_y+=3
				for i in range(6):	screen.blit(bck_boss_gi_back,(self.origin_x,self.origin_y-111+(111*i)))
				if self.origin_y>111:	self.origin_y-=111
			elif self.index==1:	screen.blit(bck_boss_la_back,(self.origin_x,self.origin_y))
			elif self.index==2:
				now=pygame.time.get_ticks()
				if now-self.scroller_timer>30:	self.scroller_timer=now; self.origin_y+=1
				for i in range(5):	screen.blit(bck_boss_jm_back,(self.origin_x,self.origin_y-146+(146*i)))
				if self.origin_y>146:	self.origin_y-=146
			elif self.index==3:	screen.blit(bck_boss_zv_back,(self.origin_x,self.origin_y))
			elif self.index==4:	screen.blit(bck_boss_dl_back,(self.origin_x,self.origin_y))

	class BossForeground(pygame.sprite.Sprite):
		def __init__(self,side,index):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.index=index
			self.image=pygame.Surface((1,1)); self.rect=self.image.get_rect()
			boss_foregrounds.add(self)
			if self.index==0:	self.angle=0
			if self.index==4:	self.alpha=0; self.image=bck_boss_dl_front; self.scale=2
			if self.index==0 or self.index==4:
				if not self.side:	self.center=(479,241)
				else:	self.center=(160,239)
			else:
				self.origin_y=16; self.scroller_timer=pygame.time.get_ticks()
				if not self.side:	self.origin_x=336
				else:	self.origin_x=16
		def update(self):
			if self.index==0:
				self.image=pygame.transform.rotate(bck_boss_gi_front,self.angle).convert_alpha()
				self.rect=self.image.get_rect(center=self.center)
				self.angle=(self.angle+1)%360
			elif self.index==1:
				now=pygame.time.get_ticks()
				if now-self.scroller_timer>30:	self.scroller_timer=now; self.origin_y+=3
				for i in range(4):	screen.blit(bck_boss_la_front,(self.origin_x,self.origin_y-168+(168*i)))
				if self.origin_y>168:	self.origin_y-=168
			elif self.index==2:
				now=pygame.time.get_ticks()
				if now-self.scroller_timer>30:	self.scroller_timer=now; self.origin_y-=3
				for i in range(3):
					for j in range(2):
						screen.blit(bck_boss_jm_front,(self.origin_x+(j*144),self.origin_y+(285*i)))
				if self.origin_y<-285:	self.origin_y+=285
			elif self.index==3:
				now=pygame.time.get_ticks()
				if now-self.scroller_timer>30:	self.scroller_timer=now; self.origin_y-=5
				for i in range(5):
					for j in range(2):
						screen.blit(bck_boss_zv_front,(self.origin_x+(j*144),self.origin_y+(144*i)))
				if self.origin_y<-144:	self.origin_y+=144
			elif self.index==4:
				if self.alpha<255:
					self.image=pygame.transform.scale(bck_boss_dl_front,(int(146*self.scale),int(146*self.scale)))
					self.image.set_alpha(self.alpha); self.alpha+=1; self.scale-=0.0035
				else:	self.image=bck_boss_dl_front_alpha
				self.rect=self.image.get_rect(center=self.center)

	class Boss_Gi(pygame.sprite.Sprite):
		def __init__(self,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.hp=350
			self.image=spr_boss_gi
			if not side:	self.orig_x=336; self.dest_x=480; self.spell_origin=(382,51)
			else:	self.orig_x=16; self.dest_x=160; self.spell_origin=(62,51)
			self.orig_y=16; self.rect=self.image.get_rect(); self.movement=False
			self.dest_y=96; self.start=False; self.pointer=0; self.move_timer=pygame.time.get_ticks()
			self.attack_timer=pygame.time.get_ticks(); self.spin=0; self.attack_timer_2=pygame.time.get_ticks()
			self.life_timer=pygame.time.get_ticks()
		def update(self):
			screen.blit(gui_boss_atk[0],self.spell_origin)
			if not self.start:
				self.pointer=math.atan2(self.dest_y-self.rect.centery,self.dest_x-self.rect.centerx)
				self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
				self.rect.center=(self.orig_x,self.orig_y)
				if self.rect.centerx==self.dest_x or self.rect.centery==self.dest_y:
					self.start=True
			else:
				now=pygame.time.get_ticks()
				if now-self.move_timer>4000:
					self.move_timer=now; self.movement=not self.movement; self.randy=random.randint(96,166)
					if not self.side:	self.randx=random.randint(400,559)
					else:	self.randx=random.randint(80,239)
				if self.movement:
					self.pointer=math.atan2(self.randy-self.rect.centery,self.randx-self.rect.centerx)
					self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
					self.rect.center=(self.orig_x,self.orig_y)
					if self.rect.centerx==self.randx or self.rect.centery==self.randy:	self.movement= not self.movement
				else:	self.attack()
			if self.hp<=0:
				snd_bossDefeat.play()
				if not self.side:	control.player_1.bossfore.kill(); control.player_1.bossbck.kill()
				else:	control.player_2.bossfore.kill(); control.player_2.bossbck.kill()
				self.kill()
			death=pygame.time.get_ticks()
			if death-self.life_timer>25000:	self.hp=0
		def attack(self):
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>450:
				self.attack_timer=now2
				snd_bullet.play()
				for i in range(24):
					bullet0=Bullet(self.rect.centerx+50*math.cos(-math.radians(360/24*i)),
						self.rect.centery+50*math.sin(-math.radians(360/24*i)),
						15*i+self.spin,2,spr_medbullet_list,7)
					bullets.add(bullet0)
				self.spin=(self.spin+7)%360
			now3=pygame.time.get_ticks()
			if now3-self.attack_timer_2>750:
				self.attack_timer_2=now3; angle=0
				if not self.side: angle=math.degrees(-math.atan2(control.player_2.rect.centery-self.rect.centery,control.player_2.rect.centerx-self.rect.centerx))
				else:	angle=math.degrees(-math.atan2(control.player_1.rect.centery-self.rect.centery,control.player_1.rect.centerx-self.rect.centerx))
				bullet1=Bullet(self.rect.centerx,self.rect.centery,angle,3,spr_bigbullet_list,7); bullets.add(bullet1)

	class Boss_LA(pygame.sprite.Sprite):
		def __init__(self,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.hp=350
			self.image=spr_boss_la; self.attacking=False; self.isCharging=True; self.lock=0
			if not side:	self.orig_x=336; self.dest_x=480; self.spell_origin=(382,51)
			else:	self.orig_x=16; self.dest_x=160; self.spell_origin=(62,51)
			self.orig_y=16; self.rect=self.image.get_rect(); self.movement=False
			self.dest_y=96; self.start=False; self.pointer=0; self.move_timer=pygame.time.get_ticks()
			self.attack_timer=pygame.time.get_ticks(); self.spin=0; self.attack_timer_2=pygame.time.get_ticks()
			self.life_timer=pygame.time.get_ticks(); self.bulletspeed=2; self.attack_timer_3=pygame.time.get_ticks()
		def update(self):
			screen.blit(gui_boss_atk[1],self.spell_origin)
			if not self.start:
				self.pointer=math.atan2(self.dest_y-self.rect.centery,self.dest_x-self.rect.centerx)
				self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
				self.rect.center=(self.orig_x,self.orig_y)
				if self.rect.centerx==self.dest_x or self.rect.centery==self.dest_y:
					self.start=True
			else:
				now=pygame.time.get_ticks()
				if now-self.move_timer>4000:
					self.move_timer=now; self.movement=not self.movement; self.randy=random.randint(96,166)
					if not self.side:	self.randx=random.randint(400,559)
					else:	self.randx=random.randint(80,239)
				if self.movement:
					self.pointer=math.atan2(self.randy-self.rect.centery,self.randx-self.rect.centerx)
					self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
					self.rect.center=(self.orig_x,self.orig_y)
					if self.rect.centerx==self.randx or self.rect.centery==self.randy:	self.movement= not self.movement
				else:	self.attack()
			if self.hp<=0:
				snd_fo.stop()
				snd_bossDefeat.play()
				if not self.side:	control.player_1.bossfore.kill(); control.player_1.bossbck.kill()
				else:	control.player_2.bossfore.kill(); control.player_2.bossbck.kill()
				self.kill()
			death=pygame.time.get_ticks()
			if death-self.life_timer>25000:	self.hp=0
		def attack(self):
			now4=pygame.time.get_ticks()
			if now4-self.attack_timer_3>250:
				self.attack_timer_3=now4; snd_bullet.stop(); snd_bullet.play()
				for i in range(12):
					bullet0=Bullet(self.rect.centerx,self.rect.centery,30*i,self.bulletspeed,spr_medbullet_list,0)
					bullet1=Bullet(self.rect.centerx,self.rect.centery,random.randint(0,359),1,spr_smallbullet_list,random.randint(0,7))
					bullets.add(bullet0,bullet1)
			if self.isCharging:	snd_isCharging.play(); self.isCharging=False
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>4000:
				self.attack_timer=now2
				if not self.side:	self.lock=math.degrees(-math.atan2(control.player_2.rect.centery-self.rect.centery,control.player_2.rect.centerx-self.rect.centerx))
				else:	self.lock=math.degrees(-math.atan2(control.player_1.rect.centery-self.rect.centery,control.player_1.rect.centerx-self.rect.centerx))
				if not self.attacking:	snd_fo.play(loops=-1); self.bulletspeed=3
				else:	snd_fo.stop(); self.isCharging=True; self.bulletspeed=2
				self.attacking=not self.attacking
			if self.attacking:
				now3=pygame.time.get_ticks()
				if now3-self.attack_timer_2>50:
					self.attack_timer_2=now3
					for i in range(4):
						laser0=Bullet(self.rect.centerx,self.rect.centery,self.lock+random.randint(-2,2),7,spr_medbullet_list,0)
						bullets.add(laser0)
			else:
				target=0
				if not self.side:	target=control.player_2.rect.center
				else:	target=control.player_1.rect.center
				pygame.draw.line(screen,WHITE,self.rect.center,target)
				pygame.draw.circle(screen,RED,target,20,1)

	class JMBullet(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,color,side):
			pygame.sprite.Sprite.__init__(self)
			if color:self.image=spr_bigbullet_list[8]
			else:	self.image=spr_bigbullet_list[0]
			self.rect=self.image.get_rect(center=(x,y))
			self.side=side; self.timer=pygame.time.get_ticks()
			self.changed=False; self.angle=angle
			self.speed=speed; self.pointer=0
			self.pos_x=x; self.pos_y=y; self.radius=8
		def update(self):
			#pygame.draw.circle(screen,GREEN,self.rect.center,self.radius)
			self.pos_x+=self.speed*math.cos(self.angle)
			self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			now=pygame.time.get_ticks()
			if now-self.timer>1000 and not self.changed:
				self.timer=now
				if not self.side:	self.pointer=math.atan2(control.player_2.rect.centery-self.rect.centery,control.player_2.rect.centerx-self.rect.centerx)
				else:	self.pointer=math.atan2(control.player_1.rect.centery-self.rect.centery,control.player_1.rect.centerx-self.rect.centerx)
				self.angle=self.pointer; self.speed=self.speed*2

				self.changed=True
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639):	self.kill()
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336):	self.kill()
			if self.rect.bottom<=0:	self.kill()
			if self.rect.top>=HEIGHT:	self.kill()

	class Boss_JM(pygame.sprite.Sprite):
		def __init__(self,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.hp=350
			self.image=spr_boss_jm
			if not side:	self.orig_x=336; self.dest_x=480; self.spell_origin=(382,51)
			else:	self.orig_x=16; self.dest_x=160; self.spell_origin=(62,51)
			self.orig_y=16; self.rect=self.image.get_rect(); self.movement=False
			self.dest_y=96; self.start=False; self.pointer=0; self.move_timer=pygame.time.get_ticks()
			self.attack_timer=pygame.time.get_ticks(); self.spin=180; self.attack_timer_2=pygame.time.get_ticks()
			self.life_timer=pygame.time.get_ticks(); self.counter=0
		def update(self):
			screen.blit(gui_boss_atk[2],self.spell_origin)
			if not self.start:
				self.pointer=math.atan2(self.dest_y-self.rect.centery,self.dest_x-self.rect.centerx)
				self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
				self.rect.center=(self.orig_x,self.orig_y)
				if self.rect.centerx==self.dest_x or self.rect.centery==self.dest_y:
					self.start=True
			else:
				now=pygame.time.get_ticks()
				if now-self.move_timer>4000:
					self.move_timer=now; self.movement=not self.movement; self.randy=random.randint(96,166)
					if not self.side:	self.randx=random.randint(400,559)
					else:	self.randx=random.randint(80,239)
				if self.movement:
					self.pointer=math.atan2(self.randy-self.rect.centery,self.randx-self.rect.centerx)
					self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
					self.rect.center=(self.orig_x,self.orig_y)
					if self.rect.centerx==self.randx or self.rect.centery==self.randy:	self.movement= not self.movement
				else:	self.attack()
			if self.hp<=0:
				snd_bossDefeat.play()
				if not self.side:	control.player_1.bossfore.kill(); control.player_1.bossbck.kill()
				else:	control.player_2.bossfore.kill(); control.player_2.bossbck.kill()
				self.kill()
			death=pygame.time.get_ticks()
			if death-self.life_timer>25000:	self.hp=0
		def attack(self):
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>250:
				self.attack_timer=now2
				if self.counter<=10:
					snd_bullet.stop(); snd_bullet.play()
					bullet0=JMBullet(self.rect.centerx,self.rect.centery,self.spin,2,random.choice([0,1]),self.side)
					bullets.add(bullet0)
					self.counter+=1; self.spin+=18
				else:	self.spin=180; self.counter=0
			now3=pygame.time.get_ticks()
			if now3-self.attack_timer_2>15:
				self.attack_timer_2=now3
				bullet1=Bullet(self.rect.centerx,self.rect.centery,random.randint(0,360),1,spr_smallbullet_list,random.choice([0,8]))
				bullets.add(bullet1)

	class ZVBullet(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,change):
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_ghostbullet[0]; self.radius=4
			self.rect=self.image.get_rect(center=(x,y))
			self.timer=pygame.time.get_ticks(); self.rota=angle
			self.angle=math.radians(-angle); self.speed=speed
			self.pos_x=x; self.pos_y=y; self.change=change
		def update(self):
			#pygame.draw.circle(screen,RED,self.rect.center,self.radius)
			self.image=pygame.transform.rotate(spr_ghostbullet[self.change],self.rota)
			self.pos_x+=self.speed*math.cos(self.angle)
			self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			now=pygame.time.get_ticks()
			if now-self.timer>800 and self.change<2:
				self.timer=now; self.change+=1
				self.change_color()
			if (303<=self.rect.right<=319 or 623<=self.rect.right<=639):	self.kill()
			elif (0<=self.rect.left<=16 or 320<=self.rect.left<=336):	self.kill()
			if self.rect.bottom<=0:	self.kill()
			if self.rect.top>=HEIGHT:	self.kill()
		def change_color(self):
			snd_spiritual.stop(); snd_spiritual.play()
			for i in range(-1,2):
				bullet0=ZVBullet(self.rect.centerx,self.rect.centery,self.rota+180+(30*i),2,self.change)
				bullets.add(bullet0)
			self.kill()

	class Boss_ZV(pygame.sprite.Sprite):
		def __init__(self,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.hp=350
			self.image=spr_boss_zv
			if not side:	self.orig_x=336; self.dest_x=480; self.spell_origin=(382,51)
			else:	self.orig_x=16; self.dest_x=160; self.spell_origin=(62,51)
			self.orig_y=16; self.rect=self.image.get_rect(); self.movement=False
			self.dest_y=96; self.start=False; self.pointer=0; self.move_timer=pygame.time.get_ticks()
			self.attack_timer=pygame.time.get_ticks(); self.spin=0;	self.life_timer=pygame.time.get_ticks()
		def update(self):
			screen.blit(gui_boss_atk[3],self.spell_origin)
			if not self.start:
				self.pointer=math.atan2(self.dest_y-self.rect.centery,self.dest_x-self.rect.centerx)
				self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
				self.rect.center=(self.orig_x,self.orig_y)
				if self.rect.centerx==self.dest_x or self.rect.centery==self.dest_y:
					self.start=True
			else:
				now=pygame.time.get_ticks()
				if now-self.move_timer>4000:
					self.move_timer=now; self.movement=not self.movement; self.randy=random.randint(96,166)
					if not self.side:	self.randx=random.randint(400,559)
					else:	self.randx=random.randint(80,239)
				if self.movement:
					self.pointer=math.atan2(self.randy-self.rect.centery,self.randx-self.rect.centerx)
					self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
					self.rect.center=(self.orig_x,self.orig_y)
					if self.rect.centerx==self.randx or self.rect.centery==self.randy:	self.movement= not self.movement
				else:	self.attack()
			if self.hp<=0:
				snd_bossDefeat.play()
				if not self.side:	control.player_1.bossfore.kill(); control.player_1.bossbck.kill()
				else:	control.player_2.bossfore.kill(); control.player_2.bossbck.kill()
				self.kill()
			death=pygame.time.get_ticks()
			if death-self.life_timer>25000:	self.hp=0
		def attack(self):
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>500:
				self.attack_timer=now2
				snd_bullet.stop(); snd_bullet.play()
				for i in range(4):
					bullet0=ZVBullet(self.rect.centerx,self.rect.centery,self.spin+(90*i),2,0)
					bullets.add(bullet0)
				self.spin=(self.spin+15)%90

	class Boss_Dl(pygame.sprite.Sprite):
		def __init__(self,side):
			pygame.sprite.Sprite.__init__(self)
			self.side=side; self.hp=350
			self.image=spr_boss_dl
			if not side:	self.orig_x=336; self.dest_x=480; self.spell_origin=(382,51)
			else:	self.orig_x=16; self.dest_x=160; self.spell_origin=(62,51)
			self.orig_y=16; self.rect=self.image.get_rect(); self.movement=False
			self.dest_y=96; self.start=False; self.pointer=0; self.move_timer=pygame.time.get_ticks()
			self.attack_timer=pygame.time.get_ticks(); self.spin=0; self.attack_timer_2=pygame.time.get_ticks()
			self.life_timer=pygame.time.get_ticks()
		def update(self):
			screen.blit(gui_boss_atk[4],self.spell_origin)
			if not self.start:
				self.pointer=math.atan2(self.dest_y-self.rect.centery,self.dest_x-self.rect.centerx)
				self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
				self.rect.center=(self.orig_x,self.orig_y)
				if self.rect.centerx==self.dest_x or self.rect.centery==self.dest_y:
					self.start=True
			else:
				now=pygame.time.get_ticks()
				if now-self.move_timer>4000:
					self.move_timer=now; self.movement=not self.movement; self.randy=random.randint(96,166)
					if not self.side:	self.randx=random.randint(400,559)
					else:	self.randx=random.randint(80,239)
				if self.movement:
					self.pointer=math.atan2(self.randy-self.rect.centery,self.randx-self.rect.centerx)
					self.orig_x+=2*math.cos(self.pointer); self.orig_y+=2*math.sin(self.pointer)
					self.rect.center=(self.orig_x,self.orig_y)
					if self.rect.centerx==self.randx or self.rect.centery==self.randy:	self.movement= not self.movement
				else:	self.attack()
			if self.hp<=0:
				snd_bossDefeat.play()
				if not self.side:	control.player_1.bossfore.kill(); control.player_1.bossbck.kill()
				else:	control.player_2.bossfore.kill(); control.player_2.bossbck.kill()
				self.kill()
			death=pygame.time.get_ticks()
			if death-self.life_timer>25000:	self.hp=0
		def attack(self):
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>50:
				self.attack_timer=now2
				snd_bullet.stop(); snd_bullet.play()
				for i in range(5):
					bullet0=Star(self.rect.centerx+50*math.cos(-math.radians(self.spin+(120*i))),
						self.rect.centery+50*math.sin(-math.radians(self.spin+(120*i))),
						random.randint(0,359),random.choice([1,2]),random.choice([0,1]))
					bullets.add(bullet0)
			now3=pygame.time.get_ticks()
			if now3-self.attack_timer_2>50:
				self.attack_timer_2=now3
				for i in range(3):
					bullet1=Bullet(self.rect.centerx+50*math.cos(-math.radians(self.spin+(120*i))),
						self.rect.centery+50*math.sin(-math.radians(self.spin+(120*i))),
						self.spin+(120*i),2,spr_medbullet_list,random.choice([0,2,3]))
					bullets.add(bullet1)
				self.spin=(self.spin+10)%360

	class Gi_Ex_Attack(pygame.sprite.Sprite):
		def __init__(self,x,y,side):
			pygame.sprite.Sprite.__init__(self); self.index=0
			self.image=spr_gi_ex_atk; self.rect=self.image.get_rect(center=(x,y))
			self.alpha=0; self.image.set_alpha(self.alpha); self.side=side
			self.last_update=pygame.time.get_ticks(); self.death_timer=pygame.time.get_ticks()
			self.conversion_time=pygame.time.get_ticks()
		def update(self):
			self.image.set_alpha(self.alpha)
			now=pygame.time.get_ticks()
			if now-self.last_update>30:
				self.last_update=now
				if self.alpha<190:	self.alpha+=5
			now2=pygame.time.get_ticks()
			if now2-self.death_timer>5000:
				self.kill()
		def conversion(self):
			naifu=Knife(self.rect.centerx,self.rect.centery,random.randint(0,359),1,self.side)
			bullets.add(naifu)
			now3=pygame.time.get_ticks()
			if now3-self.conversion_time>200:	self.kill()

	class LA_Ex_Attack(pygame.sprite.Sprite):
		def __init__(self,x,y):
			pygame.sprite.Sprite.__init__(self); self.index=1; self.start=pygame.time.get_ticks()
			self.image=pygame.Surface((1,1)); self.rect=self.image.get_rect(center=(x,y))
			self.shoot_timer=pygame.time.get_ticks(); self.death_timer=pygame.time.get_ticks()
			self.shoot_laser=False
		def update(self):
			pygame.draw.line(screen,WHITE,self.rect.center,(self.rect.centerx,16))
			now=pygame.time.get_ticks()
			if now-self.start>1000 and not self.shoot_laser:
				self.start=now; snd_backLaser.play(); self.shoot_laser=True
			if self.shoot_laser:
				now2=pygame.time.get_ticks()
				if now2-self.shoot_timer>25:
					self.shoot_timer=now
					laser0=Bullet(self.rect.centerx,self.rect.centery,random.randint(89,91),7,spr_medbullet_list,0)
					bullets.add(laser0)
			now3=pygame.time.get_ticks()
			if now3-self.death_timer>3000:	self.kill()

	class JM_Ex_Attack(pygame.sprite.Sprite):
		def __init__(self,x,y):
			snd_cross.play(); self.index=2
			pygame.sprite.Sprite.__init__(self)
			self.image=spr_jm_ex_atk[0]
			self.rect=self.image.get_rect(center=(x,y))
			self.expand_timer=pygame.time.get_ticks()
			self.new_center=self.rect.center; self.death_timer=pygame.time.get_ticks()
		def update(self):
			now=pygame.time.get_ticks()
			if now-self.expand_timer>1000:
				self.image=spr_jm_ex_atk[1]
				self.mask=pygame.mask.from_surface(self.image)
				crosses.add(self)
				self.rect=self.image.get_rect(center=self.new_center)
			now2=pygame.time.get_ticks()
			if now2-self.death_timer>3000:
				self.kill()

	class ZV_Ex_Attack(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed):
			snd_knifeAppear.play(); self.index=3; self.direction_counter=0
			pygame.sprite.Sprite.__init__(self)
			self.image=pygame.transform.rotate(spr_zv_ex_atk,angle).convert()
			self.rect=self.image.get_rect(center=(x,y)); self.change_timer=pygame.time.get_ticks()
			self.pos_x=x; self.pos_y=y; self.angle=math.radians(-angle); self.speed=speed
			self.attack_timer=pygame.time.get_ticks()
		def update(self):
			self.image=pygame.transform.rotate(spr_zv_ex_atk,math.degrees(-self.angle)).convert()
			self.pos_x+=self.speed*math.cos(self.angle); self.pos_y+=self.speed*math.sin(self.angle)
			self.rect.center=(self.pos_x,self.pos_y)
			now=pygame.time.get_ticks()
			if now-self.change_timer>2000:	self.change_timer=now; self.change_direction()
			now2=pygame.time.get_ticks()
			if now2-self.attack_timer>500:
				self.attack_timer=now2
				snd_spiritual.stop(); snd_spiritual.play()
				bullet0=Bullet(self.rect.centerx,self.rect.centery,math.degrees(self.angle),2,spr_medbullet_list,random.choice([0,3,4]))
				bullets.add(bullet0)
			if (303<=self.rect.left<=319 or 623<=self.rect.left<=639):	self.kill()
			elif (0<=self.rect.right<=16 or 320<=self.rect.right<=336):	self.kill()
			if self.rect.bottom<=16:	self.kill()
			if self.rect.top>=464:	self.kill()
		def change_direction(self):
			self.direction_counter+=1
			if self.direction_counter<3:
				snd_recovery.play()
				self.angle=math.radians(-random.randint(0,359))

	class Dl_Ex_Attack(pygame.sprite.Sprite):
		def __init__(self,x,y):
			self.index=4; self.last_update=pygame.time.get_ticks()
			pygame.sprite.Sprite.__init__(self); slowers.add(self)
			self.image=spr_dl_ex_atk[0];self.rect=self.image.get_rect(center=(x,y))
			self.death_timer=pygame.time.get_ticks(); self.frame=0
		def update(self):
			self.image=spr_dl_ex_atk[self.frame]
			now=pygame.time.get_ticks()
			if now-self.last_update>500:
				self.last_update=now
				if self.frame<len(spr_dl_ex_atk)-1:
					self.frame+=1
			now2=pygame.time.get_ticks()
			if now2-self.death_timer>7000:
				self.kill()

	class CleanBullet(pygame.sprite.Sprite):
		def __init__(self,x,y,angle,speed,duration):
			pygame.sprite.Sprite.__init__(self)
			cleaners.add(self)
			self.image=spr_clean_bullet; self.rect=self.image.get_rect(center=(x,y))
			self.posx=x; self.posy=y; self.angle=math.radians(-angle); self.speed=speed
			self.duration=duration*1000; self.death_time=pygame.time.get_ticks()
			self.radius=6
		def update(self):
			self.posx+=self.speed*math.cos(self.angle)
			self.posy+=self.speed*math.sin(self.angle)
			self.rect.center=(self.posx,self.posy)
			now=pygame.time.get_ticks()
			if now-self.death_time>self.duration:
				self.death_time=now; self.kill()
			if (313<=self.rect.right<=321 or 633<=self.rect.right<=640):	self.kill()
			elif (0<=self.rect.left<=6 or 322<=self.rect.left<=326):	self.kill()
			if self.rect.bottom<=0:	self.kill()
			if self.rect.top>=HEIGHT:	self.kill()

	class GameWinner(pygame.sprite.Sprite):
		def __init__(self,side):
			snd_bossDefeat.play()
			pygame.sprite.Sprite.__init__(self)
			self.image=pygame.Surface((1,1)); self.rect=self.image.get_rect()
			self.side=side; self.once=False
		def update(self):
			if not self.once:
				self.once=True
				pygame.time.wait(1000)
				control.player_1.kill(); control.player_2.kill()
				selection.testspawn.kill()
			if self.side:
				screen.blit(gui_round_end[0],(26,166))
				screen.blit(gui_round_end[1],(346,166))
			else:
				screen.blit(gui_round_end[0],(346,166))
				screen.blit(gui_round_end[1],(26,166))

	#spritegroups creations
	backgrounds=pygame.sprite.Group(); all_sprites=pygame.sprite.Group(); fires=pygame.sprite.Group()
	shots=pygame.sprite.Group(); enemies=pygame.sprite.Group(); explosions=pygame.sprite.Group()
	bullets=pygame.sprite.Group(); ex_shots=pygame.sprite.Group(); boss_backgrounds=pygame.sprite.Group()
	boss_foregrounds=pygame.sprite.Group(); bosses=pygame.sprite.Group(); cancelable=pygame.sprite.Group()
	lasers=pygame.sprite.Group(); ex_attacks=pygame.sprite.Group(); slowers=pygame.sprite.Group()
	players=pygame.sprite.Group(); cleaners=pygame.sprite.Group(); crosses=pygame.sprite.Group()

	#first object placement
	pygame.mixer.music.load('data/bgm/main.ogg'); pygame.mixer.music.play(loops=-1)
	control=CONTROL(); menuarrow=MenuArrow(); all_sprites.add(menuarrow)
	selection=SelectionScreen()

	running=True

	#main loop
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			elif event.type==pygame.KEYDOWN:
				mod_bitmask=pygame.key.get_mods()
				if mod_bitmask&pygame.KMOD_ALT:
					if event.key==pygame.K_RETURN:
						if not FULLSCREEN:	screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN); FULLSCREEN=True
						else:	screen=pygame.display.set_mode((WIDTH,HEIGHT)); FULLSCREEN=False
						icon=load_sprite('icon.png'); pygame.display.set_icon(icon)
					elif event.key==pygame.K_F4:	running=False
				elif control.screen==0:
					if event.key==pygame.K_DOWN:	snd_select.stop(); snd_select.play(); menuarrow.options+=1
					if event.key==pygame.K_UP:	snd_select.stop(); snd_select.play(); menuarrow.options-=1
					if event.key==pygame.K_RETURN:	menuarrow.enter()
				elif control.screen==1:
					if event.key==pygame.K_ESCAPE:
						menuarrow=MenuArrow(); all_sprites.add(menuarrow); backgrounds.empty(); control.screen=0
						selection.cursor1.kill(); selection.cursor2.kill(); selection.ready=False; selection.stagecursor.kill()
						selection.ready=False; selection.chooseStage=False
				elif control.screen==2:
					if event.key==pygame.K_ESCAPE:
						snd_fo.stop()
						backgrounds.empty(); all_sprites.empty(); shots.empty(); enemies.empty(); explosions.empty(); ex_shots.empty()
						fires.empty(); shots.empty(); bullets.empty(); boss_backgrounds.empty(); boss_foregrounds.empty()
						bosses.empty(); cancelable.empty(); lasers.empty(); slowers.empty(); players.empty(); selection.testspawn.kill()
						menuarrow=MenuArrow(); all_sprites.add(menuarrow); control.screen=0; selection.ready=False; selection.chooseStage=False
						pygame.mixer.music.load('data/bgm/main.ogg'); pygame.mixer.music.play(loops=-1); cleaners.empty()
						selection.testspawn.kill(); crosses.empty()

		#if you shoot an enemy
		hits=pygame.sprite.groupcollide(enemies,shots,False,True)
		for hit in hits:
			hit.death()

		#if your ex shot kills an enemy
		hits=pygame.sprite.groupcollide(enemies,ex_shots,False,False)
		for hit in hits:
			hit.death()

		#if you kill enemies with your explosions
		hits=pygame.sprite.groupcollide(enemies,explosions,False,False,pygame.sprite.collide_circle)
		for hit in hits:
			hit.death()

		#if you destroy a "fire" with your explosions
		hits=pygame.sprite.groupcollide(fires,explosions,False,False)
		for hit in hits:
			hit.ex_attack()

		#if you destroy a "fire" with your shots
		hits=pygame.sprite.groupcollide(fires,shots,False,True)
		for hit in hits:
			hit.hp-=1

		#if you shoot a boss
		hits=pygame.sprite.groupcollide(bosses,shots,False,True)
		for hit in hits:
			hit.hp-=1

		#if your ex shots hit a boss
		hits=pygame.sprite.groupcollide(bosses,ex_shots,False,False)
		for hit in hits:
			hit.hp-=1

		#when your explosions destroy the small bullets
		hits=pygame.sprite.groupcollide(cancelable,explosions,True,False)

		if control.screen==2:
			#if a player collides with an enemy
			hits=pygame.sprite.groupcollide(players,enemies,False,True,pygame.sprite.collide_circle)
			for hit in hits:
				if not hit.invulnerable:
					hit.cleancircle(1)
					if hit.hp==1:	hit.available=hit.max_charge
					else:	hit.available+=int(hit.max_charge/4)
					snd_gotHit.play(); hit.hp-=1; hit.invulnerable=True
					if hit.hp<0:
						game_winner=GameWinner(hit.side)
						cleaners.add(game_winner)

			#if a player collides with a bullet
			hits=pygame.sprite.groupcollide(players,bullets,False,True,pygame.sprite.collide_circle)
			for hit in hits:
				if not hit.invulnerable:
					hit.cleancircle(1)
					if hit.hp==1: hit.available=hit.max_charge
					else:	hit.available+=int(hit.max_charge/4)
					snd_gotHit.play(); hit.hp-=1; hit.invulnerable=True
					if hit.hp<0:
						game_winner=GameWinner(hit.side)
						cleaners.add(game_winner)

			#if a player collides with a laser
			hits=pygame.sprite.groupcollide(players,lasers,False,True,pygame.sprite.collide_rect_ratio(0.6))
			for hit in hits:
				if not hit.invulnerable:
					hit.cleancircle(1)
					if hit.hp==1: hit.available=hit.max_charge
					else:	hit.available+=int(hit.max_charge/4)
					snd_gotHit.play(); hit.hp-=1; hit.invulnerable=True
					if hit.hp<0:
						game_winner=GameWinner(hit.side)
						cleaners.add(game_winner)

			#if certain ex attacks hit bullets
			hits=pygame.sprite.groupcollide(ex_attacks,bullets,False,False)
			for hit in hits:
				if hit.index==0:	hit.conversion()

			#if certain ex attack slows a player down
			hits=pygame.sprite.groupcollide(players,slowers,False,False)
			for hit in hits:
				hit.slow=True

			hits=pygame.sprite.groupcollide(players,crosses,False,False,pygame.sprite.collide_mask)
			for hit in hits:
				if not hit.invulnerable:
					hit.cleancircle(1)
					if hit.hp==1: hit.available=hit.max_charge
					else:	hit.available+=int(hit.max_charge/4)
					snd_gotHit.play(); hit.hp-=1; hit.invulnerable=True
					if hit.hp<0:
						game_winner=GameWinner(hit.side)
						cleaners.add(game_winner)			

			#when cleaners... clean the screen(?
			hits=pygame.sprite.groupcollide(bullets,cleaners,True,False)
			hits=pygame.sprite.groupcollide(lasers,cleaners,True,False)
			hits=pygame.sprite.groupcollide(ex_attacks,cleaners,True,False)
			hits=pygame.sprite.groupcollide(crosses,cleaners,True,False)

			#cleaners kill enemies
			hits=pygame.sprite.groupcollide(enemies,cleaners,False,False,pygame.sprite.collide_circle)
			for hit in hits:
				hit.death()

			#cleaners kill "fires"
			hits=pygame.sprite.groupcollide(fires,cleaners,False,False)
			for hit in hits:
				hit.ex_attack()

	#drawing functions
		screen.fill(BLACK)
		backgrounds.update(); backgrounds.draw(screen)
		boss_backgrounds.update(); boss_backgrounds.draw(screen)
		boss_foregrounds.update(); boss_foregrounds.draw(screen)
		if control.screen==0:
			screen.blit(gui_main,gui_main_rect)
		elif control.screen==1:
			selection.update()
			screen.blit(gui_select,gui_select_rect)
		all_sprites.draw(screen); all_sprites.update()
		bullets.draw(screen); bullets.update()
		lasers.update(); lasers.draw(screen)
		if control.screen==2:
			selection.testspawn.update()
			cleaners.update(); cleaners.draw(screen)
			screen.blit(spr_bar,(30,457)); screen.blit(spr_bar,(350,457))
			screen.blit(spr_overlay,spr_overlay_rect)
		pygame.display.flip()
	pygame.quit()
	exit()

GameStart()