from pygame import draw

def setScene(win, scene, cave_tmx_data, overworld_tmx_data):
    if scene == 'overworld':
        # Draw all tiles for the Overworld map
        for tile in overworld_tmx_data.get_layer_by_name("Tile Layer 2").tiles():
            x_pixel = tile[0] * 8
            y_pixel = tile[1] * 8
            win.blit(tile[2], (x_pixel, y_pixel))
    elif scene == 'cave':
        # Draw all tiles for the Cave map
        for tile in cave_tmx_data.get_layer_by_name("Tile Layer 2").tiles():
            x_pixel = tile[0] * 8
            y_pixel = tile[1] * 8
            win.blit(tile[2], (x_pixel, y_pixel))
    elif scene == 'bossRoom':
        # Draw all tiles for the boss room map
        for tile in cave_tmx_data.get_layer_by_name("Tile Layer 2").tiles():
            x_pixel = tile[0] * 8
            y_pixel = tile[1] * 8
            win.blit(tile[2], (x_pixel, y_pixel))
    else:
        print('You have a typo in scene variable!')