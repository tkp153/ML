FROM python:3



# ユーザ'vscode'を作成する
# 他のリポジトリではUSER_UIDがベースのイメージですでに使われている場合は別の値を使っています。
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG nvidia/cuda:11.6.0-cudnn8-devel-ubuntu20.04

ARG CUDA_VERSION=cuda-11.6
ARG PYTHON_VERSION=python3
ARG TZ=Asia/Tokyo

ENV DEBIAN_FRONTED=noninteractive
ENV TZ ${TZ}

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVERS_CAPABILITIES=all

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /root

# ユーザの作成と`sudo`の利用設定
# 言語・場所設定
RUN apt-get update \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get -y install locales \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN apt-get -y install curl git

# その他環境変数など
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# vim, less, gccのインストール
RUN apt-get install -y vim less gcc

# 以下 pip
# VSCodeで自動フォーマットやリントの動作をさせるため事前にインストール
RUN apt install -y python3-pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install flake8 autopep8
RUN pip install ipykernel
RUN pip install tqdm
RUN git config --global user.name "syunmame"
RUN git config --global user.email sunqiantian@gmail.com

# サンプルソースで利用しているパッケージとこの後利用しそうなものを追加
RUN pip install python-dotenv fastapi uvicorn
