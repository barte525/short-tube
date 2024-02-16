Console aplication takes a link to a YouTube video as an input and provides the option to summarize it using one of three models:

- bart summarizer cnn (https://huggingface.co/philschmid/bart-large-cnn-samsum)
- facebok bart summarizer cnn (https://huggingface.co/facebook/bart-large-cnn)
- sbert based summarizer												

If a particular film is already in the video_transcripts folder, it is not downloaded. The application provides the option to clean the folder.

To set up the project
1) Download the repository
2) Have Docker installed
3) Build the container using the command: docker-compose up --build

To use the application, enter the container terminal, navigate to the workspace folder, and execute the program with the command:
python3 run.py
To run tests, execute the command:
python3 -m unittest tests/models_test.py
