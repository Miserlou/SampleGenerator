#! /bin/bash
docker build -t miserlou/blas .
docker run -it --volume `pwd`:/derp miserlou/blas /bin/bash -c 'pip install /derp/knnimpute/; pip install /derp/fancyimpute/; cd /derp; echo "Now run: python impute.py blah_the_file_25000.txt"; bash'
