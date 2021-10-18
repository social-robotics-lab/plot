# plot
Pythonでグラフ描画する

# Install
```
git clone https://github.com/social-robotics-lab/plot.git
cd plot
docker build -t plot .
```

# Run
```
docker run -it --name plot --mount type=bind,source="$(pwd)"/src,target=/tmp --rm plot /bin/bash
python sample.py
```