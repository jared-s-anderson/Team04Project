from pygame import mixer

def sounds(scene, volume):
  
    if scene == 'overworld':
        # Loading the song
        mixer.music.load("sounds\A_field_of_Peace.mp3")

    # Setting the volume
    mixer.music.set_volume(volume)
  
    # Start playing the song
    mixer.music.play()