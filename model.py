from eeg_source_loc import subjects_dir


model = mne.make_bem_model(subject='fsaverage', ico=4, conductivity=(0.3,), subjects_dir=subjects_dir)