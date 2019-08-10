#wave data get  -xlxw

#import
import wave as we
import numpy as np
import matplotlib.pyplot as plt

def wavread(path):
    wavfile =  we.open(path,"rb")
    params = wavfile.getparams()
    framesra,frameswav= params[2],params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav,dtype = np.short)
    datause.shape = -1,2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0/framesra)
    return datause,time

def main():
    # path = input("The Path is:")
    path = '我们走.wav'
    # wavdata,wavtime = wavread(path)
    wavdata = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,13,24,564,234,654,234,675,234,23]]
    wavtime = []
    counter = 0
    for i in wavdata[0]:
        wavtime.append(counter)
        counter += 1
    print(len(wavdata))
    print(len(wavtime))
    plt.title("Night.wav's Frames")
    plt.subplot(211)
    plt.plot(wavtime, wavdata[0],color = 'green')
    # plt.subplot(212)
    # plt.plot(wavtime, wavdata[1])
    plt.show()
    
main()