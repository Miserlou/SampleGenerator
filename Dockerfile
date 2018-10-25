FROM ubuntu:16.04

RUN \
  apt-get update -qq && \
  apt-get install -y lsb-release && \
  echo "deb http://archive.linux.duke.edu/cran/bin/linux/ubuntu $(lsb_release -sc)/" \
      >> /etc/apt/sources.list.d/added_repos.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
  apt-get update -qq && \
  apt-get install -y \
  ed \
  git \
  mercurial \
  libcairo-dev \
  libedit-dev \
  lsb-release \
  python3 \
  python3-pip \
  libpq-dev \
  libxml2-dev \
  libssl-dev \
  libcurl4-openssl-dev \
  curl \
  liblapack-dev \
  gfortran \
  wget && \
  rm -rf /var/lib/apt/lists/*

ENV LAPACK=/usr/lib/liblapack.so
ENV ATLAS=/usr/lib/libatlas.so
ENV BLAS=/usr/lib/libblas.so

RUN pip3 install numpy scipy

ENTRYPOINT []
