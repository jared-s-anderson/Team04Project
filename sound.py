from pygame import mixer

def sounds(scene, volume):
  
    if scene == 'overworld':
        # Loading the song
        mixer.music.load("sounds\A_field_of_Peace.mp3")
    elif scene == 'cave':
         mixer.music.load("sounds\Cave_song.mp3")
    elif scene == 'bossRoom':
        mixer.music.load("sounds\The_Hydra_Burns.mp3")
    else:
        print('You have a typo in scene variable!')
    # Setting the volume
    mixer.music.set_volume(volume)
  
    # Start playing the song
    mixer.music.play()