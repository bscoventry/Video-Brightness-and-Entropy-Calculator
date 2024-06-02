# Video Brightness and Complexity Calculator
Calculates the brightness and complexity as information entropy of a video

# Necessary packages and conda installation
To create a conda environment to run this code, start by
```
conda create -n VideoAnalysis python=3.10           
conda activate VideoAnalysis
```
Other versions of Python may work, but only 3.10 was tested. 
Only a few packages are needed. Install the following:
```
pip install numpy
pip install Pyarrow
pip install pandas
pip install scipy
pip install opencv-python
pip install matplotlib
```
# Running the program
To run the program on a list of videos, open VideoStatistics.py in an IDE (Visual Studio Code or similar). Move down to variable name VidList. This is the list of videos you want to calculate brightness and complexity on. Videos 
should be stored in a seperate folder. Mine is set to C://CodeRepos//Videos but this can be changed to any directory. Once these are set, simply run
```
python VideoStatistics.py
```
In the directory containing VideoStatistics.py, a new file "Brightness_Complexity.csv" will have been created.

# A note on Complexity
Complexity here is measured as the frame by frame entropy measured in bits as Shannon entropy. Mean entropy here is thus frame-by-frame mean entropy across the entire video. Because this is Shannon entropy, a fully static frame, such as an all white or all black frame will have an entropy value of 0. 
