# Add base image
FROM python:3.11-alpine as dockerapp

# Define new user
ARG USERNAME=devuser
ARG USERGROUP=devgroup

# Create the user
RUN addgroup -S $USERGROUP && adduser -S $USERNAME -G $USERGROUP

# Define work directory
ENV DIRPATH=/home/code

# Create work directory
RUN mkdir -p $DIRPATH

# Define output directory
ENV OUTPUTDIRPATH=/home/output

# Create output directory
RUN mkdir -p $OUTPUTDIRPATH

# Give user access to the output directory
RUN chown $USERNAME $OUTPUTDIRPATH

# Copy script to work directory
COPY ./script.py $DIRPATH

# Set default work directory
WORKDIR $DIRPATH

# Set the default user
USER $USERNAME

# Execute script
CMD [ "python3", "./script.py"]