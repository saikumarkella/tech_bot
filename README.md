## Tech-Bot

**Running the Tech-Bot in 2 ways.**
    
    1. Using Python command
    2. By Running Docker.

**Using Python Commans** 
    
    - Install dependenceis 
        > pip install -r requirements.txt

    - run the app file using streamlit
        > streamlit run app.py

    Note: please export environment variables i.e Open AI key and Brave Search Key.
        For linux
        > export OPENAI_KEY=*******your openai key*****
        > export BRAVE_KEY=********your brave search key****

        For windows
        > set OPENAI_KEY=*******your openai key*****
        > set BRAVE_KEY=********your brave search key****

**using Docker**

    - Build docker image
        > docker build --tag image_name

    - Run the docker image
        > docker run image_name

    Note : Please modify the OPENAI API key in dockerfile.

    
        



