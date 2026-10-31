import pygame
import os
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
# Set ASSETS path relative to the pygamefinale folder
# When running from pygamefinale folder: "the_pale_wanderer_complete/the_pale_wanderer/assets"
ASSETS = "the_pale_wanderer_complete/the_pale_wanderer/assets"
ASSETS_PATH = "the_pale_wanderer_complete/the_pale_wanderer/assets"

# Player dictionary - maps asset names to surfaces loaded from filesystem
PLAYER_ASSETS = {
    "walk_1": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_walk_1.png")),
    "walk_2": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_walk_2.png")),
    "walk_3": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_walk_3.png")),
    "walk_4": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_walk_4.png")),
    "idle_1": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_idle_1.png")) if os.path.exists(os.path.join(ASSETS_PATH, "player", "pale_wanderer_idle_1.png")) else None,
    "idle_2": pygame.image.load(os.path.join(ASSETS_PATH, "player", "pale_wanderer_idle_2.png")) if os.path.exists(os.path.join(ASSETS_PATH, "player", "pale_wanderer_idle_2.png")) else None,
}


PLAYER_LAYER = 1


PLAYER_SPEED = 200 

# Animation settings
ANIMATION_SPEED = 150


class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.assets = PLAYER_ASSETS
        
        self.image = self.assets["walk_1"]
        self.rect = self.image.get_rect(topleft=(x, y))
        

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        
        self.walk_frame = 0
        self.last_animation_update = 0
        self.is_moving = False
        self.facing_right = True
        
        self.walk_frames = [
            self.assets["walk_1"],
            self.assets["walk_2"],
            self.assets["walk_3"],
            self.assets["walk_4"],
        ]
    
    def update(self, dt, keys):

        self.direction = pygame.math.Vector2(0, 0)
        self.is_moving = False
        self.vel = 0
        

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.is_moving = True
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.is_moving = True
            self.facing_right = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.is_moving = True
        if keys[pygame.K_SPACE] or keys[pygame.K_SPACE]:
                self.direction.y = -10
                self.is_moving = True

        if self.rect.y>600:
            self.rect.y=600
                
        

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        

        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
        self.vel = min(self.vel + 0.5, 8)
        self.direction.y += int(self.vel)
        #self.rect.topleft = (int(self.x), int(self.y))
        

        if self.is_moving:
            self._update_animation(dt)
        else:

            self.image = self.walk_frames[0] if self.facing_right else pygame.transform.flip(self.walk_frames[0], True, False)
    
    def _update_animation(self, dt):

        now = pygame.time.get_ticks()
        if now - self.last_animation_update > ANIMATION_SPEED:
            self.last_animation_update = now
            self.walk_frame += 1
            if self.walk_frame >= len(self.walk_frames):
                self.walk_frame = 0
            

            if self.facing_right:
                self.image = self.walk_frames[self.walk_frame]
            else:
                self.image = pygame.transform.flip(self.walk_frames[self.walk_frame], True, False)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1=Player(800/2, 600/2)
player_group=pygame.sprite.Group()
player_group.add(P1)


# NOTE: boss frames are big (696px, Void 888px). Scale them down with
#       pygame.transform.smoothscale(...) at load time if memory is tight.
# NOTE: images load as plain surfaces. After pygame.display.set_mode(...)
# call  surface.convert_alpha()  on them if you want faster blitting.

# ===== PLAYER =====
player_pale_wanderer_attack_down = pygame.image.load(f"{ASSETS}/player/pale_wanderer_attack_down.png")
player_pale_wanderer_attack_recover = pygame.image.load(f"{ASSETS}/player/pale_wanderer_attack_recover.png")
player_pale_wanderer_attack_slash = pygame.image.load(f"{ASSETS}/player/pale_wanderer_attack_slash.png")
player_pale_wanderer_attack_up = pygame.image.load(f"{ASSETS}/player/pale_wanderer_attack_up.png")
player_pale_wanderer_attack_windup = pygame.image.load(f"{ASSETS}/player/pale_wanderer_attack_windup.png")
player_pale_wanderer_crouch = pygame.image.load(f"{ASSETS}/player/pale_wanderer_crouch.png")
player_pale_wanderer_dash = pygame.image.load(f"{ASSETS}/player/pale_wanderer_dash.png")
player_pale_wanderer_death_1 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_death_1.png")
player_pale_wanderer_death_2 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_death_2.png")
player_pale_wanderer_fall = pygame.image.load(f"{ASSETS}/player/pale_wanderer_fall.png")
player_pale_wanderer_focus = pygame.image.load(f"{ASSETS}/player/pale_wanderer_focus.png")
player_pale_wanderer_heal_1 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_heal_1.png")
player_pale_wanderer_heal_2 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_heal_2.png")
player_pale_wanderer_hurt_1 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_hurt_1.png")
player_pale_wanderer_hurt_2 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_hurt_2.png")
player_pale_wanderer_idle_1 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_idle_1.png")
player_pale_wanderer_idle_2 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_idle_2.png")
player_pale_wanderer_jump_peak = pygame.image.load(f"{ASSETS}/player/pale_wanderer_jump_peak.png")
player_pale_wanderer_jump_rise = pygame.image.load(f"{ASSETS}/player/pale_wanderer_jump_rise.png")
player_pale_wanderer_land = pygame.image.load(f"{ASSETS}/player/pale_wanderer_land.png")
player_pale_wanderer_victory = pygame.image.load(f"{ASSETS}/player/pale_wanderer_victory.png")
player_pale_wanderer_walk_1 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_walk_1.png")
player_pale_wanderer_walk_2 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_walk_2.png")
player_pale_wanderer_walk_3 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_walk_3.png")
player_pale_wanderer_walk_4 = pygame.image.load(f"{ASSETS}/player/pale_wanderer_walk_4.png")
player_pale_wanderer_wall_cling = pygame.image.load(f"{ASSETS}/player/pale_wanderer_wall_cling.png")

# ===== FX =====
fx_dash_trail = pygame.image.load(f"{ASSETS}/fx/dash_trail.png")
fx_dust_1 = pygame.image.load(f"{ASSETS}/fx/dust_1.png")
fx_dust_2 = pygame.image.load(f"{ASSETS}/fx/dust_2.png")
fx_ember = pygame.image.load(f"{ASSETS}/fx/ember.png")
fx_heal_glow = pygame.image.load(f"{ASSETS}/fx/heal_glow.png")
fx_hit_flash = pygame.image.load(f"{ASSETS}/fx/hit_flash.png")
fx_hit_spark = pygame.image.load(f"{ASSETS}/fx/hit_spark.png")
fx_light_ray = pygame.image.load(f"{ASSETS}/fx/light_ray.png")
fx_scythe = pygame.image.load(f"{ASSETS}/fx/scythe.png")
fx_scythe_upgraded = pygame.image.load(f"{ASSETS}/fx/scythe_upgraded.png")
fx_slash_down = pygame.image.load(f"{ASSETS}/fx/slash_down.png")
fx_slash_h = pygame.image.load(f"{ASSETS}/fx/slash_h.png")
fx_slash_up = pygame.image.load(f"{ASSETS}/fx/slash_up.png")
fx_soul_orb = pygame.image.load(f"{ASSETS}/fx/soul_orb.png")
fx_spore_particle = pygame.image.load(f"{ASSETS}/fx/spore_particle.png")
fx_void_particle = pygame.image.load(f"{ASSETS}/fx/void_particle.png")

