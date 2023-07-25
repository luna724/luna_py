import os
import subprocess

def create(noise_strength, filename, extension="wav"):
    duration = 10
    subprocess.run(["sox", "-n", "-r", "44100", "-c", "1", f"./white_noise/{filename}.{extension}", "synth", str(duration), "whitenoise", "vol", str(noise_strength)])

os.makedirs("./white_noise", exist_ok=True)

for x in range(10, 61):
    x  /= 100
    print(f"Creating White Noise.. \nStrength: {str(x)}")
    create(x, f"wn_{str(x)}")

print("White Noise Generation Done.")