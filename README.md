# pokemon_catcher_-_discord_bot

This is a python script that sends a message to a discord channel to catch a pokemon of the [Toasty bot](https://toastybot.com/features). It is scheduled to run every 3 hours and 10 seconds.

:warning: This is not a Discord bot. :warning:

*Please follow the [installation tutorial](#installation) if you want to change the location, locally or on another machine, of the API !**

---

## Technologies :
- [Python](https://www.python.org/) 3.6
- [dotenv](https://pypi.org/project/python-dotenv/) 1.0.0 - Reads the key-value pair from .env file and adds them to environment variable. In this project, it is used to get the project private constants.
- [os](https://docs.python.org/3/library/os.html) - Miscellaneous operating system interfaces. In this project, it is used to get the current working directory.
- [request](https://pypi.org/project/requests/) 2.25.1 - Requests is an elegant and simple HTTP library for Python, built for human beings. In this project, it is used to send a message to the discord channel.

---

## Installation

1. Clone the repository
2. Open the project in vscode
3. Open the terminal (```ctrl + ù```)
4. Create a virtual environment : ```python -m venv env```
5. Configure the path to python in local environment :
   1. Open the command palette (```ctrl + shift + p```)
   2. Select *Preferences: Open Workspace Settings*
   3. Click on *Open settings.json* icon : ![go-to-file icon](https://raw.githubusercontent.com/microsoft/vscode-codicons/main/src/icons/go-to-file.svg) (*top right*)
   
   A *.vscode* folder has been created with a *settings.json* file inside.

   4. Paste this following code line in the *settings.json* file :
        ```json
         {    
            "python.defaultInterpreterPath": "${workspaceFolder}\\env\\Scripts\\python"
         }
        ```
   5. Save the file (```ctrl + s```)
6. Open a python terminal (*first time*) :
   1. Kill the current terminal : ![trash icon](https://raw.githubusercontent.com/microsoft/vscode-codicons/main/src/icons/trash.svg)
   2. Open a python file (or create a new one)
   3. Re-open the terminal (```ctrl + ù```)

**Now, you are able re-open the python terminal, whatever the file you are working on.**

7. Install the dependencies : ```pip install -r requirements.txt```
8. Add the project private constants :
   1. Create a *.env* file at the root of the project
   2. Add the following constants :
      ```env
      DISCORD_TOKEN = <your_discord_token>
      DISCORD_CHANNEL_ID = <your_discord_channel_id>
      ```
      - *DISCORD_TOKEN* : You can get it on the browser Discord app by pressing F12, going to the *Network* tab, send a message in a channel and copy the *Authorization* key in the *Request Headers* section of the message request.</br>
      :warning: *Do it in a private browser and don't log out from Discord! The window can be closed.*
      - *DISCORD_CHANNEL_ID* : The id of the channel where you want to send the message. You can get it by activating the *Developer Mode* in the *Advanced* section of the *Appearance* tab in the *User Settings*.

**Now, you are able to run the script.**
```bash
python pokemon_catcher.py
```

---

## Schedule the script execution task

### Windows :
1. Open the windows tool *Task Scheduler*
2. Create a new task :
   1. General tab :
      - Name : *Pokemon Catcher*
      - Description : *Catch pokemon in discord*
      - Security options : *Run whether user is logged on or not*
   2. Triggers tab :
      - New :
         - Begin the task : *At startup*
         - Repeat task every : *3 hours and 10 second*
         - Repeat task every : *Indefinitely*
         - Enabled : *Yes*
   3. Actions tab :
      - New :
         - Action : *Start a program*
         - Program/script : *python.exe*
         - Add arguments : *path/to/pokemon_catcher.py*
         - Start in : *path/to/pokemon_catcher_-_discord_bot*
   4. Conditions tab :
      - Uncheck *Start the task only if the computer is on AC power*
3. Save the task

---

## See
- [Python script video](https://www.youtube.com/watch?v=DArlLAq56Mo)
- [Task Scheduler video](https://www.youtube.com/watch?v=ic4lUiDTbVI)