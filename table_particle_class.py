particle = str
class_ = str
spin = input()
ec = input()
if spin == '1/2':
    if ec == '-1/3':
        particle = 'Strange'
        class_ = 'Quark'
    elif ec == '2/3':
        particle = 'Charm'
        class_ = 'Quark'
    elif ec == '-1':
        particle = 'Electron'
        class_ = 'Lepton'
    elif ec == '0':
        particle = 'Neutrino'
        class_ = 'Lepton'    
elif spin == '1':
    particle = 'Photon'
    class_ = 'Boson'
print(particle + " " + class_)