# ===== NPCS =====
npcs_bard_cricket = pygame.image.load(f"{ASSETS}/npcs/bard_cricket.png")
npcs_bremite_idle_1 = pygame.image.load(f"{ASSETS}/npcs/bremite_idle_1.png")
npcs_bremite_idle_2 = pygame.image.load(f"{ASSETS}/npcs/bremite_idle_2.png")
npcs_bremite_idle_3 = pygame.image.load(f"{ASSETS}/npcs/bremite_idle_3.png")
npcs_child_spore = pygame.image.load(f"{ASSETS}/npcs/child_spore.png")
npcs_mapmaker_moth = pygame.image.load(f"{ASSETS}/npcs/mapmaker_moth.png")
npcs_merchant_hooded = pygame.image.load(f"{ASSETS}/npcs/merchant_hooded.png")
npcs_mushroom_villager_a = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_a.png")
npcs_mushroom_villager_b = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_b.png")
npcs_mushroom_villager_c = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_c.png")
npcs_mushroom_villager_d = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_d.png")
npcs_mushroom_villager_e = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_e.png")
npcs_mushroom_villager_f = pygame.image.load(f"{ASSETS}/npcs/mushroom_villager_f.png")
npcs_smith_rhino = pygame.image.load(f"{ASSETS}/npcs/smith_rhino.png")
npcs_white_king_ghost = pygame.image.load(f"{ASSETS}/npcs/white_king_ghost.png")
npcs_white_king_statue = pygame.image.load(f"{ASSETS}/npcs/white_king_statue.png")

# ===== VILLAGE =====
village_barrel = pygame.image.load(f"{ASSETS}/village/barrel.png")
village_bench = pygame.image.load(f"{ASSETS}/village/bench.png")
village_bench_save = pygame.image.load(f"{ASSETS}/village/bench_save.png")
village_bridge_plank = pygame.image.load(f"{ASSETS}/village/bridge_plank.png")
village_crate = pygame.image.load(f"{ASSETS}/village/crate.png")
village_door = pygame.image.load(f"{ASSETS}/village/door.png")
village_fence = pygame.image.load(f"{ASSETS}/village/fence.png")
village_firefly_lamp = pygame.image.load(f"{ASSETS}/village/firefly_lamp.png")
village_hanging_lamp = pygame.image.load(f"{ASSETS}/village/hanging_lamp.png")
village_house_a = pygame.image.load(f"{ASSETS}/village/house_a.png")
village_house_b = pygame.image.load(f"{ASSETS}/village/house_b.png")
village_house_c = pygame.image.load(f"{ASSETS}/village/house_c.png")
village_lamp_post = pygame.image.load(f"{ASSETS}/village/lamp_post.png")
village_lantern = pygame.image.load(f"{ASSETS}/village/lantern.png")
village_mushroom_blue = pygame.image.load(f"{ASSETS}/village/mushroom_blue.png")
village_mushroom_glow = pygame.image.load(f"{ASSETS}/village/mushroom_glow.png")
village_mushroom_orange = pygame.image.load(f"{ASSETS}/village/mushroom_orange.png")
village_mushroom_pink = pygame.image.load(f"{ASSETS}/village/mushroom_pink.png")
village_mushroom_purple = pygame.image.load(f"{ASSETS}/village/mushroom_purple.png")
village_mushroom_red = pygame.image.load(f"{ASSETS}/village/mushroom_red.png")
village_pot = pygame.image.load(f"{ASSETS}/village/pot.png")
village_signpost = pygame.image.load(f"{ASSETS}/village/signpost.png")
village_spore_jar = pygame.image.load(f"{ASSETS}/village/spore_jar.png")
village_well = pygame.image.load(f"{ASSETS}/village/well.png")

# ===== TILES =====
tiles_abyss_bg = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_bg.png")
tiles_abyss_bg_alt = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_bg_alt.png")
tiles_abyss_decor_a = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_decor_a.png")
tiles_abyss_decor_b = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_decor_b.png")
tiles_abyss_fill = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_fill.png")
tiles_abyss_fill_alt = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_fill_alt.png")
tiles_abyss_hazard = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_hazard.png")
tiles_abyss_platform = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_platform.png")
tiles_abyss_top = pygame.image.load(f"{ASSETS}/tiles/abyss/abyss_top.png")
tiles_ants_nest_bg = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_bg.png")
tiles_ants_nest_bg_alt = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_bg_alt.png")
tiles_ants_nest_decor_a = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_decor_a.png")
tiles_ants_nest_decor_b = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_decor_b.png")
tiles_ants_nest_fill = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_fill.png")
tiles_ants_nest_fill_alt = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_fill_alt.png")
tiles_ants_nest_hazard = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_hazard.png")
tiles_ants_nest_platform = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_platform.png")
tiles_ants_nest_top = pygame.image.load(f"{ASSETS}/tiles/ants_nest/ants_nest_top.png")
tiles_desert_bg = pygame.image.load(f"{ASSETS}/tiles/desert/desert_bg.png")
tiles_desert_bg_alt = pygame.image.load(f"{ASSETS}/tiles/desert/desert_bg_alt.png")
tiles_desert_decor_a = pygame.image.load(f"{ASSETS}/tiles/desert/desert_decor_a.png")
tiles_desert_decor_b = pygame.image.load(f"{ASSETS}/tiles/desert/desert_decor_b.png")
tiles_desert_fill = pygame.image.load(f"{ASSETS}/tiles/desert/desert_fill.png")
tiles_desert_fill_alt = pygame.image.load(f"{ASSETS}/tiles/desert/desert_fill_alt.png")
tiles_desert_hazard = pygame.image.load(f"{ASSETS}/tiles/desert/desert_hazard.png")
tiles_desert_platform = pygame.image.load(f"{ASSETS}/tiles/desert/desert_platform.png")
tiles_desert_top = pygame.image.load(f"{ASSETS}/tiles/desert/desert_top.png")
tiles_gossamer_reach_bg = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_bg.png")
tiles_gossamer_reach_bg_alt = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_bg_alt.png")
tiles_gossamer_reach_decor_a = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_decor_a.png")
tiles_gossamer_reach_decor_b = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_decor_b.png")
tiles_gossamer_reach_fill = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_fill.png")
tiles_gossamer_reach_fill_alt = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_fill_alt.png")
tiles_gossamer_reach_hazard = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_hazard.png")
tiles_gossamer_reach_platform = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_platform.png")
tiles_gossamer_reach_top = pygame.image.load(f"{ASSETS}/tiles/gossamer_reach/gossamer_reach_top.png")
tiles_hole_fungal_bg = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_bg.png")
tiles_hole_fungal_bg_alt = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_bg_alt.png")
tiles_hole_fungal_decor_a = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_decor_a.png")
tiles_hole_fungal_decor_b = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_decor_b.png")
tiles_hole_fungal_fill = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_fill.png")
tiles_hole_fungal_fill_alt = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_fill_alt.png")
tiles_hole_fungal_hazard = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_hazard.png")
tiles_hole_fungal_platform = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_platform.png")
tiles_hole_fungal_top = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/hole_fungal_top.png")
tiles_hole_fungal_vine = pygame.image.load(f"{ASSETS}/tiles/hole_fungal/vine.png")
tiles_ivory_gardens_bg = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_bg.png")
tiles_ivory_gardens_bg_alt = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_bg_alt.png")
tiles_ivory_gardens_decor_a = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_decor_a.png")
tiles_ivory_gardens_decor_b = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_decor_b.png")
tiles_ivory_gardens_fill = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_fill.png")
tiles_ivory_gardens_fill_alt = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_fill_alt.png")
tiles_ivory_gardens_hazard = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_hazard.png")
tiles_ivory_gardens_platform = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_platform.png")
tiles_ivory_gardens_top = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ivory_gardens_top.png")
tiles_ivory_gardens_ladder = pygame.image.load(f"{ASSETS}/tiles/ivory_gardens/ladder.png")
tiles_mallow_mire_bg = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_bg.png")
tiles_mallow_mire_bg_alt = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_bg_alt.png")
tiles_mallow_mire_decor_a = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_decor_a.png")
tiles_mallow_mire_decor_b = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_decor_b.png")
tiles_mallow_mire_fill = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_fill.png")
tiles_mallow_mire_fill_alt = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_fill_alt.png")
tiles_mallow_mire_hazard = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_hazard.png")
tiles_mallow_mire_platform = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_platform.png")
tiles_mallow_mire_top = pygame.image.load(f"{ASSETS}/tiles/mallow_mire/mallow_mire_top.png")
tiles_pantheon_gate = pygame.image.load(f"{ASSETS}/tiles/pantheon/gate.png")
tiles_pantheon_bg = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_bg.png")
tiles_pantheon_bg_alt = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_bg_alt.png")
tiles_pantheon_decor_a = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_decor_a.png")
tiles_pantheon_decor_b = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_decor_b.png")
tiles_pantheon_fill = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_fill.png")
tiles_pantheon_fill_alt = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_fill_alt.png")
tiles_pantheon_hazard = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_hazard.png")
tiles_pantheon_platform = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_platform.png")
tiles_pantheon_top = pygame.image.load(f"{ASSETS}/tiles/pantheon/pantheon_top.png")
tiles_white_empire_bg = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_bg.png")
tiles_white_empire_bg_alt = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_bg_alt.png")
tiles_white_empire_decor_a = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_decor_a.png")
tiles_white_empire_decor_b = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_decor_b.png")
tiles_white_empire_fill = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_fill.png")
tiles_white_empire_fill_alt = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_fill_alt.png")
tiles_white_empire_hazard = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_hazard.png")
tiles_white_empire_platform = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_platform.png")
tiles_white_empire_top = pygame.image.load(f"{ASSETS}/tiles/white_empire/white_empire_top.png")

