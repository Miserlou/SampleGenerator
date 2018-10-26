FROM aleksaro/python3-base 

##########################################
# 1. Copy relevant files into container.
##########################################

COPY knnimpute/ /derp/
COPY fancyimpute/ /derp/

RUN pip install click pandas
