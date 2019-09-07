# Imagenette_Imagewoof_Leaderboard
Code package for competing the imagenette_imagewoof leaderboard


Link for official Leaderboard:
https://github.com/fastai/imagenette


With same experimental setup as mentioned in the leaderboard, 
I replaced the Mish activation function with my activation function to get the mentioned scores.

Due to compute capability limitation, (GPU RAM size) 
Leaderboards for size 128 and 192 are experimented for 5 epochs and their results are shared

As the activation function is yet to be published and I am currently working on optimizing it, I haven't 
added the code for my activation function.


Baseline    : Current leaderboard pipeline can be viewed @ https://github.com/lessw2020/Ranger-Mish-ImageWoof-5

My pipeline : Replaced my activation in place of Mish mentioned in the baseline

Dataset	Size	Epochs	Baseline mentioned in Leaderboard	Score achieved during my test			My implementation			Accuracy improvement 	
				scores of 10 runs	Avg 	Std dev	scores of 10 runs	Avg 	Std dev	%  compared to leaderboard baseline	%  compared to my experimental baseline
Imagewoof	128	5	0.7497	[0.764 0.75  0.74  0.73  0.744 0.76  0.75  0.75  0.752 0.734]	0.7474	0.0101	[0.772 0.776 0.77  0.77  0.766 0.756 0.758 0.768 0.768 0.738]	0.7642	0.0104	1.9341	2.2478
	192	5	0.7652	[0.756 0.78  0.766 0.74  0.778 0.75  0.754 0.744 0.736 0.734]	0.7538	0.0156	[0.764 0.796 0.792 0.76  0.782 0.772 0.782 0.762 0.766 0.758]	0.7734	0.0130	1.0716	2.6001
Imagenette	128	5	0.8968	[0.9   0.898 0.894 0.88  0.898 0.902 0.9   0.894 0.89  0.894]	0.895	0.0061	[0.898 0.898 0.906 0.886 0.91  0.888 0.874 0.884 0.886 0.89 ]	0.892	0.0104	-0.5352	-0.3352
	192	5	0.9068	[0.908 0.904 0.9   0.918 0.896 0.908 0.908 0.916 0.904 0.906]	0.9068	0.0063	[0.91  0.924 0.92  0.902 0.91  0.916 0.912 0.908 0.902 0.912]	0.9116	0.0067	0.5293	0.5293