# ===== ARTIFACTS =====
artifacts_abyssal_pearl = pygame.image.load(f"{ASSETS}/artifacts/abyssal_pearl.png")
artifacts_broken_white_crown = pygame.image.load(f"{ASSETS}/artifacts/broken_white_crown.png")
artifacts_gossamer_spool = pygame.image.load(f"{ASSETS}/artifacts/gossamer_spool.png")
artifacts_ivory_rose = pygame.image.load(f"{ASSETS}/artifacts/ivory_rose.png")
artifacts_memory_fragment = pygame.image.load(f"{ASSETS}/artifacts/memory_fragment.png")
artifacts_mire_lily = pygame.image.load(f"{ASSETS}/artifacts/mire_lily.png")
artifacts_pantheon_laurel = pygame.image.load(f"{ASSETS}/artifacts/pantheon_laurel.png")
artifacts_queens_mandible = pygame.image.load(f"{ASSETS}/artifacts/queens_mandible.png")
artifacts_spore_heart = pygame.image.load(f"{ASSETS}/artifacts/spore_heart.png")
artifacts_sun_shard = pygame.image.load(f"{ASSETS}/artifacts/sun_shard.png")

# ===== ENDGAME =====
endgame_pedestal = pygame.image.load(f"{ASSETS}/endgame/pedestal.png")
endgame_pedestal_filled = pygame.image.load(f"{ASSETS}/endgame/pedestal_filled.png")
endgame_seal_gate = pygame.image.load(f"{ASSETS}/endgame/seal_gate.png")
endgame_shrine_a = pygame.image.load(f"{ASSETS}/endgame/shrine_a.png")
endgame_shrine_b = pygame.image.load(f"{ASSETS}/endgame/shrine_b.png")
endgame_void_guardian = pygame.image.load(f"{ASSETS}/endgame/void_guardian.png")
endgame_void_orb = pygame.image.load(f"{ASSETS}/endgame/void_orb.png")
endgame_void_rift = pygame.image.load(f"{ASSETS}/endgame/void_rift.png")
endgame_void_tendril = pygame.image.load(f"{ASSETS}/endgame/void_tendril.png")
endgame_white_flame = pygame.image.load(f"{ASSETS}/endgame/white_flame.png")

# ===== ENEMIES =====
enemies_abyss_wraith = pygame.image.load(f"{ASSETS}/enemies/abyss_wraith.png")
enemies_ant_flyer = pygame.image.load(f"{ASSETS}/enemies/ant_flyer.png")
enemies_ant_soldier = pygame.image.load(f"{ASSETS}/enemies/ant_soldier.png")
enemies_ant_worker = pygame.image.load(f"{ASSETS}/enemies/ant_worker.png")
enemies_cave_larva = pygame.image.load(f"{ASSETS}/enemies/cave_larva.png")
enemies_empire_husk = pygame.image.load(f"{ASSETS}/enemies/empire_husk.png")
enemies_empire_sentry = pygame.image.load(f"{ASSETS}/enemies/empire_sentry.png")
enemies_fungal_crawler = pygame.image.load(f"{ASSETS}/enemies/fungal_crawler.png")
enemies_gossamer_spider = pygame.image.load(f"{ASSETS}/enemies/gossamer_spider.png")
enemies_ivory_moth = pygame.image.load(f"{ASSETS}/enemies/ivory_moth.png")
enemies_ivory_wisp = pygame.image.load(f"{ASSETS}/enemies/ivory_wisp.png")
enemies_mire_frog = pygame.image.load(f"{ASSETS}/enemies/mire_frog.png")
enemies_mire_fungus = pygame.image.load(f"{ASSETS}/enemies/mire_fungus.png")
enemies_mire_slug = pygame.image.load(f"{ASSETS}/enemies/mire_slug.png")
enemies_pantheon_champion = pygame.image.load(f"{ASSETS}/enemies/pantheon_champion.png")
enemies_pantheon_spirit = pygame.image.load(f"{ASSETS}/enemies/pantheon_spirit.png")
enemies_sand_scarab = pygame.image.load(f"{ASSETS}/enemies/sand_scarab.png")
enemies_sand_scorpion = pygame.image.load(f"{ASSETS}/enemies/sand_scorpion.png")
enemies_silk_cocoon = pygame.image.load(f"{ASSETS}/enemies/silk_cocoon.png")
enemies_spore_bat = pygame.image.load(f"{ASSETS}/enemies/spore_bat.png")
enemies_thorn_vine = pygame.image.load(f"{ASSETS}/enemies/thorn_vine.png")
enemies_void_blob = pygame.image.load(f"{ASSETS}/enemies/void_blob.png")
enemies_void_eye = pygame.image.load(f"{ASSETS}/enemies/void_eye.png")
enemies_web_weaver = pygame.image.load(f"{ASSETS}/enemies/web_weaver.png")

