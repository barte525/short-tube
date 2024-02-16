The console application takes a link to a YouTube video as input and provides the option to summarize it using one of three models:

- Bart summarizer CNN (https://huggingface.co/philschmid/bart-large-cnn-samsum)
- Facebook Bart summarizer CNN (https://huggingface.co/facebook/bart-large-cnn)
- Sbert based summarizer												

If a particular film is already in the video_transcripts folder, it is not downloaded. The application provides the option to clean the folder.

To set up the project
1) Download the repository
2) Have Docker installed
3) Build the container using the command: docker-compose up --build

To use the application, enter the container, navigate to the workspace folder, and execute the program with the command:

python3 run.py

To run tests, execute the command:

python3 -m unittest tests/models_test.py
