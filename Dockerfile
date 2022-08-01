ARG PYTHON_VER=3.10
ARG PACKAGE_NAME=interview_algorand
ARG PACKAGE_VER=0.1.0
FROM python:${PYTHON_VER} as base

RUN apt-get update && \
    apt-get upgrade -y

#############################
# Build the application
#############################
FROM base as builder

RUN useradd -m -s /bin/bash -u 1000 -U builder && \
    mkdir /tmp/build

COPY --chown=builder:builder . /tmp/build/

USER builder
WORKDIR /tmp/build/
RUN curl -sSL https://install.python-poetry.org | POETRY_PREVIEW=1 python3 - && \
    /home/builder/.local/bin/poetry build

#############################
# Runtime for the application
#############################
FROM base as runtime
ARG PACKAGE_NAME
ARG PACKAGE_VER

RUN useradd -m -s /bin/bash -u 1000 -U runtime
COPY --from=builder /tmp/build/dist/ /tmp/
USER runtime
RUN echo 'export PATH=/home/runtime/.local/bin:\$PATH' >> /home/runtime/.bashrc && \
    pip install --user /tmp/${PACKAGE_NAME}-${PACKAGE_VER}-py3-none-any.whl