# ===== PICKUPS =====
pickups_charm_crown = pygame.image.load(f"{ASSETS}/pickups/charm_crown.png")
pickups_charm_fang = pygame.image.load(f"{ASSETS}/pickups/charm_fang.png")
pickups_charm_feather = pygame.image.load(f"{ASSETS}/pickups/charm_feather.png")
pickups_charm_lily = pygame.image.load(f"{ASSETS}/pickups/charm_lily.png")
pickups_charm_silk = pygame.image.load(f"{ASSETS}/pickups/charm_silk.png")
pickups_charm_spore = pygame.image.load(f"{ASSETS}/pickups/charm_spore.png")
pickups_charm_sun = pygame.image.load(f"{ASSETS}/pickups/charm_sun.png")
pickups_charm_void = pygame.image.load(f"{ASSETS}/pickups/charm_void.png")
pickups_geo_large = pygame.image.load(f"{ASSETS}/pickups/geo_large.png")
pickups_geo_medium = pygame.image.load(f"{ASSETS}/pickups/geo_medium.png")
pickups_geo_small = pygame.image.load(f"{ASSETS}/pickups/geo_small.png")
pickups_key = pygame.image.load(f"{ASSETS}/pickups/key.png")
pickups_map_scroll = pygame.image.load(f"{ASSETS}/pickups/map_scroll.png")
pickups_mask_shard = pygame.image.load(f"{ASSETS}/pickups/mask_shard.png")
pickups_rancid_egg = pygame.image.load(f"{ASSETS}/pickups/rancid_egg.png")
pickups_soul_fragment = pygame.image.load(f"{ASSETS}/pickups/soul_fragment.png")

# ===== UI =====
ui_charm_slot = pygame.image.load(f"{ASSETS}/ui/charm_slot.png")
ui_charm_slot_filled = pygame.image.load(f"{ASSETS}/ui/charm_slot_filled.png")
ui_cursor = pygame.image.load(f"{ASSETS}/ui/cursor.png")
ui_geo_icon = pygame.image.load(f"{ASSETS}/ui/geo_icon.png")
ui_key_icon = pygame.image.load(f"{ASSETS}/ui/key_icon.png")
ui_map_icon = pygame.image.load(f"{ASSETS}/ui/map_icon.png")
ui_mask_empty = pygame.image.load(f"{ASSETS}/ui/mask_empty.png")
ui_mask_full = pygame.image.load(f"{ASSETS}/ui/mask_full.png")
ui_mask_void = pygame.image.load(f"{ASSETS}/ui/mask_void.png")
ui_soul_vial_empty = pygame.image.load(f"{ASSETS}/ui/soul_vial_empty.png")
ui_soul_vial_full = pygame.image.load(f"{ASSETS}/ui/soul_vial_full.png")
ui_soul_vial_half = pygame.image.load(f"{ASSETS}/ui/soul_vial_half.png")

# ===== WORLD =====
world_bone_pile = pygame.image.load(f"{ASSETS}/world/bone_pile.png")
world_cave_mouth = pygame.image.load(f"{ASSETS}/world/cave_mouth.png")
world_hanging_chain = pygame.image.load(f"{ASSETS}/world/hanging_chain.png")
world_log_with_scythe = pygame.image.load(f"{ASSETS}/world/log_with_scythe.png")
world_pillar_ruin = pygame.image.load(f"{ASSETS}/world/pillar_ruin.png")
world_stalactite = pygame.image.load(f"{ASSETS}/world/stalactite.png")
world_stalagmite = pygame.image.load(f"{ASSETS}/world/stalagmite.png")
world_tombstone = pygame.image.load(f"{ASSETS}/world/tombstone.png")

# ===== BOSSES SHEETS =====
bosses_ant_queen_json = f"{ASSETS}/bosses/ant_queen/ant_queen.json"   # path only
bosses_ant_queen_sheet_path = f"{ASSETS}/bosses/ant_queen/ant_queen_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_drowned_watcher_json = f"{ASSETS}/bosses/drowned_watcher/drowned_watcher.json"   # path only
bosses_drowned_watcher_sheet_path = f"{ASSETS}/bosses/drowned_watcher/drowned_watcher_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_hollow_king_json = f"{ASSETS}/bosses/hollow_king/hollow_king.json"   # path only
bosses_hollow_king_sheet_path = f"{ASSETS}/bosses/hollow_king/hollow_king_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_ivory_gardener_json = f"{ASSETS}/bosses/ivory_gardener/ivory_gardener.json"   # path only
bosses_ivory_gardener_sheet_path = f"{ASSETS}/bosses/ivory_gardener/ivory_gardener_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_mire_toad_json = f"{ASSETS}/bosses/mire_toad/mire_toad.json"   # path only
bosses_mire_toad_sheet_path = f"{ASSETS}/bosses/mire_toad/mire_toad_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_pantheon_warden_json = f"{ASSETS}/bosses/pantheon_warden/pantheon_warden.json"   # path only
bosses_pantheon_warden_sheet_path = f"{ASSETS}/bosses/pantheon_warden/pantheon_warden_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_scarab_sovereign_json = f"{ASSETS}/bosses/scarab_sovereign/scarab_sovereign.json"   # path only
bosses_scarab_sovereign_sheet_path = f"{ASSETS}/bosses/scarab_sovereign/scarab_sovereign_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_silk_matriarch_json = f"{ASSETS}/bosses/silk_matriarch/silk_matriarch.json"   # path only
bosses_silk_matriarch_sheet_path = f"{ASSETS}/bosses/silk_matriarch/silk_matriarch_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_spore_mother_json = f"{ASSETS}/bosses/spore_mother/spore_mother.json"   # path only
bosses_spore_mother_sheet_path = f"{ASSETS}/bosses/spore_mother/spore_mother_sheet.png"   # path only (sheet is huge; the frames below are already loaded)
bosses_the_void_json = f"{ASSETS}/bosses/the_void/the_void.json"   # path only
bosses_the_void_sheet_path = f"{ASSETS}/bosses/the_void/the_void_sheet.png"   # path only (sheet is huge; the frames below are already loaded)

