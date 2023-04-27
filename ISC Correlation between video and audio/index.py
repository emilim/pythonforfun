from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import imageio
import numpy as np
from pydub import AudioSegment
import wave

def power(my_list, power):
    return [x**power for x in my_list]

loc = "video/dalmatians2"
movie_name = "Dalmatians"
seconds = 60

spf = wave.open(loc+".wav", "r")
fps_audio = spf.getframerate()
n_samples_audio = seconds * fps_audio 
signal = spf.readframes(n_samples_audio)

if spf.getnchannels() == 2:
    print("modified")
    sound = AudioSegment.from_wav(loc+".wav")
    sound = sound.set_channels(1)
    sound.export(loc+".wav", format="wav")
    spf = wave.open(loc+".wav", "r")
    signal = spf.readframes(n_samples_audio)


audio_signal_input = np.frombuffer(signal, dtype=np.int16)
audio_signal_input = np.abs(audio_signal_input)

video_signal_input = imageio.get_reader(loc+'.mp4',  'ffmpeg')
fps_video = video_signal_input.get_meta_data()['fps']
n_samples_video = int(seconds * fps_video)

video_signal = []
for num in range(0, n_samples_video-1):
    image_1 = np.array(video_signal_input.get_data(num))
    image_2 = np.array(video_signal_input.get_data(num+1))
    image_1 = np.dot(image_1[...,:3], [0.299, 0.587, 0.114])
    image_2 = np.dot(image_2[...,:3], [0.299, 0.587, 0.114])
    h, w = image_1.shape
    '''
    derivative_sum = 0
    for i in range(w):
        for j in range(h):
            derivative_sum += np.abs(image_1[j][i] - image_2[j][i])
    derivative_sum /= (w*h)
    '''
    # same thing with a 32*32 chunk of the image
    derivative_sum = 0
    chunk_size = 256
    for i in range(0, w, chunk_size):
        for j in range(0, h, chunk_size):
            derivative_sum += np.abs(np.mean(image_1[j:j+chunk_size, i:i+chunk_size]) - np.mean(image_2[j:j+chunk_size, i:i+chunk_size]))
    derivative_sum /= (w*h / (chunk_size*chunk_size))
    

    if num % (n_samples_video/20) == 0:
        print("progress: {}%".format(num/(n_samples_video/20)*5), end="\r")

    video_signal.append(derivative_sum * 100)
    # make a 1-dimensional view of arr
    #flat_arr = image.ravel()

times = np.linspace(0, seconds, num=n_samples_video-1)

# average audio signal to match video
audio_signal = np.zeros(len(video_signal))
for i in range(len(video_signal)):
    ratio = int(fps_audio/fps_video)
    #audio_signal[i] = np.mean(audio_signal_input[i*ratio:(i+1)*ratio])
    sum = 0
    for j in range(ratio):
        sum += audio_signal_input[i*ratio + j]
    audio_signal[i] = sum / ratio


# ISC correlation
def ISC(x, y):
    #return np.mean(x*y) / np.sqrt(np.mean(power(x, 2)) * np.mean(power(y, 2)))
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    sum = 0
    sum_2 = 0
    sum_3 = 0
    for i in range(len(x)):
        x_i = x[i] - x_mean
        y_i = y[i] - y_mean
        sum += x_i * y_i
        sum_2 += x_i**2
        sum_3 += y_i**2
    return sum / np.sqrt(sum_2 * sum_3)

def ISC_finestra(x, y, finestra):
    func = []
    n_sample = int(finestra * fps_video)
    for start in range(1, int(n_samples_video)):
        x_fin = x[start:start+n_sample]
        y_fin = y[start:start+n_sample]
        x_mean = np.mean(x_fin)
        y_mean = np.mean(y_fin)
        sum = 0
        sum_2 = 0
        sum_3 = 0
        for i in range(len(x_fin)):
            x_i = x_fin[i] - x_mean
            y_i = y_fin[i] - y_mean
            sum += x_i * y_i
            sum_2 += x_i**2
            sum_3 += y_i**2
        func.append((sum / np.sqrt(sum_2 * sum_3)) * 10000)
    return func


isc = ISC(audio_signal, video_signal)
isc2 = ISC_finestra(audio_signal, video_signal, 3)
print("ISC is {}".format(isc))

plt.plot(times, audio_signal, c='b', label="Audio Signal")
plt.plot(times, video_signal, c='r', label="Video Signal")
plt.plot(times, isc2, c='g', label="ISC - 3 second window")

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Movie: {}, ISC: {}".format(movie_name, round(isc, 3)))
# add legend
plt.legend()
# display the plot
plt.show()