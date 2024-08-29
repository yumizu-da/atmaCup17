FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y curl git &&\
    apt-get upgrade -y && \
    apt-get clean

WORKDIR /workspace
ENV PATH="/root/.cargo/bin/:${PATH}"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY .python-version pyproject.toml uv.lock README.md ./
RUN uv python pin "$(cat .python-version)" && \
    uv sync --dev