# ===== BOSSES FRAMES =====
bosses_ant_queen_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_a_0.png")
bosses_ant_queen_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_a_1.png")
bosses_ant_queen_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_a_2.png")
bosses_ant_queen_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_a_3.png")
bosses_ant_queen_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_b_0.png")
bosses_ant_queen_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_b_1.png")
bosses_ant_queen_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_b_2.png")
bosses_ant_queen_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/attack_b_3.png")
bosses_ant_queen_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/death_0.png")
bosses_ant_queen_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/death_1.png")
bosses_ant_queen_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/death_2.png")
bosses_ant_queen_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/death_3.png")
bosses_ant_queen_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/hurt_0.png")
bosses_ant_queen_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/idle_0.png")
bosses_ant_queen_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/idle_1.png")
bosses_ant_queen_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/idle_2.png")
bosses_ant_queen_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/ant_queen/frames/idle_3.png")
bosses_drowned_watcher_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_a_0.png")
bosses_drowned_watcher_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_a_1.png")
bosses_drowned_watcher_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_a_2.png")
bosses_drowned_watcher_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_a_3.png")
bosses_drowned_watcher_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_b_0.png")
bosses_drowned_watcher_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_b_1.png")
bosses_drowned_watcher_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_b_2.png")
bosses_drowned_watcher_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/attack_b_3.png")
bosses_drowned_watcher_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/death_0.png")
bosses_drowned_watcher_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/death_1.png")
bosses_drowned_watcher_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/death_2.png")
bosses_drowned_watcher_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/death_3.png")
bosses_drowned_watcher_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/hurt_0.png")
bosses_drowned_watcher_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/idle_0.png")
bosses_drowned_watcher_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/idle_1.png")
bosses_drowned_watcher_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/idle_2.png")
bosses_drowned_watcher_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/drowned_watcher/frames/idle_3.png")
bosses_hollow_king_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_a_0.png")
bosses_hollow_king_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_a_1.png")
bosses_hollow_king_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_a_2.png")
bosses_hollow_king_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_a_3.png")
bosses_hollow_king_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_b_0.png")
bosses_hollow_king_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_b_1.png")
bosses_hollow_king_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_b_2.png")
bosses_hollow_king_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/attack_b_3.png")
bosses_hollow_king_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/death_0.png")
bosses_hollow_king_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/death_1.png")
bosses_hollow_king_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/death_2.png")
bosses_hollow_king_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/death_3.png")
bosses_hollow_king_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/hurt_0.png")
bosses_hollow_king_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/idle_0.png")
bosses_hollow_king_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/idle_1.png")
bosses_hollow_king_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/idle_2.png")
bosses_hollow_king_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/hollow_king/frames/idle_3.png")
bosses_ivory_gardener_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_a_0.png")
bosses_ivory_gardener_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_a_1.png")
bosses_ivory_gardener_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_a_2.png")
bosses_ivory_gardener_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_a_3.png")
bosses_ivory_gardener_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_b_0.png")
bosses_ivory_gardener_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_b_1.png")
bosses_ivory_gardener_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_b_2.png")
bosses_ivory_gardener_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/attack_b_3.png")
bosses_ivory_gardener_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/death_0.png")
bosses_ivory_gardener_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/death_1.png")
bosses_ivory_gardener_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/death_2.png")
bosses_ivory_gardener_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/death_3.png")
bosses_ivory_gardener_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/hurt_0.png")
bosses_ivory_gardener_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/idle_0.png")
bosses_ivory_gardener_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/idle_1.png")
bosses_ivory_gardener_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/idle_2.png")
bosses_ivory_gardener_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/ivory_gardener/frames/idle_3.png")
bosses_mire_toad_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_a_0.png")
bosses_mire_toad_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_a_1.png")
bosses_mire_toad_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_a_2.png")
bosses_mire_toad_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_a_3.png")
bosses_mire_toad_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_b_0.png")
bosses_mire_toad_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_b_1.png")
bosses_mire_toad_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_b_2.png")
bosses_mire_toad_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/attack_b_3.png")
bosses_mire_toad_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/death_0.png")
bosses_mire_toad_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/death_1.png")
bosses_mire_toad_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/death_2.png")
bosses_mire_toad_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/death_3.png")
bosses_mire_toad_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/hurt_0.png")
bosses_mire_toad_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/idle_0.png")
bosses_mire_toad_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/idle_1.png")
bosses_mire_toad_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/idle_2.png")
bosses_mire_toad_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/mire_toad/frames/idle_3.png")
bosses_pantheon_warden_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_a_0.png")
bosses_pantheon_warden_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_a_1.png")
bosses_pantheon_warden_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_a_2.png")
bosses_pantheon_warden_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_a_3.png")
bosses_pantheon_warden_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_b_0.png")
bosses_pantheon_warden_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_b_1.png")
bosses_pantheon_warden_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_b_2.png")
bosses_pantheon_warden_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/attack_b_3.png")
bosses_pantheon_warden_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/death_0.png")
bosses_pantheon_warden_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/death_1.png")
bosses_pantheon_warden_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/death_2.png")
bosses_pantheon_warden_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/death_3.png")
bosses_pantheon_warden_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/hurt_0.png")
bosses_pantheon_warden_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/idle_0.png")
bosses_pantheon_warden_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/idle_1.png")
bosses_pantheon_warden_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/idle_2.png")
bosses_pantheon_warden_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/pantheon_warden/frames/idle_3.png")
bosses_scarab_sovereign_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_a_0.png")
bosses_scarab_sovereign_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_a_1.png")
bosses_scarab_sovereign_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_a_2.png")
bosses_scarab_sovereign_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_a_3.png")
bosses_scarab_sovereign_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_b_0.png")
bosses_scarab_sovereign_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_b_1.png")
bosses_scarab_sovereign_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_b_2.png")
bosses_scarab_sovereign_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/attack_b_3.png")
bosses_scarab_sovereign_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/death_0.png")
bosses_scarab_sovereign_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/death_1.png")
bosses_scarab_sovereign_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/death_2.png")
bosses_scarab_sovereign_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/death_3.png")
bosses_scarab_sovereign_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/hurt_0.png")
bosses_scarab_sovereign_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/idle_0.png")
bosses_scarab_sovereign_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/idle_1.png")
bosses_scarab_sovereign_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/idle_2.png")
bosses_scarab_sovereign_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/scarab_sovereign/frames/idle_3.png")
bosses_silk_matriarch_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_a_0.png")
bosses_silk_matriarch_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_a_1.png")
bosses_silk_matriarch_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_a_2.png")
bosses_silk_matriarch_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_a_3.png")
bosses_silk_matriarch_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_b_0.png")
bosses_silk_matriarch_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_b_1.png")
bosses_silk_matriarch_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_b_2.png")
bosses_silk_matriarch_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/attack_b_3.png")
bosses_silk_matriarch_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/death_0.png")
bosses_silk_matriarch_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/death_1.png")
bosses_silk_matriarch_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/death_2.png")
bosses_silk_matriarch_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/death_3.png")
bosses_silk_matriarch_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/hurt_0.png")
bosses_silk_matriarch_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/idle_0.png")
bosses_silk_matriarch_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/idle_1.png")
bosses_silk_matriarch_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/idle_2.png")
bosses_silk_matriarch_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/silk_matriarch/frames/idle_3.png")
bosses_spore_mother_frames_attack_a_0 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_a_0.png")
bosses_spore_mother_frames_attack_a_1 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_a_1.png")
bosses_spore_mother_frames_attack_a_2 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_a_2.png")
bosses_spore_mother_frames_attack_a_3 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_a_3.png")
bosses_spore_mother_frames_attack_b_0 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_b_0.png")
bosses_spore_mother_frames_attack_b_1 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_b_1.png")
bosses_spore_mother_frames_attack_b_2 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_b_2.png")
bosses_spore_mother_frames_attack_b_3 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/attack_b_3.png")
bosses_spore_mother_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/death_0.png")
bosses_spore_mother_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/death_1.png")
bosses_spore_mother_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/death_2.png")
bosses_spore_mother_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/death_3.png")
bosses_spore_mother_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/hurt_0.png")
bosses_spore_mother_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/idle_0.png")
bosses_spore_mother_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/idle_1.png")
bosses_spore_mother_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/idle_2.png")
bosses_spore_mother_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/spore_mother/frames/idle_3.png")
bosses_the_void_frames_claw_sweep_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/claw_sweep_0.png")
bosses_the_void_frames_claw_sweep_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/claw_sweep_1.png")
bosses_the_void_frames_claw_sweep_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/claw_sweep_2.png")
bosses_the_void_frames_claw_sweep_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/claw_sweep_3.png")
bosses_the_void_frames_claw_sweep_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/claw_sweep_4.png")
bosses_the_void_frames_death_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_0.png")
bosses_the_void_frames_death_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_1.png")
bosses_the_void_frames_death_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_2.png")
bosses_the_void_frames_death_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_3.png")
bosses_the_void_frames_death_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_4.png")
bosses_the_void_frames_death_5 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_5.png")
bosses_the_void_frames_death_6 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_6.png")
bosses_the_void_frames_death_7 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/death_7.png")
bosses_the_void_frames_hurt_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/hurt_0.png")
bosses_the_void_frames_hurt_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/hurt_1.png")
bosses_the_void_frames_idle_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_0.png")
bosses_the_void_frames_idle_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_1.png")
bosses_the_void_frames_idle_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_2.png")
bosses_the_void_frames_idle_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_3.png")
bosses_the_void_frames_idle_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_4.png")
bosses_the_void_frames_idle_5 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/idle_5.png")
bosses_the_void_frames_orb_barrage_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/orb_barrage_0.png")
bosses_the_void_frames_orb_barrage_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/orb_barrage_1.png")
bosses_the_void_frames_orb_barrage_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/orb_barrage_2.png")
bosses_the_void_frames_orb_barrage_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/orb_barrage_3.png")
bosses_the_void_frames_orb_barrage_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/orb_barrage_4.png")
bosses_the_void_frames_phase_shift_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_shift_0.png")
bosses_the_void_frames_phase_shift_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_shift_1.png")
bosses_the_void_frames_phase_shift_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_shift_2.png")
bosses_the_void_frames_phase_shift_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_shift_3.png")
bosses_the_void_frames_phase_shift_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_shift_4.png")
bosses_the_void_frames_phase_two_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_two_0.png")
bosses_the_void_frames_phase_two_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_two_1.png")
bosses_the_void_frames_phase_two_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_two_2.png")
bosses_the_void_frames_phase_two_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/phase_two_3.png")
bosses_the_void_frames_rift_beam_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/rift_beam_0.png")
bosses_the_void_frames_rift_beam_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/rift_beam_1.png")
bosses_the_void_frames_rift_beam_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/rift_beam_2.png")
bosses_the_void_frames_rift_beam_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/rift_beam_3.png")
bosses_the_void_frames_rift_beam_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/rift_beam_4.png")
bosses_the_void_frames_summon_shades_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/summon_shades_0.png")
bosses_the_void_frames_summon_shades_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/summon_shades_1.png")
bosses_the_void_frames_summon_shades_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/summon_shades_2.png")
bosses_the_void_frames_summon_shades_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/summon_shades_3.png")
bosses_the_void_frames_summon_shades_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/summon_shades_4.png")
bosses_the_void_frames_tendril_slam_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/tendril_slam_0.png")
bosses_the_void_frames_tendril_slam_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/tendril_slam_1.png")
bosses_the_void_frames_tendril_slam_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/tendril_slam_2.png")
bosses_the_void_frames_tendril_slam_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/tendril_slam_3.png")
bosses_the_void_frames_tendril_slam_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/tendril_slam_4.png")
bosses_the_void_frames_void_nova_0 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/void_nova_0.png")
bosses_the_void_frames_void_nova_1 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/void_nova_1.png")
bosses_the_void_frames_void_nova_2 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/void_nova_2.png")
bosses_the_void_frames_void_nova_3 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/void_nova_3.png")
bosses_the_void_frames_void_nova_4 = pygame.image.load(f"{ASSETS}/bosses/the_void/frames/void_nova_4.png")

