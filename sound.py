from pygame import mixer

def sounds(scene, volume):
  
    if scene == 'hydra':
        # Loading the song
        mixer.music.load("sounds/Hydra_Rises.wav")

    # Setting the volume
    mixer.music.set_volume(volume)
  
    # Start playing the song
    mixer.music.play()