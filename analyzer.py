import numpy as np
import librosa

def analyze_audio(y, sr):
    rms = np.mean(librosa.feature.rms(y=y))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    flatness = np.mean(librosa.feature.spectral_flatness(y=y))

    confidence = 0.0
    flags = []

    if flatness > 0.5:
        confidence += 0.3
        flags.append("abnormal spectral flatness")

    if zcr < 0.05:
        confidence += 0.3
        flags.append("low pitch variance")

    if rms < 0.02:
        confidence += 0.2
        flags.append("over-clean signal")

    return {
        "confidence": min(confidence, 1.0),
        "flags": flags
    }