# ============================================================
# FRAME GROUPS  (animation lists, in play order)
# ============================================================

bosses_ant_queen_attack_a = [bosses_ant_queen_frames_attack_a_0, bosses_ant_queen_frames_attack_a_1, bosses_ant_queen_frames_attack_a_2, bosses_ant_queen_frames_attack_a_3]
bosses_ant_queen_attack_b = [bosses_ant_queen_frames_attack_b_0, bosses_ant_queen_frames_attack_b_1, bosses_ant_queen_frames_attack_b_2, bosses_ant_queen_frames_attack_b_3]
bosses_ant_queen_death = [bosses_ant_queen_frames_death_0, bosses_ant_queen_frames_death_1, bosses_ant_queen_frames_death_2, bosses_ant_queen_frames_death_3]
bosses_ant_queen_hurt = [bosses_ant_queen_frames_hurt_0]
bosses_ant_queen_idle = [bosses_ant_queen_frames_idle_0, bosses_ant_queen_frames_idle_1, bosses_ant_queen_frames_idle_2, bosses_ant_queen_frames_idle_3]
bosses_drowned_watcher_attack_a = [bosses_drowned_watcher_frames_attack_a_0, bosses_drowned_watcher_frames_attack_a_1, bosses_drowned_watcher_frames_attack_a_2, bosses_drowned_watcher_frames_attack_a_3]
bosses_drowned_watcher_attack_b = [bosses_drowned_watcher_frames_attack_b_0, bosses_drowned_watcher_frames_attack_b_1, bosses_drowned_watcher_frames_attack_b_2, bosses_drowned_watcher_frames_attack_b_3]
bosses_drowned_watcher_death = [bosses_drowned_watcher_frames_death_0, bosses_drowned_watcher_frames_death_1, bosses_drowned_watcher_frames_death_2, bosses_drowned_watcher_frames_death_3]
bosses_drowned_watcher_hurt = [bosses_drowned_watcher_frames_hurt_0]
bosses_drowned_watcher_idle = [bosses_drowned_watcher_frames_idle_0, bosses_drowned_watcher_frames_idle_1, bosses_drowned_watcher_frames_idle_2, bosses_drowned_watcher_frames_idle_3]
bosses_hollow_king_attack_a = [bosses_hollow_king_frames_attack_a_0, bosses_hollow_king_frames_attack_a_1, bosses_hollow_king_frames_attack_a_2, bosses_hollow_king_frames_attack_a_3]
bosses_hollow_king_attack_b = [bosses_hollow_king_frames_attack_b_0, bosses_hollow_king_frames_attack_b_1, bosses_hollow_king_frames_attack_b_2, bosses_hollow_king_frames_attack_b_3]
bosses_hollow_king_death = [bosses_hollow_king_frames_death_0, bosses_hollow_king_frames_death_1, bosses_hollow_king_frames_death_2, bosses_hollow_king_frames_death_3]
bosses_hollow_king_hurt = [bosses_hollow_king_frames_hurt_0]
bosses_hollow_king_idle = [bosses_hollow_king_frames_idle_0, bosses_hollow_king_frames_idle_1, bosses_hollow_king_frames_idle_2, bosses_hollow_king_frames_idle_3]
bosses_ivory_gardener_attack_a = [bosses_ivory_gardener_frames_attack_a_0, bosses_ivory_gardener_frames_attack_a_1, bosses_ivory_gardener_frames_attack_a_2, bosses_ivory_gardener_frames_attack_a_3]
bosses_ivory_gardener_attack_b = [bosses_ivory_gardener_frames_attack_b_0, bosses_ivory_gardener_frames_attack_b_1, bosses_ivory_gardener_frames_attack_b_2, bosses_ivory_gardener_frames_attack_b_3]
bosses_ivory_gardener_death = [bosses_ivory_gardener_frames_death_0, bosses_ivory_gardener_frames_death_1, bosses_ivory_gardener_frames_death_2, bosses_ivory_gardener_frames_death_3]
bosses_ivory_gardener_hurt = [bosses_ivory_gardener_frames_hurt_0]
bosses_ivory_gardener_idle = [bosses_ivory_gardener_frames_idle_0, bosses_ivory_gardener_frames_idle_1, bosses_ivory_gardener_frames_idle_2, bosses_ivory_gardener_frames_idle_3]
bosses_mire_toad_attack_a = [bosses_mire_toad_frames_attack_a_0, bosses_mire_toad_frames_attack_a_1, bosses_mire_toad_frames_attack_a_2, bosses_mire_toad_frames_attack_a_3]
bosses_mire_toad_attack_b = [bosses_mire_toad_frames_attack_b_0, bosses_mire_toad_frames_attack_b_1, bosses_mire_toad_frames_attack_b_2, bosses_mire_toad_frames_attack_b_3]
bosses_mire_toad_death = [bosses_mire_toad_frames_death_0, bosses_mire_toad_frames_death_1, bosses_mire_toad_frames_death_2, bosses_mire_toad_frames_death_3]
bosses_mire_toad_hurt = [bosses_mire_toad_frames_hurt_0]
bosses_mire_toad_idle = [bosses_mire_toad_frames_idle_0, bosses_mire_toad_frames_idle_1, bosses_mire_toad_frames_idle_2, bosses_mire_toad_frames_idle_3]
bosses_pantheon_warden_attack_a = [bosses_pantheon_warden_frames_attack_a_0, bosses_pantheon_warden_frames_attack_a_1, bosses_pantheon_warden_frames_attack_a_2, bosses_pantheon_warden_frames_attack_a_3]
bosses_pantheon_warden_attack_b = [bosses_pantheon_warden_frames_attack_b_0, bosses_pantheon_warden_frames_attack_b_1, bosses_pantheon_warden_frames_attack_b_2, bosses_pantheon_warden_frames_attack_b_3]
bosses_pantheon_warden_death = [bosses_pantheon_warden_frames_death_0, bosses_pantheon_warden_frames_death_1, bosses_pantheon_warden_frames_death_2, bosses_pantheon_warden_frames_death_3]
bosses_pantheon_warden_hurt = [bosses_pantheon_warden_frames_hurt_0]
bosses_pantheon_warden_idle = [bosses_pantheon_warden_frames_idle_0, bosses_pantheon_warden_frames_idle_1, bosses_pantheon_warden_frames_idle_2, bosses_pantheon_warden_frames_idle_3]
bosses_scarab_sovereign_attack_a = [bosses_scarab_sovereign_frames_attack_a_0, bosses_scarab_sovereign_frames_attack_a_1, bosses_scarab_sovereign_frames_attack_a_2, bosses_scarab_sovereign_frames_attack_a_3]
bosses_scarab_sovereign_attack_b = [bosses_scarab_sovereign_frames_attack_b_0, bosses_scarab_sovereign_frames_attack_b_1, bosses_scarab_sovereign_frames_attack_b_2, bosses_scarab_sovereign_frames_attack_b_3]
bosses_scarab_sovereign_death = [bosses_scarab_sovereign_frames_death_0, bosses_scarab_sovereign_frames_death_1, bosses_scarab_sovereign_frames_death_2, bosses_scarab_sovereign_frames_death_3]
bosses_scarab_sovereign_hurt = [bosses_scarab_sovereign_frames_hurt_0]
bosses_scarab_sovereign_idle = [bosses_scarab_sovereign_frames_idle_0, bosses_scarab_sovereign_frames_idle_1, bosses_scarab_sovereign_frames_idle_2, bosses_scarab_sovereign_frames_idle_3]
bosses_silk_matriarch_attack_a = [bosses_silk_matriarch_frames_attack_a_0, bosses_silk_matriarch_frames_attack_a_1, bosses_silk_matriarch_frames_attack_a_2, bosses_silk_matriarch_frames_attack_a_3]
bosses_silk_matriarch_attack_b = [bosses_silk_matriarch_frames_attack_b_0, bosses_silk_matriarch_frames_attack_b_1, bosses_silk_matriarch_frames_attack_b_2, bosses_silk_matriarch_frames_attack_b_3]
bosses_silk_matriarch_death = [bosses_silk_matriarch_frames_death_0, bosses_silk_matriarch_frames_death_1, bosses_silk_matriarch_frames_death_2, bosses_silk_matriarch_frames_death_3]
bosses_silk_matriarch_hurt = [bosses_silk_matriarch_frames_hurt_0]
bosses_silk_matriarch_idle = [bosses_silk_matriarch_frames_idle_0, bosses_silk_matriarch_frames_idle_1, bosses_silk_matriarch_frames_idle_2, bosses_silk_matriarch_frames_idle_3]
bosses_spore_mother_attack_a = [bosses_spore_mother_frames_attack_a_0, bosses_spore_mother_frames_attack_a_1, bosses_spore_mother_frames_attack_a_2, bosses_spore_mother_frames_attack_a_3]
bosses_spore_mother_attack_b = [bosses_spore_mother_frames_attack_b_0, bosses_spore_mother_frames_attack_b_1, bosses_spore_mother_frames_attack_b_2, bosses_spore_mother_frames_attack_b_3]
bosses_spore_mother_death = [bosses_spore_mother_frames_death_0, bosses_spore_mother_frames_death_1, bosses_spore_mother_frames_death_2, bosses_spore_mother_frames_death_3]
bosses_spore_mother_hurt = [bosses_spore_mother_frames_hurt_0]
bosses_spore_mother_idle = [bosses_spore_mother_frames_idle_0, bosses_spore_mother_frames_idle_1, bosses_spore_mother_frames_idle_2, bosses_spore_mother_frames_idle_3]
bosses_the_void_claw_sweep = [bosses_the_void_frames_claw_sweep_0, bosses_the_void_frames_claw_sweep_1, bosses_the_void_frames_claw_sweep_2, bosses_the_void_frames_claw_sweep_3, bosses_the_void_frames_claw_sweep_4]
bosses_the_void_death = [bosses_the_void_frames_death_0, bosses_the_void_frames_death_1, bosses_the_void_frames_death_2, bosses_the_void_frames_death_3, bosses_the_void_frames_death_4, bosses_the_void_frames_death_5, bosses_the_void_frames_death_6, bosses_the_void_frames_death_7]
bosses_the_void_hurt = [bosses_the_void_frames_hurt_0, bosses_the_void_frames_hurt_1]
bosses_the_void_idle = [bosses_the_void_frames_idle_0, bosses_the_void_frames_idle_1, bosses_the_void_frames_idle_2, bosses_the_void_frames_idle_3, bosses_the_void_frames_idle_4, bosses_the_void_frames_idle_5]
bosses_the_void_orb_barrage = [bosses_the_void_frames_orb_barrage_0, bosses_the_void_frames_orb_barrage_1, bosses_the_void_frames_orb_barrage_2, bosses_the_void_frames_orb_barrage_3, bosses_the_void_frames_orb_barrage_4]
bosses_the_void_phase_shift = [bosses_the_void_frames_phase_shift_0, bosses_the_void_frames_phase_shift_1, bosses_the_void_frames_phase_shift_2, bosses_the_void_frames_phase_shift_3, bosses_the_void_frames_phase_shift_4]
bosses_the_void_phase_two = [bosses_the_void_frames_phase_two_0, bosses_the_void_frames_phase_two_1, bosses_the_void_frames_phase_two_2, bosses_the_void_frames_phase_two_3]
bosses_the_void_rift_beam = [bosses_the_void_frames_rift_beam_0, bosses_the_void_frames_rift_beam_1, bosses_the_void_frames_rift_beam_2, bosses_the_void_frames_rift_beam_3, bosses_the_void_frames_rift_beam_4]
bosses_the_void_summon_shades = [bosses_the_void_frames_summon_shades_0, bosses_the_void_frames_summon_shades_1, bosses_the_void_frames_summon_shades_2, bosses_the_void_frames_summon_shades_3, bosses_the_void_frames_summon_shades_4]
bosses_the_void_tendril_slam = [bosses_the_void_frames_tendril_slam_0, bosses_the_void_frames_tendril_slam_1, bosses_the_void_frames_tendril_slam_2, bosses_the_void_frames_tendril_slam_3, bosses_the_void_frames_tendril_slam_4]
bosses_the_void_void_nova = [bosses_the_void_frames_void_nova_0, bosses_the_void_frames_void_nova_1, bosses_the_void_frames_void_nova_2, bosses_the_void_frames_void_nova_3, bosses_the_void_frames_void_nova_4]

