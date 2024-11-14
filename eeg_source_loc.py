import mne
import numpy as np
import os
import matplotlib.pyplot as plt


# Define your subjects_dir path where fsaverage data will be downloaded or is already located
print("Define your subjects_dir path where fsaverage data will be downloaded or is already located")
subjects_dir = "C:/Users/fmnya/mne_data/MNE-sample-data/subjects"

# Ensure fsaverage data is available in subjects_dir
print("Ensure fsaverage data is available in subjects_dir")
if not os.path.exists(os.path.join(subjects_dir, 'fsaverage', 'bem', 'inner_skull.surf')):
    print("Downloading fsaverage subject data...")
    mne.datasets.fetch_fsaverage(subjects_dir=subjects_dir)

# Load your .npy EEG data (assuming electrodes × time samples)
print("Load your .npy EEG data (assuming electrodes × time samples)")
data = np.load("video1_eLORETA.npy")

# Set up MNE info structure, needed for creating an MNE Raw object
print("Set up MNE info structure, needed for creating an MNE Raw object")
info = mne.create_info(ch_names=['eeg' + str(i) for i in range(data.shape[0])],
                       sfreq=125, ch_types='eeg')

# Create an MNE RawArray object
print("Create an MNE RawArray object")
raw = mne.io.RawArray(data, info)

# Apply a standard 10-20 montage to set channel locations
print("Apply a standard 10-20 montage to set channel locations")
montage = mne.channels.make_standard_montage("standard_1020")
raw.set_montage(montage)

# Preprocessing: Apply filters if necessary
# Uncomment and adjust this line if you need to filter the data
# raw.filter(1., 40., fir_design='firwin')

# Set up the source space using fsaverage
print("Set up the source space using fsaverage")
src = mne.setup_source_space('fsaverage', subjects_dir=subjects_dir, spacing='oct6')

# Create the BEM model and solution
print("Create the BEM model and solution")
model = mne.make_bem_model(subject='fsaverage', ico=4, conductivity=(0.3,), subjects_dir=subjects_dir)
bem = mne.make_bem_solution(model)

# Create the forward solution (requires a transformation file or alignment matrix)
print("Create the forward solution (requires a transformation file or alignment matrix)")
trans = 'fsaverage'  # 'fsaverage' is used here as a template for generic alignment
fwd = mne.make_forward_solution(raw.info, trans=trans, src=src, bem=bem, eeg=True)

# Create an inverse operator for source localization using eLORETA
print("Create an inverse operator for source localization using eLORETA")
inverse_operator = mne.minimum_norm.make_inverse_operator(raw.info, fwd, bem, loose=0.2)
stc = mne.minimum_norm.apply_inverse_raw(raw, inverse_operator, lambda2=1.0 / 9.0, method='eLORETA')

# Visualize the result on the brain model
print("Visualize the result on the brain model")
brain = stc.plot(subject='fsaverage', subjects_dir=subjects_dir, initial_time=0.1)


# Simulate time series data for EEG signal
time = np.linspace(0, 10, 1000)  # 10 seconds of data at 1000 samples
signal = 0.5 * np.sin(2 * np.pi * 7 * time) + 0.25 * np.sin(2 * np.pi * 15 * time) + np.random.normal(0, 0.05, time.shape)

# Plot the signal
plt.figure(figsize=(12, 6))
plt.plot(time, signal, label="EEG Signal")
plt.title("Simulated EEG Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

print("Source localization complete.")
