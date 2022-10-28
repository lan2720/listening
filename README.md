## 使用指南
- 目标网站视频下载成mp3
- mp3转成wav(语音识别库只认识wav格式): pydub需要用到ffmpeg，只在mac上安装成功，centos7没有安装成功，因此这一步`只能在mac上进行`
- audio转text: 由于pocketsphinx库只在gpu15机器的pip安装成功，在mac的conda环境下pip会卡住，因此这一步`只能在gpu15上进行`