fx_dust = [fx_dust_1, fx_dust_2]

npcs_bremite_idle = [npcs_bremite_idle_1, npcs_bremite_idle_2, npcs_bremite_idle_3]

player_pale_wanderer_death = [player_pale_wanderer_death_1, player_pale_wanderer_death_2]
player_pale_wanderer_heal = [player_pale_wanderer_heal_1, player_pale_wanderer_heal_2]
player_pale_wanderer_hurt = [player_pale_wanderer_hurt_1, player_pale_wanderer_hurt_2]
player_pale_wanderer_idle = [player_pale_wanderer_idle_1, player_pale_wanderer_idle_2]
player_pale_wanderer_walk = [player_pale_wanderer_walk_1, player_pale_wanderer_walk_2, player_pale_wanderer_walk_3, player_pale_wanderer_walk_4]

# hand-grouped player animations
player_pale_wanderer_jump = [player_pale_wanderer_jump_rise, player_pale_wanderer_jump_peak, player_pale_wanderer_fall]
player_pale_wanderer_attack = [player_pale_wanderer_attack_windup, player_pale_wanderer_attack_slash, player_pale_wanderer_attack_recover]

# ---- every group in one dictionary ----
ANIMATIONS = {
    "bosses_ant_queen_attack_a": bosses_ant_queen_attack_a,
    "bosses_ant_queen_attack_b": bosses_ant_queen_attack_b,
    "bosses_ant_queen_death": bosses_ant_queen_death,
    "bosses_ant_queen_hurt": bosses_ant_queen_hurt,
    "bosses_ant_queen_idle": bosses_ant_queen_idle,
    "bosses_drowned_watcher_attack_a": bosses_drowned_watcher_attack_a,
    "bosses_drowned_watcher_attack_b": bosses_drowned_watcher_attack_b,
    "bosses_drowned_watcher_death": bosses_drowned_watcher_death,
    "bosses_drowned_watcher_hurt": bosses_drowned_watcher_hurt,
    "bosses_drowned_watcher_idle": bosses_drowned_watcher_idle,
    "bosses_hollow_king_attack_a": bosses_hollow_king_attack_a,
    "bosses_hollow_king_attack_b": bosses_hollow_king_attack_b,
    "bosses_hollow_king_death": bosses_hollow_king_death,
    "bosses_hollow_king_hurt": bosses_hollow_king_hurt,
    "bosses_hollow_king_idle": bosses_hollow_king_idle,
    "bosses_ivory_gardener_attack_a": bosses_ivory_gardener_attack_a,
    "bosses_ivory_gardener_attack_b": bosses_ivory_gardener_attack_b,
    "bosses_ivory_gardener_death": bosses_ivory_gardener_death,
    "bosses_ivory_gardener_hurt": bosses_ivory_gardener_hurt,
    "bosses_ivory_gardener_idle": bosses_ivory_gardener_idle,
    "bosses_mire_toad_attack_a": bosses_mire_toad_attack_a,
    "bosses_mire_toad_attack_b": bosses_mire_toad_attack_b,
    "bosses_mire_toad_death": bosses_mire_toad_death,
    "bosses_mire_toad_hurt": bosses_mire_toad_hurt,
    "bosses_mire_toad_idle": bosses_mire_toad_idle,
    "bosses_pantheon_warden_attack_a": bosses_pantheon_warden_attack_a,
    "bosses_pantheon_warden_attack_b": bosses_pantheon_warden_attack_b,
    "bosses_pantheon_warden_death": bosses_pantheon_warden_death,
    "bosses_pantheon_warden_hurt": bosses_pantheon_warden_hurt,
    "bosses_pantheon_warden_idle": bosses_pantheon_warden_idle,
    "bosses_scarab_sovereign_attack_a": bosses_scarab_sovereign_attack_a,
    "bosses_scarab_sovereign_attack_b": bosses_scarab_sovereign_attack_b,
    "bosses_scarab_sovereign_death": bosses_scarab_sovereign_death,
    "bosses_scarab_sovereign_hurt": bosses_scarab_sovereign_hurt,
    "bosses_scarab_sovereign_idle": bosses_scarab_sovereign_idle,
    "bosses_silk_matriarch_attack_a": bosses_silk_matriarch_attack_a,
    "bosses_silk_matriarch_attack_b": bosses_silk_matriarch_attack_b,
    "bosses_silk_matriarch_death": bosses_silk_matriarch_death,
    "bosses_silk_matriarch_hurt": bosses_silk_matriarch_hurt,
    "bosses_silk_matriarch_idle": bosses_silk_matriarch_idle,
    "bosses_spore_mother_attack_a": bosses_spore_mother_attack_a,
    "bosses_spore_mother_attack_b": bosses_spore_mother_attack_b,
    "bosses_spore_mother_death": bosses_spore_mother_death,
    "bosses_spore_mother_hurt": bosses_spore_mother_hurt,
    "bosses_spore_mother_idle": bosses_spore_mother_idle,
    "bosses_the_void_claw_sweep": bosses_the_void_claw_sweep,
    "bosses_the_void_death": bosses_the_void_death,
    "bosses_the_void_hurt": bosses_the_void_hurt,
    "bosses_the_void_idle": bosses_the_void_idle,
    "bosses_the_void_orb_barrage": bosses_the_void_orb_barrage,
    "bosses_the_void_phase_shift": bosses_the_void_phase_shift,
    "bosses_the_void_phase_two": bosses_the_void_phase_two,
    "bosses_the_void_rift_beam": bosses_the_void_rift_beam,
    "bosses_the_void_summon_shades": bosses_the_void_summon_shades,
    "bosses_the_void_tendril_slam": bosses_the_void_tendril_slam,
    "bosses_the_void_void_nova": bosses_the_void_void_nova,
    "fx_dust": fx_dust,
    "npcs_bremite_idle": npcs_bremite_idle,
    "player_pale_wanderer_attack": player_pale_wanderer_attack,
    "player_pale_wanderer_death": player_pale_wanderer_death,
    "player_pale_wanderer_heal": player_pale_wanderer_heal,
    "player_pale_wanderer_hurt": player_pale_wanderer_hurt,
    "player_pale_wanderer_idle": player_pale_wanderer_idle,
    "player_pale_wanderer_jump": player_pale_wanderer_jump,
    "player_pale_wanderer_walk": player_pale_wanderer_walk,
}
clock = pygame.time.Clock()
running=True
while running:
    dt = clock.tick(60) / 1000.0  # delta time in seconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    
    # Update player
    player_group.update(dt, keys)
    
    # Draw
    screen.fill((0, 0, 0))
    screen.blit(tiles_hole_fungal_fill,(300,400))

    player_group.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
