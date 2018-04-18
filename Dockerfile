FROM python:3.6.4

RUN apt-get update

RUN apt-get -y install build-essential cmake
RUN apt-get -y install libopenblas-dev liblapack-dev
RUN pip install dlib

RUN apt-get -y install sudo
RUN git clone https://github.com/torch/distro.git /torch
WORKDIR /torch
RUN bash install-deps
RUN ./install.sh

RUN ln -s /torch/install/bin/* /usr/local/bin

RUN luarocks install dpnn
RUN luarocks install graphicsmagick
RUN luarocks install torchx
RUN luarocks install csvigo

RUN git clone https://github.com/cmusatyalab/openface.git /openface
WORKDIR /openface
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install
RUN ./models/get-models.sh

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]